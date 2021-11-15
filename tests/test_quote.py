import unittest
from app.models import Quote

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
        self.new_quote = Quote(12, "Kevson", "my name is kevson")
        
    def tearDown(self):
        '''
        Method that cleans up after every test case
        '''
        Quote.quote_list = []
        
    def test_init(self):
      self.assertEqual(self.new_user.id, 12)
      self.assertEqual(self.new_user.username, "Kevson")
      self.assertEqual(self.new_user.email, "my name is kevson")
      