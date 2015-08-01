__author__ = 'bluzky'
from unittest import TestCase
from config import db
import time
import setup_testdb
from persistent.user import User
from persistent.post import Post
from persistent.comment import Comment

class WbTescase(TestCase):
    @classmethod
    def setUpClass(cls):
        db.drop_all()
        db.create_all()
        setup_testdb.set_up_db()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        db.drop_all()
