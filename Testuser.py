import unittest

from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("Teresa", "Wanjiku", "teresawanjiku2000@gmail.com", "Terry", "rosa2d") 

    def test_init(self):
        """
        testing initialization of class
        """
        self.assertEqual(self.new_user.firstName, "Teresa")
        self.assertEqual(self.new_user.lastName, "Wanjiku")
        self.assertEqual(self.new_user.email, "teresawanjiku2000@gmail.com")
        self.assertEqual(self.new_user.username, "Terry")
        self.assertEqual(self.new_user.password, "rosa2d")

    def tearDown(self):
        """
        restart
        """
        UserData.create_account = []

    def test_save_account(self):
        """
        testing save account method
        """
        self.new_user.save_account() 
        self.assertEqual(len(UserData.create_account), 1)


if __name__ == '__main__':
    unittest.main()