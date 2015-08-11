__author__ = 'bluzky'
import uuid

from flask import request, render_template, redirect, abort, make_response, session
from flask_login import LoginManager, login_user, logout_user, current_user
from flaskext.uploads import UploadNotAllowed
from business.user import User
from persistent import User as DBUser
from lib.exceptions import InvalidFieldError, DuplicatedError, UserNotActivatedError
import lib.utils
from config import app, avatars
import mail_controller
from settings import settings

login_manager = LoginManager(app)
login_manager.login_view = "login"


def register_user():
    """
    Register new user account with given info in post param
    :return: rendered page
    """
    error = None
    # 1. collect account detail
    args = {
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["re_password"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }

    try:
        # 2. Try to create new account
        user = User.add(**args)

        # 3. Send mail with activation link to user
        if settings.require_activation:
            mail_controller.send_activation_mail(user)
            return render_template("activation.html", title="Mail sent", result="mail_sent", mail_address=args["email"])

        # 4. Redirect to login page
        if request.args["next"]:
            return redirect(request.args["next"])
        else:
            return redirect("/login")

    except DuplicatedError as e:
        # error if email has been used
        error = e.message
    except InvalidFieldError as e:
        # error if user detail is not valid
        fields = ", ".join(e.error_fields)
        if len(e.error_fields) == 1:
            v, o = "is", "it"
        else:
            v, o = "are", "them"
        error = "{0} {1} invalid. Please correct {2} and submit again".format(fields, v, o)
    except Exception as e:
        error = "Fail to create new account. Please try again later."

    return render_template("register.html", error_msg=error)


def activate_account(token):
    # log out current user first
    logout()

    from datetime import datetime

    try:
        info = lib.utils.extract_activation_info(token)
        user = DBUser.get_one({"email": info[0]})

        # redirect to login page in case user has been activated
        if user and user.activated:
            return redirect('/')

        # check if activation token is expired or not
        expire = datetime.utcfromtimestamp(info[2])
        now = datetime.now()
        if datetime.utcfromtimestamp(info[2]) < datetime.now():
            session["email"] = info[0]
            return render_template("activation.html", title="Token expired", result="expired")

        user = User.activate_user(info[0], info[1])
        # check if activation succeeded or not
        if user:
            return render_template("activation.html", title="Success", result="ok")
        else:
            return render_template("activation.html", title="Invalid link", result="invalid")
    except Exception as e:
        return render_template("activation.html", title="Bad link", result="invalid")


def generate_activation_code():
    try:
        email = session.pop("email", None)
        if email:
            user = DBUser.get_one({"email": email})
            if user:
                return render_template("activation.html", title="Mail sent", result="mail_sent", mail_address=email)
        return render_template("activation.html", title="Account not exist", result="not_exist")
    except Exception as e:
        abort(400)


def generate_activation_code_for_email(email):
    user = DBUser.get_one({"email": email})
    if user:
        return render_template("activation.html", title="Mail sent", result="mail_sent", email=email)

    return render_template("activation.html", title="Account not exist", result="not_exist")


def send_reset_password_email():
    try:
        email = request.form["email"]
        user = DBUser.get_one({"email": email})

        if user:
            user.activation_id = str(uuid.uuid4())
            user.update()
            mail_controller.send_reset_password_email(user)
            return render_template("reset_password.html", show_result=True, email=email)
        else:
            return render_template("reset_password.html",
                                   error_msg="there is no account which associate with %s" % email)
    except Exception as e:
        return render_template("reset_password.html")


def login():
    """
    Login user with given credential in form params
    :return:
    """
    error = None
    args = {
        "email": request.form["email"],
        "password": request.form["password"]
    }

    try:
        user = User.verify_user(**args)
        if user:
            # save user info in Flask-login object
            if "remember" in request.form:
                login_user(user, True)  # auto login for next visit
            else:
                login_user(user)

            # if login is redirect from another page, return back to that page
            if request.args["next"]:
                response = make_response(redirect(request.args["next"]))
            else:
                response = make_response(redirect("/"))  # default redirect to home page
            return response
        else:
            error = "Email or password does not match"
    except UserNotActivatedError as e:
        session["email"] = e.user_email
        # render activation page
        return render_template("activation.html", result='not_activated')

    except Exception as e:
        abort(404)
    return render_template("login.html", error_msg=error)


def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(id):
    return DBUser.get_by_id(int(id))


def update_profile():
    error_msg = ""
    try:
        args = {
            "user_id": current_user.id,
            "first_name": request.form["first_name"] or None,
            "last_name": request.form["last_name"] or None,
            "email": request.form["email"] or None,
            "brief": request.form["brief"] or None
        }
        avatar_photo = request.files.get("avatar")
        try:
            filename = avatars.save(avatar_photo)
            args["avatar"] = avatars.url(filename)
        except UploadNotAllowed:
            error_msg = "The upload was not allowed"
        else:
            user = User.update_user(**args)
            current_user.avatar = user.avatar
            current_user.first_name = user.first_name
            current_user.last_name = user.last_name
            current_user.email = user.email
            current_user.brief = user.brief
            return render_template("profile.html", edit=False)

    except InvalidFieldError as e:
        error_msg = e.message
    except:
        error_msg = "Cannot update your profile, please try again later."

    return render_template("profile.html", error_msg=error_msg)


def login_by_token(token):
    # log out current user first
    logout()

    from datetime import datetime

    try:
        info = lib.utils.extract_activation_info(token)
        user = DBUser.get_one({"email": info[0]})

        # check if activation token is expired or not
        if datetime.utcfromtimestamp(info[2]) < datetime.now():
            return render_template("action_result.html", action="reset_password", result="expired")
        elif user.activation_id == info[1]:
            login_user(user)
            return redirect("/change_password")
        else:
            return render_template("action_result.html", action="reset_password", result="invalid")
    except Exception as e:
        return render_template("action_result.html", action="reset_password", result="invalid")


def update_password():
    try:
        args = {
            "password": request.form["password"],
            "confirm_password": request.form["re_password"]
        }

        User.update_user(user_id=current_user.id, **args)
        return render_template("change_password.html", error_msg="")
    except:
        return render_template("change_password.html", error_msg="Password does not match. Please try again.")
