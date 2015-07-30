__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from model.post import Post as DBPost
from lib.exceptions import InvalidFieldError, AccessDeniedError, PostNotFoundError, UserNotFoundError

class TestUpdatePost(WbTescase):


    def test_update_post_with_all_valid_fields(self):
        args ={
            "user_id": 1,
            "post_id": 1,
            "title": "A night at Sai Gon",
            "content": "<p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>",
            "feature_image":"http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image1.jpg",
            "tags": "wallpaper, nature",
            "categories":"Uncategorized",
            "draft": True,
        }

        Post.update_post(**args)
        post = DBPost.get_by_id(1)
        self.assertEqual(post.user_id, args["user_id"])
        self.assertEqual(post.title, args["title"])
        self.assertEqual(post.content, args["content"])
        self.assertEqual(post.feature_image, args["feature_image"])
        self.assertEqual(post.tags, args["tags"])
        self.assertEqual(post.categories, args["categories"])


    def test_update_post_by_manager(self):
        args ={
            "user_id": 1,
            "post_id": 2,
            "title": "A night at Sai Gon",
            "content": "<p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>",
        }

        Post.update_post(**args)
        post = DBPost.get_by_id(2)
        self.assertNotEqual(post.user_id, args["user_id"])
        self.assertEqual(post.title, args["title"])
        self.assertEqual(post.content, args["content"])


    def test_update_post_without_permission(self):
        args ={
            "user_id": 2,
            "post_id": 3,
            "title": "A night at Sai Gon",
            "content": "<p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>",
        }

        try:
            Post.update_post(**args)
            self.fail('Expect AccessDeniedError')
        except AccessDeniedError:
            pass

    def test_update_post_not_exist(self):
        args ={
            "user_id": 2,
            "post_id": 100,
            "title": "A night at Sai Gon",
            "content": "<p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>",
        }

        try:
            Post.update_post(**args)
            self.fail('Expect PostNotFoundError')
        except PostNotFoundError:
            pass

    def test_update_post_no_content(self):
        args ={
            "user_id": 2,
            "post_id": 2,
            "title": "A night at Sai Gon",
            "content": "",
        }

        try:
            Post.update_post(**args)
            self.fail('Expect InvalidFieldError')
        except InvalidFieldError:
            pass


if __name__ == '__main__':
    unittest.main()
