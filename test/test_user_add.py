__author__ = 'bluzky'
import unittest
from base import WbTescase
from business.user import User
import time

class TestAddUser(WbTescase):

    def tearDown(self):
        time.sleep(1)

    def test_add_user_ideal_case(self):
        args = {
            "email": "blue2@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "first_name": "Dzung",
            "last_name": "Nguyen",
            "brief": "Hello world"
        }

        user = User.add(**args)
        self.assertIsNotNone(user.id)

    # def test_add_user_duplicate_email(self):
    #     args = {
    #         "email": "blue@gmail.com",
    #         "password": "123456",
    #         "confirm_password": "123456",
    #         "first_name": "Dzung",
    #         "last_name": "Nguyen",
    #         "brief": "Hello world"
    #     }
    #
    #     try:
    #         User.add(**args)
    #
    #         # add duplicate
    #         User.add(**args)
    #         #self.fail("should throw exception")
    #     except Exception as e:
    #         print e.message
    #         pass



if __name__ == '__main__':
    unittest.main()
