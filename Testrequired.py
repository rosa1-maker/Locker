import unittest

from required_data import RequiredData

class TestRequired(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_required = RequiredData() 

    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_required.platform, "Gmail")
        self.assertEqual(self.new_required.username, "terry")
        self.assertEqual(self.new_required.password, "rosa2d")

    def tearDown(self):
    
        RequiredData.required = []

    def test_save_credential(self):
        """
        test if required data is saved in the required list
        """
        self.new_required.save_required()  
        self.assertEqual(len(RequiredData.required), 1)

    def test_display_required(self):
        """
        test display required data method
        """
        # self.assertEqual(RequiredData.display_required(), RequiredData.required)

if __name__ == '__main__':
    unittest.main()