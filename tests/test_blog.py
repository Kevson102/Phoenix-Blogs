import unittest # imports the unittest module
from app.models import Blog # imports the users class from the user.py file

class TestBlog(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the Users class.
    Args:
        unittest.TestCase: Test case class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Setup method to run before each test case.
        '''
        self.new_blog = Blog(12, "title", "kevson", "picpath", "my name is kevson", "2021")
        
    def tearDown(self):
        '''
        Method that cleans up after every test case
        '''
        Blog.blog_list = []
        
    def test_init(self):
      self.assertEqual(self.new_blog.id, 12)
      self.assertEqual(self.new_blog.blog_title, "title")
      self.assertEqual(self.new_blog.author, "kevson")
      self.assertEqual(self.new_blog.blog_display_pic_path, "picpath")
      self.assertEqual(self.new_blog.blog_content, "my name is kevson")
      self.assertEqual(self.new_blog.date_posted, "2021")
