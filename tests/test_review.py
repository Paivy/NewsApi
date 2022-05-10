import unittest
from  app.models import Sources,Articles
# Movie = movie.Movie
class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("abc-news","ABC NEWS","your trusred news source","https://abcnews.go.com","general","en","us")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles( "Applesfera.com", "Jesús Quesada", "the apple", "learn more about apples", "https://apple.com", "https://i.blogs.es/bfbe77/apple-watch-series-7/840_560.jpg","2022-05-02T05:13:03Z")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


