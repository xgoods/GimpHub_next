#!flask/bin/python
from .app import app
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)

#app.run(host=app.config['GLOBAL_HOST'], port = app.config['GLOBAL_PORT'], debug = app.config['DEBUG'])

if __name__ == '__main__':
    app.run()
