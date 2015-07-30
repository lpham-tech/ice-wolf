__author__ = 'bluzky'
import unittest
from base import WbTescase
from controller.user import User
from lib.exceptions import InvalidFieldError, UserNotFoundError, AccessDeniedError


class TestDeleteUser(WbTescase):

    @classmethod
    def setUpClass(cls):
        WbTescase.setUpClass()
        args = {
            "email": "admin2@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "first_name": "Admin",
            "last_name": "Nguyen",
            "brief": "Hello world"
        }

        manager = User.add(**args)
        manager.role = "manager"
        manager.update()
        cls.manager = manager


        cls.user_id = [1,2,3,4]

    def test_delete_user_ideal_case(self):
        try:
            User.delete_user(self.manager.id, self.user_id[0])
        except Exception as e:
            self.fail("Not expect exception")

    def test_delete_user_not_exist(self):
        try:
            User.delete_user(self.manager.id, 44444)
            self.fail("Expect UserNotFoundError")
        except UserNotFoundError as e:
            pass

    def test_delete_user_not_by_manager(self):
        try:
            User.delete_user(self.user_id[1], self.user_id[2])
            self.fail("Expect AccessDeniedError")
        except AccessDeniedError as e:
            pass



if __name__ == '__main__':
    unittest.main()
