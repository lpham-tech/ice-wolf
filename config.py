# configuration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

TESTING = False
DEBUG = True
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
LOGIN_ENDPOINT = "/login"

#create application
app = Flask(__name__)
app.config.from_object( __name__)
db = SQLAlchemy(app)