__author__ = 'bluzky'
from flask import abort, render_template
from business.post import Post

PER_PAGE = 10

def get_latest_post(page):
    try:
        pagination = Post.get_posts_pagination(page=page, per_page=PER_PAGE)
        return render_template("index.html", pagination=pagination)
    except Exception as e:
        #temporary return 404
        #TODO: render 404 page
        abort(404)
