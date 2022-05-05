import urllib.request,json
from .models import Article,Source

api_key = None
api_base_url = None
# art_url = None
# articles_url=None

def configure_request(app):
    global api_key,api_base_url
    api_key = app.config['NEWS_API_KEY']
    # s_url = app.config['SOURCE_ARTICLES_URL']
    api_base_url = app.config['NEWS_API_BASE_URL']
    # art_url = app.config['NEWS_ARTICLES_APL_URL']
    
# def get_sources(category):
#     """
#     function that gets response from the api call
#     """
#     sources_url = s_url.format(category,api_key)

#     with urllib.request.urlopen(sources_url) as url:
#         sources_data = url.read()
#         response = json.loads(sources_data)
#         sources_outcome = None
#         if response['sources']:
#             sources_outcome_items = response['sources']
#             sources_outcome = process_new_sources(sources_outcome_items)
#     return sources_outcome


# def process_new_sources(sources_list):
#     sources_outcome = []
#     for one_source in sources_list:
#         id = one_source.get("id")
#         name = one_source.get("name")
#         description = one_source.get("description")
#         url = one_source.get("url")
#         category = one_source.get("category")
#         language = one_source.get("language")
#         country = one_source.get("country")
#         new_source = Source(id,name,description,url,category,language,country)
#         sources_outcome.append(new_source)
#     return sources_outcome

def get_articles(category=None,source=None):
    articles_url = None
    if category is not None:
        articles_url = api_base_url.format(f'top-headlines?category={category}&language=en',api_key)
    elif source is not None:
        articles_url = api_base_url.format(f'top-headlines?sources={source}&language=en',api_key)
    else:
        articles_url = api_base_url.format(f'top-headlines?language=en',api_key)

    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        articles_outcome = None
        if articles_response['articles']:
            articles_outcome_items = articles_response['articles']
            articles_outcome = process_new_articles(articles_outcome_items)
    return articles_outcome


def process_new_articles(articles_list):
    articles_outcome = []
    for article in articles_list:
        source = article.get("source")
        author = article.get("author")
        description = article.get("description")
        title = article.get("title")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt")
        if urlToImage:
            new_article = Article(source, author, title, description, url, urlToImage, publishedAt)
            articles_outcome.append(new_article)
    return articles_outcome


def get_sources():
    source_url = api_base_url.format("sources?language=en",api_key)
    with urllib.request.urlopen(source_url) as url:
        art_data = url.read()
        response = json.loads(art_data)
        source_articles = None
        if response['sources']:
            sources_list = response['sources']
            source_articles = process_sources(sources_list)
    return source_articles

def process_sources(sources_list):
    source_objects = []
    for source in sources_list:
        id = source.get("id")
        name = source.get('name')
        source_object = Source(id,name)
        source_objects.append(source_object)
    return source_objects

# def search_articles(article_name):
#     search_url = art_url.format(article_name,api_key)
#     with urllib.request.urlopen(search_url) as url:
#         search_data = url.read()
#         search_response = json.loads(search_data)
#         search_outcome= None
#         if search_response['articles']:
#             all_search_results = search_response['articles']
#             search_outcome = search_articles(all_search_results)
#     return search_outcome