__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from lib.exceptions import UserNotFoundError, InvalidFieldError


class TestFindPosByCategory(WbTescase):
    def test_find_post_with_valid_info(self):
        posts = Post.find_post_by_category("Python", 1, 3)
        self.assertEqual(len(posts), 3)

    def test_find_post_without_pagination_param(self):
        posts = Post.find_post_by_category("NON IT")
        self.assertEqual(len(posts), 6)


    def test_find_post_with_invalid_pagination_param(self):
        posts = Post.find_post_by_category("NON IT", 0, -2)
        self.assertEqual(len(posts), 6)

    def test_find_post_with_out_of_range_index(self):
        posts = Post.find_post_by_category("C++", 4, 7)
        self.assertEqual(len(posts), 0)

    def test_find_post_with_not_exist_category(self):

        posts = Post.find_post_by_category("Java", 4, 7)
        self.assertEqual(len(posts), 0)


    def test_find_post_with_invalid_categories(self):

        try:
            Post.find_post_by_category("")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
