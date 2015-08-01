__author__ = 'bluzky'
from flask import request, redirect, url_for, render_template
from config import app
from persistent import db
from controller import user_controller

@app.route("/")
def homepage_handler():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register_handler():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        return user_controller.register_user()


@app.route("/login", methods=["GET", "POST"])
def login_handler():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        return "OK"


@app.route("/login", methods=["GET"])
def logout_handler():
    # clean session
    return redirect(url_for('/'))


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("single_post.html")


@app.route("/newpost", methods=["GET", "POST"])
def add_post_handler():
    if request.method == 'GET':
        return render_template("add_post.html")
    elif request.method == 'POST':
        # do add post
        return "OK"


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post_handler(post_id):
    if request.method == 'GET':
        return render_template("add_post.html")
    elif request.method == 'POST':
        # do add post
        return "OK"


@app.route("/add_comment", methods=["POST"])
def add_comment_handler():
    return "OK"


@app.route("/category/<cat_slug>", methods=["GET"])
def search_by_category_handler(cat_slug):
    return "OK"


@app.route("/tag/<tag_slug>", methods=["GET"])
def search_by_tag_handler(tag_slug):
    return "OK"

@app.before_first_request
def initialize_database():
    db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    app.run()
