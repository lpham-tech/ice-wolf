__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from lib.exceptions import UserNotFoundError, InvalidFieldError


class TestFindPosByUser(WbTescase):
    def test_find_post_with_valid_info(self):
        pagination, author = Post.find_post_by_author_pagination(3, 1, 3)
        self.assertEqual(len(pagination.items), 3)

    def test_find_post_without_pagination_param(self):
        pagination, author = Post.find_post_by_author_pagination(3)
        self.assertEqual(len(pagination.items), 6)


    def test_find_post_with_invalid_pagination_param(self):
        pagination, author = Post.find_post_by_author_pagination(3, 0, -2)
        self.assertEqual(len(pagination.items), 6)

    def test_find_post_with_out_of_range_index(self):
        pagination, author = Post.find_post_by_author_pagination(3, 4, 7)
        self.assertEqual(len(pagination.items), 0)

    def test_find_post_with_not_exist_author(self):

        try:
            Post.find_post_by_author_pagination(10, 4, 7)
            self.fail("Expect UserNotFoundError")
        except UserNotFoundError:
            pass

    def test_find_post_with_invalid_author_id(self):

        try:
            Post.find_post_by_author_pagination("abc")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
