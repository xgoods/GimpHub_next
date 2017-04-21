__author__ = 'paul'

#from app import app
from flask import Flask
from celery import Celery
from .crawl import getArticle

from . import functions


def make_celery(app):
    celery = Celery('celery', broker=app.config['CELERY_BROKER_URL'],
                    backend=app.config['CELERY_BROKER_URL'])
    celery.config_from_object("celeryconfig")
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config.from_pyfile('../config.py')


# queue = Celery('celery', broker=app.config['CELERY_BROKER_URL'])
# queue.config_from_object("celeryconfig")

queue = make_celery(app)


# def getActive():
#
#     i = current_app.control.inspect()
#     print i.active()
#
#     return 0

@queue.task
def updateNews():

    articles = [{'category':'US_News','url':'http://www.nydailynews.com/news/politics/donald-trump-accused-groping-woman-breast-1998-u-s-open-article-1.2838346'},
                {'category':'US_News','url':'http://www.nydailynews.com/news/politics/donald-trump-accused-groping-woman-breast-1998-u-s-open-article-1.2838346'},] # articles

    db = functions.get_db_proc()
    for article in articles:
        if not article['title'] or article['title'].isspace():
            article['title'] = getArticle.get_generic_title(article['url'])
        article['content'] = getArticle.get_generic_article(article['url'])

        db.articles.insert(article)



