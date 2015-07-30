__author__ = 'bluzky'
import unittest

from base import WbTescase
from controller.post import Post
from model.post import Post as DBPost
from lib.exceptions import InvalidFieldError

class TestAddPost(WbTescase):


    def test_add_post_with_all_valid_fields(self):
        args ={
            "user_id": 2,
            "title": "A night at Sai Gon",
            "content": "<p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>",
            "feature_image":"http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image1.jpg",
            "tags": "wallpaper, nature",
            "categories":"Uncategorized",
            "draft": True,
        }

        p = Post.add_post(**args)
        self.assertIsNotNone(p)

        post = DBPost.get_by_id(p.id)
        self.assertEqual(post.user_id, args["user_id"])
        self.assertEqual(post.title, args["title"])
        self.assertEqual(post.content, args["content"])
        self.assertEqual(post.feature_image, args["feature_image"])
        self.assertEqual(post.tags, args["tags"])
        self.assertEqual(post.categories, args["categories"])


    def test_add_post_without_title(self):
        args ={
            "user_id": 2,
            "title": "",
            "content": "<p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>",
            "feature_image":"http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image1.jpg",
            "tags": "wallpaper, nature",
            "categories":"Uncategorized",
            "draft": True,
        }

        p = Post.add_post(**args)
        self.assertIsNotNone(p)

        post = DBPost.get_by_id(p.id)
        self.assertEqual(post.user_id, args["user_id"])
        self.assertGreater(len(post.title), 0)
        self.assertEqual(post.content, args["content"])
        self.assertEqual(post.feature_image, args["feature_image"])
        self.assertEqual(post.tags, args["tags"])
        self.assertEqual(post.categories, args["categories"])

    def test_add_post_without_content(self):
        args = {
            "user_id": 2,
            "title": "Hello",
            "content": "",
        }

        try:
            Post.add_post(**args)
            self.fail("Expect InvalidFieldError")
        except InvalidFieldError:
            pass



if __name__ == '__main__':
    unittest.main()
