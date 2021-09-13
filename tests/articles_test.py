import unittest
from app .news import Everything


class TestArticles(unittest.TestCase):
    '''
    Class to test the behaviour of the articles class
    '''
    def setUp(self):
        self.new_article = Everything('Amerix', 'Guard your Frame', 'It is the time for men to realize how much they are worthy', 'https://goodmenproject.com/ethics-values/men-worthy-despite-taught-fiff/', 'https://bing.com/images', '2021-08-12T11:31:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Everything))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.author, 'Amerix')
        self.assertEquals(self.new_article.title, 'Guard your Frame')
        self.assertEquals(self.new_article.description, 'It is the time for men to realize how much they are worthy')
        self.assertEquals(self.new_article.url, 'https://goodmenproject.com/ethics-values/men-worthy-despite-taught-fiff/')
        self.assertEquals(self.new_article.urlToImage,'https://bing.com/images')
        self.assertEquals(self.new_article.publishedAt, '2021-08-12T11:31:03Z')
