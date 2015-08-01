__author__ = 'bluzky'
import unittest

from base import WbTescase
from business.post import Post
from lib.exceptions import InvalidFieldError


class TestFindPosByKeyword(WbTescase):
    def test_find_post_with_valid_info(self):
        posts = Post.find_post_by_keyword("orem", 1, 3)
        self.assertEqual(len(posts), 3)

    def test_find_post_with_sql_injection(self):
        try:
            posts = Post.find_post_by_keyword("Lorem';select * from user;--", 1, 3)
            self.fail("Expect InvalidFieldError")
        except:
            pass

    def test_find_post_without_pagination_param(self):
        posts = Post.find_post_by_keyword("Lorem")
        self.assertEqual(len(posts), 10)

    def test_find_post_with_invalid_pagination_param(self):
        posts = Post.find_post_by_keyword("Lorem", 0, -2)
        self.assertEqual(len(posts), 10)

    def test_find_post_with_out_of_range_index(self):
        posts = Post.find_post_by_keyword("Lorem", 4, 7)
        self.assertEqual(len(posts), 0)

    def test_find_post_with_not_exist_keyword(self):

        posts = Post.find_post_by_category("Java")
        self.assertEqual(len(posts), 0)

    def test_find_post_with_invalid_categories(self):

        try:
            Post.find_post_by_keyword("")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
