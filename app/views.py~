from app import app, socketio
from flask import render_template, redirect, jsonify, request, session, abort, Markup
from . import mailing
from . import forms
from . import userDAO
from .decorators import requireLoginLevel
import logging.config
import traceback
from .functions import get_db
from .blueprint_static import static_B
from .blueprint_users import users_B
from .blueprint_chan import chan_B
from .sessions import MongoSessionInterface
from flask_socketio import SocketIO, emit

app.session_interface = MongoSessionInterface()


logging.config.fileConfig(app.config['LOG_CONFIG_FILE'])
logr = logging.getLogger('mizzychan.views')

app.register_blueprint(static_B)
app.register_blueprint(users_B)
app.register_blueprint(chan_B)

#LSO = SessionObject.SessionObject()

#log.basicConfig(filename='example.log',level=log.DEBUG, format="[%(levelname)s] : %(message)s")
@app.context_processor
def inject_vars():

    pageVars = {'conf':app.config}
    pageVars['banner'] = "GimpHub"

    if 'level' in session:

            pageVars['aws'] = session['aws']
            pageVars['user'] = session['user']
            pageVars['fname'] = session['fname']
            pageVars['lname'] = session['lname']
            pageVars['level'] = session['level']
            pageVars['loginForm'] = None

    else:
        pageVars['user'] = False
        # pageVars['loginForm'] = forms.loginForm()
        # pageVars['loginForm'].wantsurl.data = request.path

    return pageVars

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

@app.route('/index', methods = ['GET'])
@app.route('/', methods = ['GET'])
def index():

    db = get_db()


    return render_template('index.html')

@app.route('/trending', methods = ['GET'])
def trending():
    return render_template('trending.html')

@app.route('/categories', methods = ['GET'])
def categories():
    return render_template('categories.html')

@app.route('/info', methods = ['GET'])
def info():
    return render_template('info.html')

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template('contact.html')

@app.errorhandler(405)
def errpage_405(e):    
    logr.debug("==================405, REDIRECTED====================")
    return redirect('/') #temporary solution because I dont know how to get methods from url_for 
 
@app.errorhandler(404)
def errpage_404(e):    
    return render_template('error.html', error = {'type':404,'title':"404"})

@app.errorhandler(403)
def errpage_403(e):    
    return render_template('error.html', error = {'type':403,'title':"403"})

@app.errorhandler(410)
def errpage_410(e):    
    return render_template('error.html', error = {'type':410,'title':"410"})

@app.errorhandler(500)
def errpage_500(e):
    tb = traceback.format_exc()
    print(tb)
    return render_template('error.html', error = {'type':500,'title':"500"})
