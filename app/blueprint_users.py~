from app import app, socketio
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, abort, jsonify
from . import mailing
from . import forms
from . import userDAO
from .decorators import requireLoginLevel
from .functions import get_db
import logging

logr = logging.getLogger('.blueprint_users')
users_B = Blueprint('users', __name__)


@users_B.route('/login', methods = ['GET'])
def login():
    return render_template("login.html")

@users_B.route('/', methods = ['GET'])
def home():
    return render_template("index.html")

@users_B.route('/userpage', methods = ['GET'])
def user():
    return render_template("userpage.html")

@users_B.route('/user/<user>', methods = ['GET'])
def userpage(user):

    db = get_db()
    exists = db.users.find_one({'username':user})
    if not exists:
        flash("Error, user %s does not exist" % user, "warning")
        return render_template("index.html")


    return render_template("userpage.html", user=user,dateCreated = exists.get('dateCreated', "1994"))

    


@users_B.route('/userlist', methods = ['GET'])
def userlist():

    db = get_db()
    userlist = db.users.find({})


    return '<br>'.join([x['_id'] for x in userlist])







@users_B.route('/verifylogin', methods = ['POST'])
def verifylogin():

    loginForm = request.form



    #print(registerForm['emailreg'])

    if all(x in loginForm for x in ('emaillogin', 'passwordLogin')):


        db = get_db()


        userSecurity = userDAO.userDAO(db)
        user = userSecurity.validate_login(loginForm['emaillogin'],loginForm['passwordLogin'])

        if user not in [None, False]:
            session['level'] = user['level']
            session['user'] = user['_id']
            # session['fname'] = user['firstName']
            # session['lname'] = user['lastName']

            if 'wantsurl' in request.form:
                return redirect(request.form['wantsurl'])
            else:
                return redirect('/')
        #
        # if user == False:
        #     body = """<p>Sorry, this username is currently locked out. You must contact the system administrator to unlock it</p>"""
        #     header = "Login Error"
        #     return render_template("completepage.html", header = header, body = body, loginForm = loginForm)

    body = """<p>Sorry, this username / password combination was not found in the database</p>"""

    header = "Login Error"

    return render_template("userpage.html", header = header, body = body, loginForm = loginForm)


# # actually processes the password reset
# @users_B.route('/forgotPassword', methods=['POST'])
# @disableLDAP
# def forgotPassword():
#     forgotPasswordForm = frequest.form
#
#     if forgotPasswordForm.validate_on_submit():
#
#         db = get_db()
#         user = db.users.find_one({'_id': forgotPasswordForm.userName.data})
#         if (user == None):
#             statusMessage = {'heading': 'Failure', 'body': 'Sorry, that user name is not registered on our website.'}
#             return render_template('forgotlogininfo.html', statusMessage=statusMessage)
#         else:
#             userSecurity = userDAO.userDAO(db)
#             unhashedPassword = userSecurity.reset_password(user['_id'])
#
#
#             statusMessage = {'heading': 'Success',
#                              'body': 'The new password was sent successfully to your email address.'}
#             return render_template('forgotlogininfo.html', statusMessage=statusMessage)
#
#     return render_template('forgotlogininfo.html', forgotPasswordForm=forgotPasswordForm)

@users_B.route('/verifyregister', methods=['POST', 'GET'])
def verifyregister():
    registerForm = request.form


    print(registerForm['emailreg'])

    if all(x in registerForm for x in ('emailreg', 'password', 'passwordreg')):
        print("asd3")
        db = get_db()
        print (db.users.find({'_id': registerForm['emailreg']}).count() != 0)
        print("asd4")

        if (registerForm['passwordreg'] != registerForm['password']):
            print("asd5")
            flash("Error, passwords do not match", 'danger')
            return render_template('index.html')
            # check that username does not already exist
        elif (db.users.find({'_id': registerForm['emailreg']}).count() != 0):
            print("asd6")
            flash("Error, user already exists", 'danger')
            return render_template('index.html')
        else:
            print("asd89")

            # when successful, render the success page and add the user with limited access
            userSecurity = userDAO.userDAO(db)

            additionalInfo = {}
            # add all of the other form fields to the database
            # for field in registerForm:
            #     # make sure not to overwrite unsecure values
            #     if field.name not in ['csrf_token', 'passwordReg', 'passwordConf', 'createLinuxUser', 'userNameReg']:
            #         additionalInfo[field.name] = field.data


            print("asd")
            # hashing the username makes the confirm url extremely difficult to guess (and look long, as expected)
            user = userSecurity.add_user(registerForm['emailreg'], registerForm['password'],
                                          2, {})
            print("asd2")
            flash("Registered Successfully!", 'info')
            return render_template('index.html')



    else:
        flash("Form is missing required information, please check below", 'info')
        return redirect('/')


@users_B.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    flash("Logged out successfully", 'success')
    return redirect('/')




               
        
