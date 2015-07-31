__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from lib.exceptions import InvalidFieldError


class TestGetPost(WbTescase):
    def test_get_post_valid(self):
        post = Post.get_post(1)
        self.assertIsNotNone(post)

    def test_get_post_with_negative_id(self):
        try:
            post = Post.get_post(-1)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_get_post_with_string_id(self):
        try:
            post = Post.get_post("abc")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


    def test_get_post_not_exist(self):
        post = Post.get_post(122)
        self.assertIsNone(post)


if __name__ == '__main__':
    unittest.main()
