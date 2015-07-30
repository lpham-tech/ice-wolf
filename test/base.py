__author__ = 'bluzky'
from unittest import TestCase
from config import db
import setup_testdb
from model.user import User
from model.post import Post
from model.comment import Comment

class WbTescase(TestCase):
    @classmethod
    def setUpClass(cls):
        db.drop_all()
        db.create_all()
        setup_testdb.set_up_db()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
