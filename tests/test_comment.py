import unittest
from app.models import Comment

class TestUsers(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the Users class.
    Args:
        unittest.TestCase: Test case class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Setup method to run before each test case.
        '''
        self.new_quote = Comment(12, "Kevson", "2021")
        
    def tearDown(self):
        '''
        Method that cleans up after every test case
        '''
        Comment.comment_list = []
        
    def test_init(self):
      self.assertEqual(self.new_comment.id, 12)
      self.assertEqual(self.new_comment.comment_message, "Kevson")
      self.assertEqual(self.new_comment.date_posted, "2021")
      
