__author__ = 'bluzky'
from config import db
from datetime import  datetime

class Comment(db.Model):
    _table_name = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    time = db.Column(db.DateTime())
    approved = db.Column(db.Boolean(), default=False)

    def __init__(self, content, post_id, user_id, comment_time = None, approved=False):
        self.content = content
        self.post_id = post_id
        self.user_id = user_id

        if comment_time:
            self.time = comment_time
        else:
            self.time = datetime.now()

        self.approved = approved


    def __repr__(self):
        return "Comment: %s ..." % self.content[:50]