from flask import Blueprint, render_template
import logging

logr = logging.getLogger('gimphub.blueprint_static')

static_B = Blueprint('static', __name__)

@static_B.route('/terms', methods = ['GET'])
def terms():
    
    return render_template('terms.html')

@static_B.route('/privacy', methods = ['GET'])
def privacy():
    
    return render_template('privacy.html')

@static_B.route('/licenses', methods = ['GET'])
def licenses():
    
    return render_template('licenses.html')

@static_B.route('/registercomplete', methods = ['GET', 'POST'])
def registercomplete():    
    
    return render_template('registercomplete.html')