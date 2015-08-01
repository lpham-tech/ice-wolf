__author__ = 'bluzky'
import unittest
from persistent.comment import Comment as DBComment
from controller.comment import Comment
from base import WbTescase
from lib.exceptions import InvalidFieldError, CommentNotFoundError, AccessDeniedError


class TestUpdateComment(WbTescase):

    def test_update_comment_ideal_case(self):
        args={
            "user_id": 2,
            "comment_id": 1,
            "content": "new comment content here"
        }

        cm = Comment.update_comment(**args)
        self.assertIsNotNone(cm)

        comment = DBComment.get_by_id(1)
        self.assertIsNotNone(comment)
        self.assertEqual(comment.user_id, args["user_id"])
        self.assertEqual(comment.content, args["content"])


    def test_update_comment_invalid_comment_id(self):
        args={
            "user_id": 2,
            "comment_id": -2,
            "content": "This is my first comment on this page"
        }

        try:
            Comment.update_comment(**args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_update_comment_with_not_exist_comment(self):
        args={
            "user_id": 2,
            "comment_id": 200,
            "content": "This is my first comment on this page"
        }

        try:
            Comment.update_comment(**args)
            self.fail("Expect CommentNotFoundError")
        except CommentNotFoundError:
            pass

    def test_update_comment_with_empty_comment(self):
        args={
            "user_id": 2,
            "comment_id": 1,
            "content": ""
        }

        try:
            Comment.update_comment(**args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_update_others_comment(self):
        args={
            "user_id": 2,
            "comment_id": 2,
            "content": "Hello world"
        }

        try:
            Comment.update_comment(**args)
            self.fail("Expect AccessDeniedError")
        except AccessDeniedError:
            pass

if __name__ == "__main__":
    unittest.main()