__author__ = 'bluzky'
from lib.mail_utils import send_mail
from lib import utils
from flask import render_template, request, url_for
import default
from config import ADMINS

def send_activation_mail(user):
    try:
        args = dict()
        args["subject"] = "[%s] %s" %(default.APPLICATION_NAME, default.ACTIVATION_MAIL_SUBJECT)
        args["sender"] = ADMINS[0]
        args["recipients"] = [user.email]
        activation_link = request.host_url + 'activate/verify/' + utils.generate_activation_token(user.email, user.activation_id)
        args["text_body"] = render_template("mail_templates/activation_email.txt", user=user, application=default.APPLICATION_NAME, activation_url=activation_link)
        args["html_body"] = render_template("mail_templates/activation_email.html", user=user, application=default.APPLICATION_NAME, activation_url=activation_link)
        send_mail(**args)
    except Exception as e:
        print e.message
        #TODO: log or doing something here