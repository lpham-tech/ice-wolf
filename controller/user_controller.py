__author__ = 'bluzky'
from flask import session, request, render_template, redirect, abort, make_response
from business.user import User
from persistent import User as DBUser
from lib.exceptions import InvalidFieldError, DuplicatedError, UserNotActivatedError
from flask_login import LoginManager, login_user, logout_user
from config import app

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
        User.add(**args)
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
        # except Exception as e:
        error = "Fail to create new account. Please try again later."
    return render_template("register.html", error_msg=error)


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
    session.pop("user", None)
    session.pop("logged_in", None)
    return redirect("/")

@login_manager.user_loader
def load_user(id):
    return DBUser.get_by_id(int(id))

def update_profile():
    pass
