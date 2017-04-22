from app import app
import random
import string
import hashlib
import pymongo
import pwd
import logging
import subprocess
import crypt

class userDAO(object):

    def __init__(self, db):
        self.db = db
        self.users = self.db.users
        self.SECRET = 'verysecret'
        self.logr = logging.getLogger('gimphub.userDAO')
        self.dbconfig = db.config.find_one({}, {'_id':0})

    # makes a little salt
    def make_salt(self):
        salt = ""
        for i in range(5):
            salt = salt + random.choice(string.ascii_letters)
        return b"asfaslk"

    # implement the function make_pw_hash(name, pw) that returns a hashed password
    # of the format:
    # HASH(pw + salt),salt
    # use sha256

    def make_pw_hash(self, pw,salt=None):
        if salt == None:
            salt = self.make_salt()
        return hashlib.sha256(pw.encode('utf-8')).hexdigest()
    
    #make a hash of the user name to use for the registration confirm email
    def make_user_hash(self, user_id, salt=None):        
        return hashlib.sha256(user_id).hexdigest()
    
    #make a hash of the user name slightly different to use for the administrator approval
    def make_user_hash_admin(self, user_id, salt=None):
        if salt == None:
            salt = self.make_salt();
        return hashlib.sha256(user_id).hexdigest()

    # Validates a user login. Returns user record or None for failure or False for lockout
    def validate_login(self, username, password):
               
        user = None
        try:
            user = self.users.find_one({'_id': username.lower()})
        except:
            self.logr.error("Unable to query database for user")

        if user is None:
            self.logr.debug("User %s not in database" % username)
            return None

        if 'nFailedLogins' in user and user['nFailedLogins'] >= self.dbconfig.get('loginAttemptsBeforeLock', 3):
            self.logr.debug("user %s is locked out" % username)
            return False

        #salt = user['password'].split(',')[1]

        if user['password'] != self.make_pw_hash(password):
            self.logr.debug("user password is not a match")
            if 'nFailedLogins' in user:
                nFailed = user['nFailedLogins']
            else:
                nFailed = 0
            self.users.update({'_id':user['_id']}, {'$set':{'nFailedLogins':nFailed+1}})
            return None

        # Looks good
        self.users.update({'_id': user['_id']}, {'$set':{'nFailedLogins':0}})
        return user
    
    # levels: {0: reserved, 1:admin, 2:standard user, 3:verified email but not activated, 4:not verified email, 5:banned}
    # creates a new user in the users collection
    def add_user(self, username, password, level, additionalInfo={}):

        print(password.encode('utf-8'))
        password_hash = self.make_pw_hash(password)
        #userHash = self.make_user_hash(username)
        #userHashAdmin = self.make_user_hash_admin(username)



        printable = set(string.printable)
        userName = filter(lambda x: x in printable, username.lower())

        user = {'_id': username.lower(), 'password': password_hash, 'level': level, 'username': userName}

        #remove the left over value of user name LATER I NEED TO REMEMBER WHERE THE PASSWORD WAS DONE LIKE THIS AND REMOVE IT THERE
        additionalInfo.pop('userName',None) 
        
        #username and password is all that is required, but we can provide more information optionally
        user.update(additionalInfo)
        
        try:
            self.users.insert(user)
        except pymongo.errors.OperationFailure:
            self.logr.debug("oops, mongo error")
            return 'The mongo driver has failed. Please contact the web-master immediately'
        except pymongo.errors.DuplicateKeyError as e:
            self.logr.debug("oops, username is already taken")
            return 'That username is already taken'        

        return user
    
    #platform extension possibility: create the same user on the server.
    def add_user_linux(self, username, password):
        try:
            pwd.getpwnam(username)
            self.logr.info('User %s already exists on the headnode, skipping creation' % username)
        except KeyError:            
            self.logr.info('User %s does not exist on headnode, creating...' % username)
            encpassword = crypt.crypt(password, self.make_salt())
            try:
                subprocess.check_call(["useradd","-d",'/home/'+username,'-m','-p',encpassword,'-c',username,'-s','/bin/bash',username])
            except:
                self.logr.error('Count not create user %s on the headnode: subprocess call returned with non-zero exit status.')
            try:
                subprocess.check_call(["usermod", "-a", '-G', 'fuse', username])
            except:
                self.logr.error('Count not add user %s to fuse group.')

                
    def check_user_linux(self, username):
        
        try:
            pwd.getpwnam(username)
            self.logr.debug('User %s does indeed exist on the headnode' % username)
            exists = True
        except KeyError:
            exists = False
            self.logr.debug('User %s does not exist on the headnode' % username)
        return exists
    
    #update a user's information in the database
    def update_user(self, username, updates={}):
        

        for update in updates:
            
            if update == 'passwordReg':
                password_hash = self.make_pw_hash(updates['passwordReg'])
                
                self.users.update({'_id':username.lower()},{'$set':{'password':password_hash}})
                
            else:
                self.users.update({'_id':username.lower()},{'$set':{update:updates[update]}})
    
    #generate a new random password for a user and reset it            
    def reset_password(self, username):
        
        password = self.make_salt() + self.make_salt()
        self.update_user(username, {'passwordReg':password})
        return password
        
        

