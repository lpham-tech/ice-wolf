__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from lib.exceptions import UserNotFoundError, InvalidFieldError


class TestFindPosByCategory(WbTescase):
    def test_find_post_with_valid_info(self):
        pagination = Post.find_post_by_category_pagination("Python", 1, 3)
        self.assertEqual(len(pagination.items), 3)

    def test_find_post_without_pagination_param(self):
        pagination = Post.find_post_by_category_pagination("NON IT")
        self.assertEqual(len(pagination.items), 7)


    def test_find_post_with_invalid_pagination_param(self):
        pagination = Post.find_post_by_category_pagination("NON IT", 0, -2)
        self.assertEqual(len(pagination.items), 7)

    def test_find_post_with_out_of_range_index(self):
        pagination = Post.find_post_by_category_pagination("C++", 4, 7)
        self.assertEqual(len(pagination.items), 0)

    def test_find_post_with_not_exist_category(self):

        pagination = Post.find_post_by_category_pagination("Java", 4, 7)
        self.assertEqual(len(pagination.items), 0)


    def test_find_post_with_invalid_categories(self):

        try:
            Post.find_post_by_category_pagination("")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
