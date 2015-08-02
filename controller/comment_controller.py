__author__ = 'bluzky'
from flask import session, request, abort, redirect
from business.comment import Comment

def add_comment():
    args = {
        "post_id":request.form["post_id"] or None,
        "user_id": session["user"]["id"],
        "content": request.form["comment"] or None
    }

    try:
        Comment.add_comment(**args)
        if request.form["next"]:
            return redirect(request.form["next"])
        else:
            return redirect("/")
    except:
        abort(400)

