__author__ = 'bluzky'
import unittest
import hashlib

from base import WbTescase
from controller.user import User
from model.user import User as DBUser
from lib.exceptions import InvalidFieldError


class TestUpdateUser(WbTescase):
    @classmethod
    def setUpClass(cls):
        WbTescase.setUpClass()
        args = {
            "email": "admin@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "first_name": "Admin",
            "last_name": "Nguyen",
            "brief": "Hello world"
        }
        user1 = User.add(**args)

        args["email"] = "editor2@gmail.com"
        args["first_name"] = "Editor2"
        user2 = User.add(**args)

        args["email"] = "editor3@gmail.com"
        args["first_name"] = "Editor3"
        user3 = User.add(**args)

        args["email"] = "editor4@gmail.com"
        args["first_name"] = "Editor4"
        user4 = User.add(**args)
        cls.user_id = [user1.id, user2.id, user3.id, user4.id]

    def test_update_user_all_valid_field(self):
        args = {
            "email": "changed@gmail.com",
            "password": "abcxyz",
            "confirm_password": "abcxyz",
            "first_name": "Dzung",
            "last_name": "Nguyen Tien",
            "brief": "Hello world Again"
        }

        User.update_user(self.user_id[0], **args)
        user = DBUser.get_by_id(self.user_id[0])

        self.assertEqual(user.id, self.user_id[0])
        self.assertEqual(user.email, args["email"])
        self.assertEqual(user.password, hashlib.md5(args["password"]).hexdigest())
        self.assertEqual(user.first_name, args["first_name"])
        self.assertEqual(user.last_name, args["last_name"])
        self.assertEqual(user.brief, args["brief"])

    def test_update_no_info(self):
        args = {
            "email": "editor2@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "first_name": "Editor2",
            "last_name": "Nguyen",
            "brief": "Hello world"
        }

        User.update_user(self.user_id[1])
        user = DBUser.get_by_id(self.user_id[1])

        self.assertEqual(user.id, self.user_id[1])
        self.assertEqual(user.email, args["email"])
        self.assertEqual(user.password, hashlib.md5(args["password"]).hexdigest())
        self.assertEqual(user.first_name, args["first_name"])
        self.assertEqual(user.last_name, args["last_name"])
        self.assertEqual(user.brief, args["brief"])

    def test_update_info_bad_email(self):
        args = {
            "email": "changedmail.com",
        }

        try:
            User.update_user(self.user_id[0], **args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_update_info_password_not_matched(self):
        args = {
            "password": "123456",
            "confirm_password":"123"
        }

        try:
            User.update_user(self.user_id[0], **args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_update_info_bad_name_first_name(self):
        args = {
            "first_name": "",
            "last_name" : "me again"
        }

        try:
            User.update_user(self.user_id[0], **args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_update_info_bad_name_last_name(self):
        args = {
            "first_name": "Hello",
            "last_name" : ""
        }

        try:
            User.update_user(self.user_id[0], **args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

if __name__ == '__main__':
    unittest.main()
