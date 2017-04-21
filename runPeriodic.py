import threading
from .app.crawl import getArticle, rucrawler
import pymongo

INTERVAL_SECONDS = 30*60
MONGO_HOST = '52.54.134.145'
MONGO_PORT = 27017
MONGO_DATABASE = 'mizzychan'

def get_db():
    connection = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    database = getattr(connection, MONGO_DATABASE)
    return connection, database



def run():
    threading.Timer(INTERVAL_SECONDS, run).start()
    # articles = [{'category': 'US_News',
    #            'url': 'http://www.nydailynews.com/news/politics/donald-trump-accused-groping-woman-breast-1998-u-s-open-article-1.2838346'},
    #           {'category': 'US_News',
    #            'url': 'http://www.nydailynews.com/news/politics/donald-trump-accused-groping-woman-breast-1998-u-s-open-article-1.2838346'}, ]  # articles

    #articles = rucrawler.getPolitics()
    #articles += rucrawler.getBusiness()
    #articles += rucrawler.getEntertainment()
    articles = rucrawler.getMemes()
    #articles += rucrawler.getSports()
    #articles += rucrawler.getTech()
    #articles += rucrawler.getUSNews()
    #articles += rucrawler.getWorldNews()
    conn, db = get_db()
    for article in articles:
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
        except Exception as e:
            print(e)
        try:
            db.articles.insert(article)
        except pymongo.errors.DuplicateKeyError:
            print("duplicate URL, ignoring")
        except Exception as e:
            print("unknown error: %s" % str(e))
    conn.close()
run()