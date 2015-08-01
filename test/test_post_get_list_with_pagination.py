__author__ = 'bluzky'
import unittest

from base import WbTescase
from business.post import Post


class TestGetPostListWithPagination(WbTescase):
    def test_get_post_list_valid(self):
        pagination = Post.get_posts_pagination(1, 5)
        self.assertEqual(len(pagination.items), 5)

    def test_get_post_list_without_param(self):
        pagination = Post.get_posts_pagination()
        self.assertEqual(len(pagination.items), 10)

    def test_get_post_list_with_invalid_param(self):
        pagination = Post.get_posts_pagination(0, -2)
        self.assertEqual(len(pagination.items), 10)

    def test_get_post_list_with_out_of_range_id(self):
        pagination = Post.get_posts_pagination(4, 7)
        self.assertEqual(len(pagination.items), 0)

if __name__ == '__main__':
    unittest.main()
