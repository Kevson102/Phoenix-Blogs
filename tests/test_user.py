import unittest # imports the unittest module
from app.models import User # imports the users class from the user.py file

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
        self.new_user = User(12, "Kevson", "kevson@gmail.com", "qwrttyy", "my name is kevson", "CsGitituComp")
        
    def tearDown(self):
        '''
        Method that cleans up after every test case
        '''
        User.user_list = []
        
    def test_init(self):
      self.assertEqual(self.new_user.id, 12)
      self.assertEqual(self.new_user.username, "Kevson")
      self.assertEqual(self.new_user.email, "kevson@gmail.com")
      self.assertEqual(self.new_user.profile_pic_path, "qwrttyy")
      self.assertEqual(self.new_user.user_bio, "my name is kevson")
      self.assertEqual(self.new_user.pass_secure, "CsGitituComp")
    

# if __name__ == '__main__':
#   unittest.main()