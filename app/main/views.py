from flask import render_template
from . import main
from . . requests import get_news



@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    news = get_news()
    title = "KENYANEWS"
    return render_template("index.html",title = title, articles = news)

# @main.route('/sources')
# def sources():
#     """
#     View news page function that returns the news details page and its data
#     """
#     news = get_sources()
#     return render_template('news.html', sources= news)