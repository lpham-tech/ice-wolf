__author__ = 'bluzky'
from persistent.post import Post
from persistent.user import User
from persistent.comment import Comment
import hashlib
def set_up_db():
    args = {
        "email": "admin@gmail.com",
        "password": hashlib.md5("123456").hexdigest(),
        "first_name": "Admin",
        "last_name": "Nguyen",
        "brief": "Hello world",
        "role": "manager"
    }
    user = User(**args)
    user.save()

    args["email"] = "editor2@gmail.com"
    args["first_name"] = "Editor2"
    args["role"] = 'editor'
    user = User(**args)
    user.save()

    args["email"] = "editor3@gmail.com"
    args["first_name"] = "Editor3"
    user = User(**args)
    user.save()

    args["email"] = "editor4@gmail.com"
    args["first_name"] = "Editor4"
    user = User(**args)
    user.save()

    args = {
        "title": "Post 1 title",
        "content": """<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
        <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
        <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
        <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>""",
        "user_id": 1,
        "categories":"`c++`,`python`"
    }

    post = Post(**args)
    post.save()

    args["title"] = "Post 2 title"
    args["user_id"] = 2

    post = Post(**args)
    post.save()

    args["title"] = "Post 3 title"
    args["user_id"] = 3

    post = Post(**args)
    post.save()

    args["title"] = "Post 4 title"
    args["user_id"] = 4

    post = Post(**args)
    post.save()

    args["title"] = "Post Hello title"
    args["user_id"] = 1
    args["categories"] = "`non-it`"

    post = Post(**args)
    post.save()

    args["title"] = "Good morning"
    args["user_id"] = 2

    post = Post(**args)
    post.save()

    args["title"] = "First day at Moscow"
    args["user_id"] = 2
    args["categories"] = "`journey`, `non-it`"

    post = Post(**args)
    post.save()

    args["title"] = "Surprising"
    args["user_id"] = 3

    post = Post(**args)
    post.save()

    args["title"] = "So awesome lake"
    args["user_id"] = 3

    post = Post(**args)
    post.save()

    args["title"] = "My new Phone"
    args["user_id"] = 3
    args["categories"] = "`photo`, `non-it`"

    post = Post(**args)
    post.save()

    args["title"] = "Photo with new phone"
    args["user_id"] = 3

    post = Post(**args)
    post.save()

    args["title"] = "List of useful app for Blackberry"
    args["user_id"] = 3
    args["categories"] = "`uncategorized`"

    post = Post(**args)
    post.save()


    cmt_args={
        "content":"<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>",
        "post_id":1,
        "user_id":2,
    }
    cmt = Comment(**cmt_args)
    cmt.save()


    cmt_args["post_id"] = 1
    cmt_args["user_id"] = 3
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 1
    cmt_args["user_id"] = 4
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 3
    cmt_args["user_id"] = 4
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 3
    cmt_args["user_id"] = 2
    cmt = Comment(**cmt_args)
    cmt.save()
    cmt_args["post_id"] = 4
    cmt_args["user_id"] = 1
    cmt = Comment(**cmt_args)
    cmt.save()
    cmt_args["post_id"] = 7
    cmt_args["user_id"] = 1
    cmt = Comment(**cmt_args)
    cmt.save()
    cmt_args["post_id"] = 4
    cmt_args["user_id"] = 2
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 3
    cmt_args["user_id"] = 3
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 2
    cmt_args["user_id"] = 4
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 2
    cmt_args["user_id"] = 1
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 2
    cmt_args["user_id"] = 3
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 2
    cmt_args["user_id"] = 4
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 5
    cmt_args["user_id"] = 3
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 5
    cmt_args["user_id"] = 2
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 5
    cmt_args["user_id"] = 3
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 5
    cmt_args["user_id"] = 4
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 6
    cmt_args["user_id"] = 4
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 6
    cmt_args["user_id"] = 1
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 9
    cmt_args["user_id"] = 1
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 9
    cmt_args["user_id"] = 1
    cmt = Comment(**cmt_args)
    cmt.save()

    cmt_args["post_id"] = 9
    cmt_args["user_id"] = 3
    cmt = Comment(**cmt_args)
    cmt.save()