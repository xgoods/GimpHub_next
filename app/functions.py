from app import app
import pymongo
from flask import g, session
import configparser

def connect_db():
    connection = pymongo.MongoClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])
    if all(not x for x in (app.config['MONGO_AUTHENTICATION_DATABASE'],
                           app.config['MONGO_USER'])):
        pass
    elif app.config['MONGO_AUTHENTICATION_DATABASE'] == None:
        getattr(connection, app.config['MONGO_DATABASE']).authenticate(app.config['MONGO_USER'],
                                                                       app.config['MONGO_PASS'])
    else:
        getattr(connection, app.config['MONGO_AUTHENTICATION_DATABASE']).authenticate(app.config['MONGO_USER'],
                                                                                      app.config['MONGO_PASS'])
    database = getattr(connection, app.config['MONGO_DATABASE'])
    return (connection, database,)


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    try:
        if not hasattr(g, 'db'):
            g.db = connect_db()
    except RuntimeError:
        return get_db_proc()
    return g.db[1]


def get_db_proc():
    """Opens a new database connection always to be used in a separate background process (must be closed manually)
    """
    return connect_db()[1]


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db[0].close()


