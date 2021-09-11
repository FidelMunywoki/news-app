from flask import render_template
from . import main
from ..requests import get_news


#views

@main.route('/')

def index():
    """
      view root  page that returns the index page and its data
    
    """
    title = 'PASHA - Home of Treading News'
    
    news = get_news()
    
    return render_template('index.html', title = title, news = news)
