#!flask/bin/python
from app import app
from app import socketio

#print "5"
#app.debug=True
socketio.run(app)
