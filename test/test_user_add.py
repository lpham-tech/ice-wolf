__author__ = 'bluzky'
import unittest
from base import WbTescase
from controller.user import User
from lib.exceptions import InvalidFieldError


class TestAddUser(WbTescase):
    def test_add_user_ideal_case(self):
        args = {
            "email": "blue@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "first_name": "Dzung",
            "last_name": "Nguyen",
            "brief": "Hello world"
        }

        user = User.add(**args)
        self.assertIsNotNone(user.id)

    def test_add_user_duplicate_email(self):
        args = {
            "email": "blue@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "first_name": "Dzung",
            "last_name": "Nguyen",
            "brief": "Hello world"
        }

        try:
            user = User.add(**args)
            #self.fail("should throw exception")
        except Exception as e:
            print e.message
            pass


if __name__ == '__main__':
    unittest.main()
