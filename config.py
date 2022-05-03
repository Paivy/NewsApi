import os

from instance.config import NEWS_API_KEY
class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey= d19196c92d7e4608b4948b64b292c88b'
    NEWS_API_KEY  = os.environ.get('d19196c92d7e4608b4948b64b292c88b')


class  ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production':ProdConfig
}