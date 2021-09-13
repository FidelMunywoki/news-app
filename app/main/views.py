from flask import render_template, redirect, url_for, request
from . import main
from ..requests import get_news_sources, get_news_articles, topheadlines


#views

@main.route('/')

def index():
    """
      view root  page that returns the index page and its data
    
    """
    title = 'PASHA - Home of Treading News'
    
    general_category = get_news_sources('general')
    business_category = get_news_sources('business')
    entertainment_category = get_news_sources('entertainment')
    sports_category = get_news_sources('sports')
    technology_category = get_news_sources('technology')
    science_category = get_news_sources('science')
    health_category = get_news_sources('health')
    
    
    return render_template('index.html', title = title, general = general_category, business = business_category, entertainment = entertainment_category, sport = sports_category,technology = technology_category, science = science_category, health = health_category)


@main.route('/articles/<source_id>')
def articles(source_id):
  """
  Function that returns articles accordig to thier sources
  
  """
  news_source = get_news_articles(source_id)
  title = f'{source_id} | All Articles'
  
  return render_template('articles.html', title = title, name = source_id,news = news_source)




@main.route('/topheadlines&<int:per_page>')
def headlines(per_page):
    '''
    Function that returns top headlines articles
    '''
    topheadlines_news = topheadlines(per_page)
    title = 'Top Headlines'

    return render_template('topheadlines.html', title = title, name = 'Top Headlines', news = topheadlines_news)