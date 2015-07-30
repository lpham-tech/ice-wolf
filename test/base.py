__author__ = 'bluzky'
from unittest import TestCase
from config import db
from model.user import User
from model.post import Post
from model.comment import Comment

class WbTescase(TestCase):
    @classmethod
    def setUpClass(cls):
        db.drop_all()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
