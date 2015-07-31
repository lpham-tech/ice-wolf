__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from lib.exceptions import InvalidFieldError


class TestFindPosByKeywordWithPagination(WbTescase):
    def test_find_post_with_valid_info(self):
        pagination = Post.find_post_by_keyword_pagination("orem", 1, 3)
        self.assertEqual(len(pagination.items), 3)

    def test_find_post_with_sql_injection(self):
        try:
            pagination = Post.find_post_by_keyword_pagination("Lorem';select * from user;--", 1, 3)
            self.fail("Expect InvalidFieldError")
        except:
            pass

    def test_find_post_without_pagination_param(self):
        pagination = Post.find_post_by_keyword_pagination("Lorem")
        self.assertEqual(len(pagination.items), 10)

    def test_find_post_with_invalid_pagination_param(self):
        pagination = Post.find_post_by_keyword_pagination("Lorem", 0, -2)
        self.assertEqual(len(pagination.items), 10)

    def test_find_post_with_out_of_range_index(self):
        pagination = Post.find_post_by_keyword_pagination("Lorem", 4, 7)
        self.assertEqual(len(pagination.items), 0)

    def test_find_post_with_not_exist_keyword(self):

        pagination = Post.find_post_by_keyword_pagination("Java")
        self.assertEqual(len(pagination.items), 0)

    def test_find_post_with_invalid_categories(self):

        try:
            Post.find_post_by_keyword_pagination("")
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
