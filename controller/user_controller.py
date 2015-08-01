__author__ = 'bluzky'
from flask import session, request, render_template, redirect, url_for
from business.user import User
from lib.exceptions import InvalidFieldError, DuplicatedError

def register_user():
    error = None
    args={
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["re_password"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
    }
    
    try:
        User.add(**args)
        return redirect("/")
    except DuplicatedError as e:
        error = e.message
    except InvalidFieldError as e:
        fields = ", ".join(e.error_fields)
        if len(e.error_fields) == 1:
            v,o = "is", "it"
        else:
            v,o = "are", "them"
        error = "{0} {1} invalid. Please correct {2} and submit again".format(fields, v, o)
    #except Exception as e:
        error = "Fail to create new account. Please try again later."
    return render_template("register.html",error_msg=error)




def login():
    pass

def logout():
    pass

def update_profile():
    pass
