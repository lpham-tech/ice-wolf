__author__ = 'bluzky'
from model.post import Post as DBPost
from datetime import datetime

from lib.exceptions import InvalidFieldError


class Post(object):
    @classmethod
    def add_post(cls, user_id, title, content, feature_image=None, tags = None, categories = None, draft=False):

        # not need to check author existent

        #if title is empty, use curent date as title
        if len(title) == 0:
            time = datetime.now()
            title = time.strftime("%A %d %B %Y")

        if not content:
            raise InvalidFieldError("Post content could not be empty", ["content"])

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
    def update_post(cls, author_id, post_id, title, content, feature_image=None, tags = None, categories = None, draft=False):
        pass

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
    def delete_post(cls, author_id, post_id):
        pass

