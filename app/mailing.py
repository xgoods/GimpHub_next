from app import app, mail

from flask_mail import Message
from flask import url_for
from threading import Thread

from .functions import get_db_proc

def send_async_email(msg):
    with app.app_context():
        mail.send(msg)

def send_test_mail(emailAddress):
    print("sending")
    subject = "subject"
    sender = "sender"
    mail_to_be_sent = Message(subject=subject, sender = sender, recipients=[emailAddress])
    mail_to_be_sent.html = "A test Email"
    thr = Thread(target = send_async_email, args = [mail_to_be_sent])
    thr.start()
        
    
