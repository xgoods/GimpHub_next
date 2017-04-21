import gevent.monkey
gevent.monkey.patch_all()

from flask import Flask
from flask_mail import Mail
from flask_socketio import SocketIO
import os

app = Flask(__name__)

app.config.from_pyfile('../config.py')

initPath = os.path.dirname(os.path.realpath(__file__))

app.config.update()

mail=Mail(app)

#getattr(client, authenticationDatabase)

socketio = SocketIO(app, async_mode='gevent')

from app import views



