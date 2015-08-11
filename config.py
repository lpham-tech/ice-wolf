# configuration

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flaskext.uploads import (UploadSet, configure_uploads, IMAGES)
import os

TESTING = False
DEBUG = True
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
LOGIN_ENDPOINT = "/login"

DEFAULT_FILE_STORAGE = 'filesystem'
UPLOADED_PHOTOS_DEST = os.path.realpath('.') + '/static/upload'
UPLOADED_FILES_DEST = os.path.realpath('.') + '/static/upload'
ALLOWED_EXTENSIONS = ('txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif')

# email server
MAIL_SERVER = 'your mail host' #'smtp.googlemail.com'
MAIL_PORT = 587 # your mail port on server
MAIL_USE_TLS = True # using TLS ?
MAIL_USE_SSL = False # using SSL ?
MAIL_USERNAME = 'your user name'#os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = "your password"#os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['abc@example.com']


#create application
app = Flask(__name__)
app.config.from_object( __name__)
db = SQLAlchemy(app)
mail = Mail(app)

# uploads
avatars = UploadSet('photos', IMAGES)
configure_uploads(app, avatars)