__author__ = 'bluzky'
from model.comment import Comment as DBComment
from model.post import Post as DBPost
from model.user import User as DBUser
from lib.utils import is_id_valid
from lib.exceptions import InvalidFieldError, PostNotFoundError, UserNotFoundError, CommentNotFoundError, AccessDeniedError


class Comment(object):
    @classmethod
    def add_comment(cls, post_id, user_id, content):
        if not is_id_valid(post_id):
            raise InvalidFieldError("post id is invalid", ["post_id"])

        # not need to check user id for logged in user
        # if not is_id_valid(user_id):
        #     raise InvalidFieldError("user id is invalid", ["user_id"])

        post = DBPost.get_by_id(post_id)
        if not post:
            raise PostNotFoundError(post_id=post_id)

        if len(content) < 10:
            raise InvalidFieldError("comment is too short", ["content"])

        args = {
            "post_id": post_id,
            "user_id": user_id,
            "content": content
        }
        comment = DBComment(**args)
        try:
            comment.save()
            return comment
        except:
            return None

    @classmethod
    def update_comment(cls, user_id, comment_id, content):

        # not necessary to check user_id
        # if not is_id_valid(user_id):
        #     raise InvalidFieldError("user id is invalid", ["user_id"])

        if not is_id_valid(comment_id):
            raise InvalidFieldError("comment id is invalid", ["comment_id"])

        commenter = DBUser.get_by_id(user_id)
        if not commenter:
            raise UserNotFoundError("User with id = %d  does not exist" % user_id)

        comment = DBComment.get_by_id(comment_id)
        if not comment:
            raise CommentNotFoundError(comment_id=comment_id)

        if len(content) < 10:
            raise InvalidFieldError("comment is too short", ["content"])

        # only allow commenter to update comment
        if comment.user_id != user_id:
            raise  AccessDeniedError("You cannot edit others comment")

        comment.content = content
        try:
            comment.update()
            return comment
        except:
            raise

    @classmethod
    def delete_comment(cls, user_id, comment_id):
        # not necessary to check user_id
        # if not is_id_valid(user_id):
        #     raise InvalidFieldError("user id is invalid", ["user_id"])

        if not is_id_valid(comment_id):
            raise InvalidFieldError("comment id is invalid", ["comment_id"])

        user = DBUser.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User with id = %d  does not exist" % user_id)

        comment = DBComment.get_by_id(comment_id)
        if not comment:
            raise CommentNotFoundError(comment_id=comment_id)

        # only allow commenter/post author to delete comment
        if comment.user_id != user_id and comment.post.id != user_id:
            raise  AccessDeniedError("You cannot delete others comment")

        try:
            comment.delete()
            return comment
        except:
            raise
