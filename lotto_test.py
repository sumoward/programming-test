import unittest
from lotto import lotto_day


class annagramTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_sql_connector1(self):
        pass
        self.dedsert.add_user('brian1', 134, 'astronaut1')
        self.assertEqual("[(1, 'brian1', 134, 'astronaut1')]",
                         self.dedsert.__str__())
        self.dedsert.add_user('brian2', 1345, 'astronaut2')
        self.assertEqual("[(1, 'brian1', 134, 'astronaut1'), (2, 'brian2', 1345, 'astronaut2')]",
                         self.dedsert.__str__())



if __name__ == "__main__":
    unittest.main()