__author__ = 'bluzky'
from model.user import User as DBUser
from lib.utils import is_email_address_valid
from lib.exceptions import InvalidFieldError
import hashlib

class User(object):

    @classmethod
    def add(cls, email, password, confirm_password, first_name, last_name, brief=None):

        #validate email
        if not is_email_address_valid(email):
            raise InvalidFieldError("Email address is not valid", ["email"])

        # check matched password
        if password != confirm_password:
            raise InvalidFieldError("Password and confirm password does not match", ["password", "confirm_password"])
        elif len(password) < 6:
            raise InvalidFieldError("Password length must be at least 6 characters", ["password"])
        # validate name
        if len(first_name) == 0 or len(last_name) == 0:
            raise InvalidFieldError("First name and/or last name are in valid", ["first_name", "last_name"])

        args = {
            "email": email,
            "password": hashlib.md5(password).hexdigest(),
            "first_name": first_name,
            "last_name": last_name
        }

        if brief:
            args["brief"] = brief

        # create activate id
        user = DBUser(**args)
        user.activation_id = hashlib.md5(email+password).hexdigest()

        #persistent user object
        try:
            user.save()
            return user
        except:
            raise




