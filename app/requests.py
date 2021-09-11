import urllib.request, json

from app.news import Everything, EverythingSources


api_key = None
sources_url = None
articles_url = None
top_headlines_url = None
everything_url = None 
everything_search_url = None 

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_SOURCE_BASE_URL']
    top_headlines_url = app.config['TOP_HEADLINES_BASE_URL']



# news sources

def get_news_sources(category):
    '''
    Function tha gets the json response to our url request
    '''
    
    # get_news_url = base_url.format(api_key)
    get_news_sources_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'.format(category, api_key)
    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)
        
        news_results = None
        
        if get_news_sources_response['sources']:
            news_sources_results_list = get_news_sources_response['sources']
            news_sources_results = process_sources_results(news_sources_results_list)
            
            
    return news_sources_results

def process_sources_results(news_sources_list):
    '''
    Function  that processes the news sources result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain sources details

    Returns :
        news_results: A list of news objects
    '''
    
    news_sources_results = []
    for news_sources_item in news_sources_list:
        source_id  = news_sources_item.get('id')
        source_name =news_sources_item.get('name')
        source_description = news_sources_item.get('description')
        source_url = news_sources_item.get('url')
        source_category = news_sources_item.get('category')
        language = news_sources_item.get('language')
        source_country = news_sources_item.get('country')
        
        if source_url:
            news_source_object = EverythingSources(source_id, source_name, source_description, source_url, source_category, language, source_country)
            news_sources_results.append(news_source_object)
            
    return news_sources_results


# get new articles
def get_news_articles(source_id,article):
    '''
    Function tha gets the json response to our url request
    '''
    
    # get_news_url = base_url.format(api_key)
    get_news_articles_url = articles_url.format(source_id, article, api_key)
    with urllib.request.urlopen(get_news_articles_url) as url:
        get_news_articles_data = url.read()
        get_news_articles_response = json.loads(get_news_articles_data)
        
        news_articles_results = None
        
        if get_news_articles_response['articles']:
            news_articles_results_list = get_news_articles_response['articles']
            news_articles_results = process_article_results(news_articles_results_list)
            
            
    return news_articles_results

def process_article_results(news_articles_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of news objects
    '''
    
    news_articles_results = []
    for news_article_item in news_articles_list:
        title =news_article_item.get('title')
        author = news_article_item.get('author')
        description = news_article_item.get('description')
        url = news_article_item.get('url')
        publishedAt = news_article_item.get('publishedAt')
        content = news_article_item.get('content')
        urlToImage = news_article_item.get('urlToImage')
        
        if urlToImage:
            news_article_object = Everything(author, title, description, url, urlToImage, publishedAt, content)
            news_articles_results.append(news_article_object)
            
    return news_articles_results


# get top headline stories

def topheadlines(category):
    '''
    Function that gets articles based on the source id
    '''
    get_topheadlines_url = top_headlines_url.format(api_key)

    with urllib.request.urlopen(get_topheadlines_url) as url:
        topheadlines_data = url.read()
        topheadlines_response = json.loads(topheadlines_data)

        topheadlines_results = None
        
        if topheadlines_response['articles']:
            topheadlines_results = process_article_results(topheadlines_response['articles'])

    return topheadlines_results