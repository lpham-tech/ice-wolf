# configuration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

#create application
app = Flask(__name__)
app.config.from_object( __name__)
db = SQLAlchemy(app)