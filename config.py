# configuration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

TESTING = False
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
LOGIN_ENDPOINT = "/login"

#create application
app = Flask(__name__)
app.config.from_object( __name__)
db = SQLAlchemy(app)