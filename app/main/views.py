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