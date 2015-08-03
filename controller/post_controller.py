__author__ = 'bluzky'
from flask import abort, render_template, request, session, redirect, url_for
from business.post import Post
from lib.exceptions import AccessDeniedError
import default

PER_PAGE = 10

def get_latest_post(page):
    try:
        pagination = Post.get_posts_pagination(page=page, per_page=PER_PAGE)
        return render_template("index.html", pagination=pagination, menu_items=default.categories)
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

def edit_post(post_id):
    try:
        post = Post.get_post(post_id)
        #only author can edit post
        if post.author.id != session["user"]["id"] and session["user"]["role"] != "manager":
            abort(403)
        return render_template("add_post.html", post=post, categories=default.categories)
    except Exception as e:
        abort(404)

def update_post():
    args={
            "user_id": session["user"]["id"],
            "post_id": request.form["post_id"] or None,
            "title":request.form["title"] or None,
            "content": request.form["content"] or None,
            "categories": request.form.getlist("categories") or None,
            "tags": request.form["tags"] or None,
            "feature_image":request.form["feature_image"] or None,
        }
    try:
        post = Post.update_post(**args)
        return render_template("add_post.html", post=post, categories=default.categories)
    except AccessDeniedError:
        abort(403)
    except Exception as e:
        abort(400)

def search_post_by_keyword():
    keyword = request.args["keyword"] or None
    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", PER_PAGE)

    try:
        pagination = Post.find_post_by_keyword_pagination(keyword, page, per_page)
        return render_template("search_result.html", pagination=pagination, keyword=keyword, menu_items=default.categories)
    except Exception as e:
        abort(400)

def filter_post_by_category(cat_name, page):
    try:
        pagination = Post.find_post_by_category_pagination(cat_name, page)
        return render_template("search_result.html", pagination=pagination, category=cat_name, menu_items=default.categories)
    except Exception as e:
        abort(400)

def filter_by_user(user_id, page):
    try:
        pagination, author = Post.find_post_by_author_pagination(user_id,page)
        return render_template("search_result.html", pagination=pagination, author=author, menu_items=default.categories)
    except Exception as e:
        abort(400)