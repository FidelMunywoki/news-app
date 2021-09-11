

import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=sports&apiKey={}'
    NEWS_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
       Config : The parent configuration class with General configurations settings
    '''
    pass
class DevConfig(Config):
    '''
    Developmet configuration child class
    
    Args:
       Config: The parent configuration class with General  configuration setting
    '''
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}