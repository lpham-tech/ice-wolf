__author__ = 'bluzky'
from config import db
from base import ModelMethods

class User(db.Model, ModelMethods):
    _table_name = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    avatar = db.Column(db.String(512), default="")
    brief = db.Column(db.String(1024), default="")
    role = db.Column(db.String(20), default="editor")
    activated =db.Column(db.Boolean, default=True)

    # activation_id is used for activating account and reset password
    activation_id = db.Column(db.String(64))

    posts = db.relationship('Post', backref=db.backref('user', lazy='select'), lazy='dynamic')
    comments = db.relationship('Comment', backref=db.backref('user', lazy='select'), lazy='dynamic')

    def __init__(self, email, password, first_name, last_name, avatar=None, brief=None, role=None):
        #self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        if avatar:
            self.avatar = avatar
        if brief:
            self.brief = brief

        if role:
            self.role = role


    def __repr__(self):
        return "User: %s %s" % (self.first_name, self.last_name)