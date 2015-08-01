__author__ = 'bluzky'
import unittest

from base import WbTescase
from business.post import Post


class TestGetPostList(WbTescase):
    def test_get_post_list_valid(self):
        posts = Post.get_posts(1, 5)
        self.assertEqual(len(posts), 5)

    def test_get_post_list_without_param(self):
        posts = Post.get_posts()
        self.assertEqual(len(posts), 10)


    def test_get_post_list_with_invalid_param(self):
        posts = Post.get_posts(0, -2)
        self.assertEqual(len(posts), 10)

    def test_get_post_list_with_out_of_range_id(self):
        posts = Post.get_posts(4, 7)
        self.assertEqual(len(posts), 0)

if __name__ == '__main__':
    unittest.main()
