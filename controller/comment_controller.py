__author__ = 'bluzky'
from flask import session, request, abort, redirect
from business.comment import Comment
from flask_login import current_user

def add_comment():
    args = {
        "post_id":request.form["post_id"] or None,
        "user_id": current_user.id,
        "content": request.form["comment"] or None
    }

    try:
        Comment.add_comment(**args)
        if request.form["next"]:
            return redirect(request.form["next"])
        else:
            return redirect("/")
    except Exception as e:
        abort(400)

def delete_comment(comment_id):
    try:
        args = {
            "user_id" : current_user.id,
            "comment_id": comment_id
        }
        Comment.delete_comment(**args)
        return redirect(request.referrer)
    except Exception as e:
        abort(400)

