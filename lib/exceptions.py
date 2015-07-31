__author__ = 'bluzky'

class InvalidFieldError(Exception):
    def __init__(self, msg, error_fields = []):
        self.error_fields = error_fields
        super(InvalidFieldError, self).__init__(msg)

class UserNotFoundError(Exception):
    def __init__(self, msg=None, name=None, email=None):

        if name:
            msg = "User %s does not exist" % name
            self.username = name
        elif email:
            msg = "User with email %s does not exist" % email
            self.email = email
        elif msg is None:
            msg = "User does not exist"

        super(UserNotFoundError, self).__init__(msg)

class PostNotFoundError(Exception):
    def __init__(self, msg = None, post_id=None):
        if post_id:
            self.post_id = post_id
            msg = "Post with id = %d does not exist"
        elif msg is None:
            msg = "Post does not exist"

        super(PostNotFoundError,self).__init__(msg)

class AccessDeniedError(Exception):
    def __init__(self, msg):
        super(AccessDeniedError,self).__init__(msg)

class InvalidActionError(Exception):
    def __init__(self, msg):
        super(InvalidActionError,self).__init__(msg)