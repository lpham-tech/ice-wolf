__author__ = 'bluzky'
from config import db
from model.user import User
from model.post import Post
from model.comment import Comment

def init():
    db.create_all()

def test_insert():
    user1 = User("dzung", "blue@gmail.com", "Dzung", "Nguyen")
    db.session.add(user1)
    try:
        db.session.commit()
        print "Insert successfully"
    except:
        print "Insert: Failed"

def test_query():
    users = User.query.all()
    print users

def test_filter():
    users = User.query.filter_by(email="blue@gmail.com").first()
    print users

    # multiple filter criteria
    users = User.query.filter_by(username="dzung", email="blue@gmail.com").first()
    print users

init()
#test_insert()
test_query()
test_filter()