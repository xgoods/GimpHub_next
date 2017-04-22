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





@users_B.route('/verifylogin', methods = ['POST'])
def verifylogin():

    loginForm = request.form
    
    if loginForm.validate_on_submit():
        db = get_db()


        userSecurity = userDAO.userDAO(db)
        user = userSecurity.validate_login(loginForm.email.data.lower(),loginForm.password.data)

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

    return render_template("completepage.html", header = header, body = body, loginForm = loginForm)


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

@users_B.route('/verifyregister', methods=['POST'])
@disableLDAP
def verifyregister():
    registerForm = forms.registerForm()

    if registerForm.validate_on_submit():

        db = get_db()

        if (registerForm.passwordReg.data != registerForm.passwordConf.data):
            flash("Error, passwords do not match", 'danger')
            return redirect('/register')
            # check that username does not already exist
        elif (db.users.find({'_id': registerForm.userNameReg.data}).count() != 0):
            flash("Error, user already exists", 'danger')
            return redirect('/register')
        else:
            # when successful, render the success page and add the user with limited access
            userSecurity = userDAO.userDAO(db)

            additionalInfo = {}
            # add all of the other form fields to the database
            for field in registerForm:
                # make sure not to overwrite unsecure values
                if field.name not in ['csrf_token', 'passwordReg', 'passwordConf', 'createLinuxUser', 'userNameReg']:
                    additionalInfo[field.name] = field.data



            # hashing the username makes the confirm url extremely difficult to guess (and look long, as expected)
            user = userSecurity.add_user(registerForm.email.data, registerForm.passwordReg.data,
                                          2, additionalInfo)

            return redirect('/registercomplete')

    else:
        flash("Form is missing required information, please check below", 'info')
        return render_template('register.html', registerForm=registerForm)


@users_B.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    flash("Logged out successfully", 'success')
    return redirect('/')




               
        
