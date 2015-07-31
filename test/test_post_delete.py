__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from model.post import Post as DBPost
from lib.exceptions import AccessDeniedError, PostNotFoundError


class TestDeletePost(WbTescase):
    def test_delete_post_all_field_valid(self):
        args = {
            "user_id": 1,
            "post_id": 1
        }

        Post.delete_post(**args)
        post = DBPost.get_by_id(1)
        self.assertIsNone(post)

    def test_delete_post_by_manager(self):
        args = {
            "user_id": 1,
            "post_id": 2
        }

        Post.delete_post(**args)
        post = DBPost.get_by_id(2)
        self.assertIsNone(post)

    def test_delete_post_without_permission(self):
        """
        user who want to delete pos is not the author or manager
        :return:
        """
        args = {
            "user_id": 2,
            "post_id": 3
        }

        try:
            Post.delete_post(**args)
            self.fail("Expect AccessDeniedError")
        except AccessDeniedError:
            pass

    def test_delete_not_exist_post(self):
        args = {
            "user_id": 2,
            "post_id": 100
        }

        try:
            Post.delete_post(**args)
            self.fail("Expect PostNotFoundError")
        except PostNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
