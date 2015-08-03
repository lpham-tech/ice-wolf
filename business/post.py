__author__ = 'bluzky'
from datetime import datetime

from persistent.post import Post as DBPost
from persistent.user import User as DBUser
from lib.exceptions import InvalidFieldError, AccessDeniedError, UserNotFoundError, PostNotFoundError
from lib.utils import is_id_valid, get_slug_from_string
import default


class Post(object):
    @classmethod
    def add_post(cls, user_id, title, content, feature_image=None, tags=None, categories=None, draft=False):

        # not need to check author existent

        # if title is empty, use curent date as title
        if len(title) == 0:
            time = datetime.now()
            title = time.strftime("%A %d %B %Y")

        if not content:
            raise InvalidFieldError("Post's content could not be empty", ["content"])

        if not categories:
            categories = [default.DEFAULT_CATEGORY]

        args = {
            "user_id": user_id,
            "title": title,
            "content": content,
            "feature_image": feature_image,
            "tags": tags,
            "categories": categories,
            "draft": draft
        }

        post = DBPost(**args)
        try:
            post.save()
            return post
        except:
            raise

    @classmethod
    def update_post(cls, user_id, post_id, title=None, content=None, feature_image=None, tags=None, categories=None,
                    draft=False):
        # only allow author or manager to edit post
        user = DBUser.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User with id = %d does not exist" % user_id)

        if not is_id_valid(post_id):
            raise InvalidFieldError("Post id is invalid", ["post_id"])

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
            post.categories = ",".join("`%s`"%cat for cat in categories)

        post.update()
        return post

    @classmethod
    def get_post(cls, post_id):
        if not is_id_valid(post_id):
            raise InvalidFieldError("Post id is invalid", ["post_id"])
        post = DBPost.get_by_id(post_id)

        # if post:
        #     comments = post.comments.all()
        #
        #     post.comments = comments
        return post

    @classmethod
    def get_posts(cls, page=1, per_page=10):
        """
        Get many post at a time, order by post time
        :param page: page index begin at 1
        :param per_page:
        :return:
        """
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        start = (page - 1) * per_page   # id in sql start at 1
        post_list = DBPost.get(start=start, per_page=per_page, order_by="time desc")
        return post_list

    @classmethod
    def get_posts_pagination(cls, page=1, per_page=10):
        """
        Get many post at a time, order by post time
        :param page: page index begin at 1
        :param per_page:
        :return:
        """
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        pagination = DBPost.pagination_get(page=page, per_page=per_page, order_by="time desc")
        return pagination

    @classmethod
    def find_post_by_keyword(cls, keyword, page=1, per_page=10):
        """
        Find all post publish by specific author

        :param category_name: category name
        :param page: page index begin at 1
        :param per_page:
        :return:
        """

        if not keyword:
            raise InvalidFieldError("category cannot be empty", ["search string"])

        args = {
            "title": "%s" % keyword,
            "content": "%s" % keyword,
        }

        # validate pagination info
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        try:
            start = (page - 1) * per_page   # id in sql start at 1
            post_list = DBPost.search(search_dict=args, start=start, per_page=per_page, order_by="time desc")
            return post_list
        except:
            raise InvalidFieldError("Can not search with given string", ["search string"])

    @classmethod
    def find_post_by_keyword_pagination(cls, keyword, page=1, per_page=10):
        """
        Find all post publish by specific author

        :param category_name: category name
        :param page: page index begin at 1
        :param per_page:
        :return:
        """

        if not keyword:
            raise InvalidFieldError("category cannot be empty", ["search string"])

        args = {
            "title": "%s" % keyword,
            "content": "%s" % keyword,
        }

        # validate pagination info
        if not is_id_valid(page):
            page = 1
        else:
            page = int(page)

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        try:
            start = (page - 1) * per_page   # id in sql start at 1
            post_list = DBPost.pagination_search(search_dict=args, page=page, per_page=per_page, order_by="time desc")
            return post_list
        except Exception as e:
            raise InvalidFieldError("Can not search with given string", ["search string"])

    @classmethod
    def find_post_by_category(cls, category_name, page=1, per_page=10):
        """
        Find all post publish by specific author

        :param category_name: category name
        :param page: page index begin at 1
        :param per_page:
        :return:
        """

        if not category_name:
            raise InvalidFieldError("category cannot be empty", ["category"])
        cat_slug = get_slug_from_string(category_name)
        args = {"categories": "`%s`" % cat_slug}

        # validate pagination info
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        start = (page - 1) * per_page  # id in sql start at 1
        post_list = DBPost.search(search_dict=args, start=start, per_page=per_page, order_by="time desc")
        return post_list

    @classmethod
    def find_post_by_category_pagination(cls, category_name, page=1, per_page=10):
        """
        Find all post publish by specific author

        :param category_name: category name
        :param page: page index begin at 1
        :param per_page:
        :return:
        """

        if not category_name:
            raise InvalidFieldError("category cannot be empty", ["category"])
        cat_slug = get_slug_from_string(category_name)
        args = {"categories": "`%s`" % cat_slug}

        # validate pagination info
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        pagination = DBPost.pagination_search(search_dict=args, page=page, per_page=per_page, order_by="time desc")
        return pagination

    @classmethod
    def find_post_by_author(cls, author_id, page=1, per_page=10):
        """
        Find all post publish by specific author

        :param author_id: id of author to find post by
        :param page: page index begin at 1
        :param per_page:
        :return:
        """

        # valid user if
        if not is_id_valid(author_id):
            raise InvalidFieldError("author id does not valid.", ["author_id"])

        # confirm user existent
        author = DBUser.get_by_id(author_id)
        if not author:
            raise UserNotFoundError("User with id = %d does not exist")

        args = {"user_id": author_id}

        # validate pagination info
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        start = (page - 1) * per_page   # id in sql start at 1
        post_list = DBPost.get(filter_dict=args, start=start, per_page=per_page, order_by="time desc")
        return post_list, author

    @classmethod
    def find_post_by_author_pagination(cls, author_id, page=1, per_page=10):
        """
        Find all post publish by specific author

        :param author_id: id of author to find post by
        :param page: page index begin at 1
        :param per_page:
        :return:
        """

        # valid user if
        if not is_id_valid(author_id):
            raise InvalidFieldError("author id does not valid.", ["author_id"])

        # confirm user existent
        author = DBUser.get_by_id(author_id)
        if not author:
            raise UserNotFoundError("User with id = %d does not exist")

        args = {"user_id": author_id}

        # validate pagination info
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        pagination = DBPost.pagination_get(filter_dict=args, page=page, per_page=per_page, order_by="time desc")
        return pagination, author

    @classmethod
    def delete_post(cls, user_id, post_id):
        user = DBUser.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User with id = %d does not exist" % user_id)

        if not is_id_valid(post_id):
            raise InvalidFieldError("Post id is invalid", ["post_id"])

        post = DBPost.get_by_id(post_id)
        if not post:
            raise PostNotFoundError(post_id=post_id)

        # only allow author and manager to delete post
        if post.author.id != user_id and user.role != "manager":
            raise AccessDeniedError("You don't have permission to delete this post.")

        post.delete()
