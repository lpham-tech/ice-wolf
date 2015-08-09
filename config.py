# configuration

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import os

TESTING = False
DEBUG = True
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
LOGIN_ENDPOINT = "/login"

# # email server
# MAIL_SERVER = 'your mail host' #'smtp.googlemail.com'
# MAIL_PORT = 587 # your mail port on server
# MAIL_USE_TLS = True # using TLS ?
# MAIL_USE_SSL = False # using SSL ?
# MAIL_USERNAME = 'your user name'#os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = "your password"#os.environ.get('MAIL_PASSWORD')
#
# # administrator list
# ADMINS = ['abc@example.com']

__author__ = 'bluzky'
# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "icewolf.blog@gmail.com"#os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = "thisiswolf"#os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['icewolf.blog@gmail.com']


#create application
app = Flask(__name__)
app.config.from_object( __name__)
db = SQLAlchemy(app)
mail = Mail(app)