__author__ = 'bluzky'
import uuid

from flask import request, redirect, render_template, session, abort, url_for
from config import app
from persistent import db
from controller import user_controller, login_manager
from controller import post_controller
from controller import comment_controller
from lib import utils
from flask_login import login_required, current_user
import default
import os
from settings import settings


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/index/<int:page>", methods=["GET", "POST"])
def homepage(page=1):
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

@app.route("/activation/verify/<token>", methods=["GET"])
def activate(token):
    if settings.require_activation:
        return user_controller.activate_account(token)
    else:
        abort(404)


@app.route("/activation/generate", methods=["GET", "POST"])
def generate_activation_token():
    if settings.require_activation:
        if request.method == 'GET':
            # generate for existing user, in case expired link
            return user_controller.generate_activation_code()
        else:
            # generate for user in case bad link
            if request.form["email"]:
                return user_controller.generate_activation_code_for_email(request.form["email"])
            else:
                abort(400)
    else:
        abort(404)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        try:
            if current_user.is_authenticated():
                if request.args["next"]:
                    return redirect(request.args["next"])
                else:
                    return redirect("/")
            else:
                return render_template("login.html")
        except Exception as e:
            return render_template("login.html")
    elif request.method == 'POST':
        return user_controller.login()


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == 'GET':
        try:
            if current_user.is_authenticated():
                return redirect("/")
            else:
                return render_template("reset_password.html")
        except Exception as e:
            return render_template("reset_password.html")
    elif request.method == 'POST':
        return user_controller.send_reset_password_email()

@app.route("/reset_password/<token>", methods=["GET"])
def reset_password(token):
    return user_controller.login_by_token(token)

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password(token = None):
    if request.method == 'GET':
        return render_template("change_password.html")
    else:
        return user_controller.update_password()


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile_handler():
    if request.method == "GET":
        if request.args and request.args["action"] == "edit":
            return render_template("profile.html", edit=True)
        else:
            return render_template("profile.html")
    else:
        if "update" in request.form:
            return user_controller.update_profile()
        else:
            return render_template("profile.html")



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

# ERROR HANDLER
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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
app.jinja_env.globals['has_readmore_tag'] = utils.has_readmore_tag
app.jinja_env.globals['get_to_readmore'] = utils.get_to_readmore

if __name__ == "__main__":
    db.init_app(app)
    #login_manager.init_app(app)
    if app.config["DEBUG"]:
        app.run()
    else:
        port = int(os.environ.get('PORT', 80))
        app.run(host='0.0.0.0', port=port)
