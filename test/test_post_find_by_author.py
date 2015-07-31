__author__ = 'bluzky'
__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from lib.exceptions import UserNotFoundError, InvalidFieldError


class TestFindPosByUser(WbTescase):
    def test_find_post_with_valid_info(self):
        posts, author = Post.find_post_by_author(3, 1, 3)
        self.assertEqual(len(posts), 3)

    def test_find_post_without_pagination_param(self):
        posts, author = Post.find_post_by_author(3)
        self.assertEqual(len(posts), 5)


    def test_find_post_with_invalid_pagination_param(self):
        posts, author = Post.find_post_by_author(3, 0, -2)
        self.assertEqual(len(posts), 5)

    def test_find_post_with_out_of_range_index(self):
        posts, author = Post.find_post_by_author(3, 4, 7)
        self.assertEqual(len(posts), 0)

    def test_find_post_with_not_exist_author(self):

        try:
            posts = Post.find_post_by_author(10, 4, 7)
            self.fail("Expect UserNotFoundError")
        except UserNotFoundError:
            pass

    def test_find_post_with_invalid_author_id(self):

        try:
            Post.find_post_by_author("abc")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
