from flask import Flask
from flask import render_template
import feedparser


application = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition_world.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@application.route('/')
def hello():
    return '<h1 style="color:blue">Hello There!</h1>'

@application.route('/news')
@application.route('/news/<site>')
def news(site='bbc'):
    site = site.lower() if site.lower() in RSS_FEEDS else 'bbc'
    url = RSS_FEEDS[site]
    feed = feedparser.parse(url)
    first_article = feed['entries'][0]
    return render_template('home.html', articles=feed['entries'])


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
