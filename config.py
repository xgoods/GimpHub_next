
#FLASK SETTINGS
DEBUG = True
CSRF_ENABLED = False
SECRET_KEY = 'pksd33r3fmn123'

#FILE LOCATION SETTINGS
LOG_CONFIG_FILE = 'app/ini/log.ini.nofile'

#SERVER SETTINGS
GLOBAL_HOST = '0.0.0.0'
GLOBAL_PORT = 5000

#EMAIL SETTINGS
MAIL_SERVER='smtp.1and1.com'
MAIL_PORT=587
MAIL_USE_SSL=False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

#MONGO_SETTINGS
MONGO_HOST = 'gimphub.duckdns.org'
MONGO_PORT = 27017
MONGO_DATABASE = 'gimphub'
MONGO_AUTHENTICATION_DATABASE = None #set to None to use same database for auth and connection
MONGO_USER = None
MONGO_PASS = None

#USER AUTHENTICATION SETTINGS
SESSION_TIMEOUT_MINUTES = 10080

#CELERY SETTINGS
CELERY_ENABLE = True
CELERY_BROKER_URL = 'mongodb://gimphub.duckdns.org:27017/gimphub'

SWITCH_SECONDS = 10*1