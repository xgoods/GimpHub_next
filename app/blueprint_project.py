from app import app, socketio
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, abort, jsonify
from flask_socketio import emit, join_room, leave_room
from . import mailing
from . import forms
from . import userDAO
from .decorators import requireLoginLevel
from .functions import get_db
import logging
import string, random
import requests
from .crawl import getArticle
import datetime, calendar, time
logr = logging.getLogger('gimphub.blueprint_chan')
project_B = Blueprint('project', __name__)


@project_B.route('/project/<project>', methods = ['GET'])
def project(project):
    #room=request.args['room'] if 'room' in request.args else None

    return render_template('project.html', project=project)

@project_B.route('/changeUserName', methods = ['POST', 'GET'])
def changeUserName():
    if all(x in request.form for x in ('g-recaptcha-response', 'userNameChange')):

        dictToSend = {'secret': '6Ldw_wkUAAAAAJFyh_Pmg1KKyM_1ta4Rwg3smpEY',
                      'response': request.form['g-recaptcha-response']}
        res = requests.get('https://www.google.com/recaptcha/api/siteverify',
                           params=dictToSend,
                           verify=True)
        if res.json()['success']:

            return jsonify({'ok': 1})
        else:
            return jsonify({'ok': 0})
    else:
        return jsonify({'ok': 0})

labels={
            'US_News': 'US News',
            'World_News':'World News',
            'Politics':'Politics',

            'Technology':'Technology',
            'Entertainment':'Entertainment',
            'Business':'Business',

            'Sports':'Sports',

            'Memes':'Memes'}

@project_B.route('/categories/<category>', methods = ['GET'])
def categories(category):

    name = labels[category]



    # getting the time until switch
    interval = app.config['SWITCH_SECONDS']

    current_time = calendar.timegm(time.gmtime())
    remainingTime = interval - (current_time % interval)
    print(remainingTime)




    return render_template('categories.html', categoryName=name,
                           category=category,
                           remainingTime=remainingTime,
                           interval=interval)

@project_B.route('/testArticles', methods = ['GET'])
def testArticles():

    db = get_db()
    for i in range(30):

        db.articles.insert({'url':'http://stackoverflow.com/questions/%d' % (5584586+i),
                            'title':'test%d' % (5584586+i),
                            'category':'Technology'})

    return "OK"

@project_B.route('/getCurrentArticle', methods = ['POST'])
def getCurrentArticle():
    if not 'category' in request.json:
        return jsonify({'ok':0, 'err':'Must provide category'})

    interval = app.config['SWITCH_SECONDS']

    current_time = calendar.timegm(time.gmtime())
    intervals_passed = current_time // interval

    db = get_db()
    article = db.articles.find({'category': request.json['category']}).sort([('$natural',1)]).limit(1)
    if not article.count():
        return jsonify({'ok': 0, 'err': 'no articles!'})
    article = article[0]
    #print article

    if 'index' not in article:
        db.articles.update({'_id': article['_id']}, {'$set': {'index': intervals_passed}})

    elif 'index' in article and intervals_passed > article['index']:
        db.articles.remove({'_id':article['_id']})
        article = db.articles.find({'category': request.json['category']}).sort([('$natural',1)]).limit(1)
        if not article.count():
            return jsonify({'ok': 0, 'err': 'no articles!'})
        article = article[0]
        db.articles.update({'_id': article['_id']}, {'$set': {'index': intervals_passed}})

    del article['_id']
    return jsonify({'ok':1, 'article':article})

@project_B.route('/upload', methods = ['POST'])
def upload():
    if not 'category' in request.json or not 'url' in request.json or not 'title' in request.json:
        return jsonify({'ok':0, 'err':'Must provide category'})

    category = request.json['category']
    url = request.json['url']
    title = request.json['title']
    if category and url and title:
        article = {'url':url,
                   'title':title,
                   'category':category}
        try:
            if 'title' not in article or not article['title'] or article['title'].isspace():
                article['title'] = getArticle.get_generic_title(article['url'])
        except:
            pass
        try:
            article['content'] = getArticle.get_generic_article(article['url'])
        except:
            pass
        try:
            article['img'] = getArticle.get_generic_image(article['url'])
        except:
            pass
        db = get_db()
        print(article)
        try:
            db.articles.insert(article)
        except Exception as e:
            print("unknown error: %s" % str(e))

    return jsonify({'ok':1})


@socketio.on('connect', namespace='/chat')
def connect2():
    # join_room(session['user'])
    # room = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))

    emit('connectConfirm')

# 'disconnected' is a special event
@socketio.on('disconnect')
def disconnected():
    pass

@socketio.on('userDisconnect', namespace='/chat')
def userDisconnect(user, room):
    #db = get_db()
    #db.msgs.insert({'room':room, 'user':user, 'left':True, 'time':tStamp})

    leave_room(room)
    emit('userDisconnect', {'ok': 1, 'user':user, 'room':room}, room=room)


@socketio.on('joined', namespace='/chat')
def joined(user, room):
    join_room(room)
    #at some point, twisted will be implemented instead of this
    #loggedIn.addUser(user)
    #print loggedIn.getUsers()
    #db = get_db()
    #db.msgs.insert({'room':room, 'user':user, 'joined':True, 'time':tStamp})

    print('user joined')
    emit('joined', {'ok': 1, 'user': user, 'room':room}, room=room)


# @socketio.on('checkUsersOnlineInit', namespace='/chat')
# def checkUsersOnlineInit():
#     emit('checkUsersOnlineInit', {}, broadcast=True)
#
# @socketio.on('checkUsersOnlineConfirm', namespace='/chat')
# def checkUsersOnlineConfirm(user, status):
#     db = get_db()
#     #cur = [msg for msg in db.msgs.find({'room':status, 'msg':{'$exists':True}},{'_id':0}).sort([('$natural',-1)]).limit(20)]
#     cur = []
#     emit('checkUsersOnlineConfirm', {'msgs':cur, 'user':user, 'room':status}, room=room)

@socketio.on('chatMsg', namespace='/chat')
def chatMsg(user, room, data):


    # #msgs.insert({'post':message})
    # if message != 'connected':
    #
    #     msgsCol.insert({'user':message['user'], 'msg':message['post']})
    #
    #     emit('update', message, broadcast=True)
    #db = get_db()
    #db.msgs.insert({'room':room, 'user':user, 'msg':data})
    emit('chatMsg', {'user':user, 'data':data, 'room':room}, room=room)
