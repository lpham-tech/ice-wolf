__author__ = 'bluzky'
from flask import request, redirect, url_for, render_template, session, abort
from config import app
from persistent import db
from controller import user_controller
from controller import post_controller
from controller import comment_controller
#from lib import login_required
from flask_login import login_required
import default
import uuid


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/index/<int:page>", methods=["GET", "POST"])
def homepage(page = 1):
    return post_controller.get_latest_post(page=page)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        if "logged_in" in session:
            if request.args["next"]:
                return redirect(request.args["next"])
            else:
                return redirect("/")
        else:
            return render_template("register.html")
    elif request.method == 'POST':
        return user_controller.register_user()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        if "logged_in" in session:
            if request.args["next"]:
                return redirect(request.args["next"])
            else:
                return redirect("/")
        else:
            return render_template("login.html")
    elif request.method == 'POST':
        return user_controller.login()


@app.route("/logout", methods=["GET"])
def logout():
    return user_controller.logout()


@app.route("/post/<int:post_id>")
def post(post_id):
    return post_controller.show_single_post(post_id)


@app.route("/publish", methods=["GET", "POST"])
@login_required
def add_post():
    if request.method == 'GET':
        return render_template("add_post.html", categories=default.categories)
    elif request.method == 'POST':
        return post_controller.add_post()


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit(post_id):
    if request.method == 'GET':
        return post_controller.edit_post(post_id)
    elif request.method == 'POST':
        return post_controller.update_post()

@app.route("/comment", methods=["POST"])
@login_required
def comment():
    return comment_controller.add_comment()

@app.route("/category/<category>", methods=["GET"])
@app.route("/category/<category>/<int:page>", methods=["GET"])
def category(category, page=1):
    return post_controller.filter_post_by_category(category, page)

@app.route("/author/<int:author_id>", methods=["GET"])
@app.route("/author/<int:author_id>/<int:page>", methods=["GET"])
def author(author_id, page=1):
    return post_controller.filter_by_user(author_id, page)

@app.route("/tag/<tag_slug>", methods=["GET"])
def search_by_tag_handler(tag_slug):
    return "OK"

@app.route("/search", methods=["GET"])
def search():
    return post_controller.search_post_by_keyword()

@app.before_first_request
def initialize_database():
    db.create_all()

# CSRF protection
@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

if __name__ == "__main__":
    db.init_app(app)
    user_controller.login_manager.init_app(app)
    app.run()
