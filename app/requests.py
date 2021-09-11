import urllib.request, json
from app.news import Everything


api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    Function tha gets the json response to our url request
    '''
    
    # get_news_url = base_url.format(api_key)
    get_news_url = 'https://newsapi.org/v2/everything?q=sports&apiKey=26ea37785fde4254830dfa0d226ac805'
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
            
            
    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of news objects
    '''
    
    news_results = []
    for news_item in news_list:
        #id  = news_item.get('id')
        title =news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        urlToImage = news_item.get('urlToImage')
        
        if urlToImage:
            news_object = Everything(author, title, description, url, urlToImage, publishedAt, content)
            news_results.append(news_object)
            
    return news_results