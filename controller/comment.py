__author__ = 'bluzky'
from model.comment import Comment as DBComment
from model.post import Post as DBPost
from lib.utils import is_id_valid
from lib.exceptions import InvalidFieldError, PostNotFoundError


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
    def update_comment(cls, comment_id, content):
        pass

    @classmethod
    def delete_comment(cls, comment_id):
        pass