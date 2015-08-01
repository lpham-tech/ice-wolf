__author__ = 'bluzky'
import unittest
from persistent.comment import Comment as DBComment
from business.comment import Comment
from base import WbTescase
from lib.exceptions import InvalidFieldError, CommentNotFoundError, AccessDeniedError


class TestDeleteComment(WbTescase):

    def test_delete_comment_ideal_case(self):
        args={
            "user_id": 2,
            "comment_id": 1,
        }

        Comment.delete_comment(**args)

        comment = DBComment.get_by_id(1)
        self.assertIsNone(comment)

    def test_delete_comment_by_post_author(self):
        args={
            "user_id": 2,
            "comment_id": 10,
        }

        Comment.delete_comment(**args)

        comment = DBComment.get_by_id(10)
        self.assertIsNone(comment)


    def test_delete_comment_invalid_comment_id(self):
        args={
            "user_id": 2,
            "comment_id": -2,
        }

        try:
            Comment.delete_comment(**args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass

    def test_delete_comment_with_not_exist_comment(self):
        args={
            "user_id": 2,
            "comment_id": 200,
        }

        try:
            Comment.delete_comment(**args)
            self.fail("Expect CommentNotFoundError")
        except CommentNotFoundError:
            pass


    def test_delete_others_comment(self):
        args={
            "user_id": 2,
            "comment_id": 2,
        }

        try:
            Comment.delete_comment(**args)
            self.fail("Expect AccessDeniedError")
        except AccessDeniedError:
            pass

if __name__ == "__main__":
    unittest.main()