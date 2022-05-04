import urllib.request,json
from .models import News

#Getting api key
api_key = None

#Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
def get_news():
    """
    function that gets the json response to our url request
    """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
        #print(news_results_list)
            news_results = process_results(news_results)

    return news_results
def process_results(news_list):
    """
    Function that processes the movie result and transform them to a list of objects
    Args:
    news_list: Alist of dictionaries that contains news details
    
    Returns :
        news_results: A list of news objects
    """

    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        urlToimage = news_item.get('urlToimage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')

        news_object = News(title,description,urlToimage,content,publishedAt)
        #print(news_object)
        news_results.append(news_object)
        #print(news_results)
    return news_results

#Sources
# def get_sources():
#     """
#     ffunction that gets the json responce to our url request
#     """
#     get_news_url = base_url.format(api_key)
#     get_sources_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey= d19196c92d7e4608b4948b64b292c88b'

#     with urllib.request.urlopen(get_sources_url) as url:
