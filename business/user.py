__author__ = 'bluzky'
import hashlib

from persistent.user import User as DBUser
from lib.utils import is_email_address_valid
from lib.exceptions import InvalidFieldError, AccessDeniedError, UserNotFoundError, UserNotActivatedError


class User(object):
    @classmethod
    def add(cls, email, password, confirm_password, first_name, last_name, brief=None):

        # validate email
        if not is_email_address_valid(email):
            raise InvalidFieldError("Email address is not valid", ["email"])

        # check matched password
        if password != confirm_password:
            raise InvalidFieldError("Password and confirm password does not match", ["password", "confirm_password"])
        elif len(password) < 6:
            raise InvalidFieldError("Password length must be at least 6 characters", ["password"])
        # validate name
        if not first_name or not last_name:
            raise InvalidFieldError("First name and/or last name are in valid", ["first_name", "last_name"])

        args = {
            "email": email.lower(),
            "password": hashlib.md5(password).hexdigest(),
            "first_name": first_name,
            "last_name": last_name
        }

        if brief:
            args["brief"] = brief

        # create activate id
        user = DBUser(**args)
        user.activation_id = hashlib.md5(email + password).hexdigest()

        # persistent user object
        try:
            user.save()
            return user
        except:
            raise

    @classmethod
    def verify_user(cls, email, password):
        # validate input
        if not is_email_address_valid(email) or len(password) < 6:
            return None

        arg = {
            "email": email.lower(),
        }

        password_hashed = hashlib.md5(password).hexdigest()
        user = DBUser.get_one(arg)

        if user :
            if user.activated:
                if user.password == password_hashed:
                    # only return some basic info

                    return user
                else:
                    return None
            else:
                raise UserNotActivatedError(email=user.email)
        else:
            return None

    @classmethod
    def activate_user(cls, email, activation_id):
        # validate input
        if not is_email_address_valid(email):
            return None

        arg = {
            "email": email.lower(),
        }

        user = DBUser.get_one(arg)

        if user :
                if user.activation_id == activation_id:
                    # only return some basic info
                    user.activation_id = ""
                    user.activated = True
                    user.update()
                    return user
                else:
                    return None
        else:
            return None

    @classmethod
    def delete_user(cls, request_user_id, user_delete):
        user = DBUser.get_by_id(request_user_id)
        dl_user = DBUser.get_by_id(user_delete)

        # if not user:
        #     raise UserNotFoundError("user with id = %d does not exist", request_user_id)

        if not dl_user:
            raise UserNotFoundError("user with id = %d does not exist", user_delete)

        if user.role != "manager":
            raise AccessDeniedError("Not manager user cannot delete account")
        else:
            dl_user.delete()

    @classmethod
    def update_user(cls, user_id, email=None, password=None, confirm_password=None, first_name=None, last_name=None,
                    brief=None):
        try:
            user = DBUser.get_by_id(user_id)

            if user is None:
                raise UserNotFoundError("User with id = %d does not exist" %user_id)

            # validate email
            if email and not is_email_address_valid(email):
                raise InvalidFieldError("Email address is not valid", ["email"])
            elif email:
                user.email = email

            if password and confirm_password:
                # check matched password
                if password != confirm_password:
                    raise InvalidFieldError("Password and confirm password does not match", ["password", "confirm_password"])
                elif len(password) < 6:
                    raise InvalidFieldError("Password length must be at least 6 characters", ["password"])
                else:
                    user.password = hashlib.md5(password).hexdigest()

            # validate name
            if first_name is not None and len(first_name) == 0:
                raise InvalidFieldError("First name is in valid", ["first_name"])
            elif first_name:
                user.first_name = first_name

            if last_name is not  None and len(last_name) == 0:
                raise InvalidFieldError("Last name is in valid", ["last_name"])
            elif last_name:
                user.last_name = last_name

            if brief:
                user.brief = brief

            # persistent user object
            user.update()
            return user
        except:
            raise
