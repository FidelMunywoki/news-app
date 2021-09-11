from flask import render_template
from . import main
from ..requests import get_news, get_news_sources


#views

@main.route('/')

def index():
    """
      view root  page that returns the index page and its data
    
    """
    title = 'PASHA - Home of Treading News'
    
    news = get_news()
    news_sources = get_news_sources()
    
    return render_template('index.html', title = title, news = news, news_sources = news_sources)
