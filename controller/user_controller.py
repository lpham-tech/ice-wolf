__author__ = 'bluzky'
from flask import session, request, render_template, redirect, abort
from business.user import User
from lib.exceptions import InvalidFieldError, DuplicatedError, UserNotActivatedError


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
            session["user"] = user
            session["logged_in"] = True
            return redirect("/")
        else:
            error = "Email or password does not match"
    except UserNotActivatedError as e:
        error = e.message
    except:
        abort(404)
    return render_template("login.html", error_msg=error)


def update_profile():
    pass
