__author__ = 'bluzky'
import unittest
from persistent.comment import Comment as DBComment
from business.comment import Comment
from base import WbTescase
from lib.exceptions import InvalidFieldError, PostNotFoundError


class TestUserAddComment(WbTescase):

    def test_add_comment_ideal_case(self):
        args={
            "user_id": 1,
            "post_id": 2,
            "content": "This is my first comment on this page"
        }

        cm = Comment.add_comment(**args)
        self.assertIsNotNone(cm)

        comment = DBComment.get_by_id(cm.id)
        self.assertIsNotNone(comment)
        self.assertEqual(comment.user_id, args["user_id"])
        self.assertEqual(comment.post_id, args["post_id"])
        self.assertEqual(comment.content, args["content"])

    def test_add_comment_invalid_post_id(self):
        args={
            "user_id": 1,
            "post_id": -2,
            "content": "This is my first comment on this page"
        }

        try:
            Comment.add_comment(**args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_add_comment_with_not_exist_post(self):
        args={
            "user_id": 1,
            "post_id": 200,
            "content": "This is my first comment on this page"
        }

        try:
            Comment.add_comment(**args)
            self.fail("Expect PostNotFoundError")
        except PostNotFoundError:
            pass

    def test_add_comment_with_empty_comment(self):
        args={
            "user_id": 1,
            "post_id": 1,
            "content": ""
        }

        try:
            Comment.add_comment(**args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

if __name__ == "__main__":
    unittest.main()