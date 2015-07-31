__author__ = 'bluzky'
from model.post import Post as DBPost
from model.user import User as DBUser
from datetime import datetime

from lib.exceptions import InvalidFieldError, AccessDeniedError, UserNotFoundError, PostNotFoundError


class Post(object):
    @classmethod
    def add_post(cls, user_id, title, content, feature_image=None, tags = None, categories = None, draft=False):

        # not need to check author existent

        #if title is empty, use curent date as title
        if len(title) == 0:
            time = datetime.now()
            title = time.strftime("%A %d %B %Y")

        if not content:
            raise InvalidFieldError("Post's content could not be empty", ["content"])

        args = {
            "user_id": user_id,
            "title" : title,
            "content" : content,
            "feature_image": feature_image,
            "tags":tags,
            "categories":categories,
            "draft":draft
        }

        post = DBPost(**args)
        try:
            post.save()
            return post
        except:
            raise


    @classmethod
    def update_post(cls, user_id, post_id, title = None, content = None, feature_image=None, tags = None, categories = None, draft=False):
        # only allow author or manager to edit post
        user = DBUser.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User with id = %d does not exist" % user_id )

        post = DBPost.get_by_id(post_id)
        if not post:
            raise PostNotFoundError(post_id=post_id)

        if post.author.id != user_id and user.role != "manager":
            raise AccessDeniedError("You cannot edit post not published by you.")

        if title:
            post.title = title

        if content:
            post.content = content
        elif content is not None and len(content) == 0:
            raise InvalidFieldError("Post's content cannot be empty", ["content"])

        if feature_image:
            post.feature_image = feature_image

        if tags:
            post.tags = tags

        if categories:
            post.categories = categories

        post.update()
        return post



    @classmethod
    def get_post(cls, post_id):
        pass

    @classmethod
    def get_list_post(cls, page = 0, post_each_page=20):
        pass

    @classmethod
    def get_post_by_category(cls, category_name, page=0, post_each_page=20):
        pass

    @classmethod
    def get_post_by_author(cls, author_id, page=0, post_each_page=20):
        pass

    @classmethod
    def delete_post(cls, user_id, post_id):
        user = DBUser.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User with id = %d does not exist" % user_id )

        post = DBPost.get_by_id(post_id)
        if not post:
            raise PostNotFoundError(post_id=post_id)

        #only allow author and manager to delete post
        if post.author.id != user_id and user.role != "manager":
            raise AccessDeniedError("You don't have permission to delete this post.")

        post.delete()


