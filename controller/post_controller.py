__author__ = 'bluzky'
from flask import abort, render_template, request, session, redirect, url_for
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

def show_single_post(post_id):
    try:
        post = Post.get_post(post_id)
        if post:
            return render_template("single_post.html", post=post)
        else:
            abort(404)
    except Exception as e:
        #TODO: render 404 page
        abort(404)

def add_post():
    try:
        args={
            "user_id": session["user"]["id"],
            "title":request.form["title"] or None,
            "content": request.form["content"] or None,
            "categories": request.form.getlist("categories") or None,
            "tags": request.form["tags"] or None,
            "feature_image":request.form["feature_image"] or None,
        }
        post = Post.add_post(**args)

        return redirect(url_for('post', post_id=post.id))
    except:
        abort(400)