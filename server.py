__author__ = 'bluzky'
from flask import request, redirect, url_for, render_template, session, abort
from config import app
from persistent import db
from controller import user_controller
from controller import post_controller
import uuid


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/index/<int:page>", methods=["GET", "POST"])
def homepage(page = 1):
    return post_controller.get_latest_post(page=page)


@app.route("/register", methods=["GET", "POST"])
def register_handler():
    if request.method == 'GET':
        if "logged_in" in session:
            return redirect("/")
        else:
            return render_template("register.html")
    elif request.method == 'POST':
        return user_controller.register_user()


@app.route("/login", methods=["GET", "POST"])
def login_handler():
    if request.method == 'GET':
        if "logged_in" in session:
            return redirect("/")
        else:
            return render_template("login.html")
    elif request.method == 'POST':
        return user_controller.login()


@app.route("/logout", methods=["GET"])
def logout_handler():
    session.pop("user", None)
    session.pop("logged_in", None)
    return redirect("/")


@app.route("/post/<int:post_id>")
def post(post_id):
    return post_controller.show_single_post(post_id)


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


@app.route("/category/<name>", methods=["GET"])
def category(name):
    return "OK"


@app.route("/tag/<tag_slug>", methods=["GET"])
def search_by_tag_handler(tag_slug):
    return "OK"

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
    app.run()
