__author__ = 'bluzky'
from flask import request, render_template, redirect, abort, make_response, session
from business.user import User
from persistent import User as DBUser
from lib.exceptions import InvalidFieldError, DuplicatedError, UserNotActivatedError
import lib.utils
from flask_login import LoginManager, login_user, logout_user, current_user
from config import app
from mail_controller import send_activation_mail

login_manager = LoginManager(app)
login_manager.login_view = "login"

def register_user():
    error = None
    args = {
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["re_password"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }

    try:
        user = User.add(**args)
        send_activation_mail(user)
        if request.args["next"]:
            return redirect(request.args["next"])
        else:
            return redirect("/")
    except DuplicatedError as e:
        error = e.message
    except InvalidFieldError as e:
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
    #log out current user first
    logout()

    from datetime import  datetime
    try:
        info = lib.utils.extract_activation_info(token)
        user = DBUser.get_one({"email":info[0]})

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


def login():
    error = None
    args = {
        "email": request.form["email"],
        "password": request.form["password"]
    }

    try:
        user = User.verify_user(**args)
        if user:
            if "remember" in request.form:
                login_user(user, True)
            else:
                login_user(user)

            # session["user"] = user.public_info()
            # session["logged_in"] = True
            if request.args["next"]:
                response = make_response( redirect(request.args["next"]))
            else:
                response = make_response( redirect("/"))

            return response
        else:
            error = "Email or password does not match"
    except UserNotActivatedError as e:
        error = e.message
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
    pass
