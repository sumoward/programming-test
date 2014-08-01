import unittest
from sql_connector import manageDB


class annagramTestCase(unittest.TestCase):

    def setUp(self):
        pass
        self.dedsert = manageDB()

    def tearDown(self):
        pass
        self.dedsert.db_close()

    def test_sql_connector1(self):
        pass
        self.dedsert.add_user('brian1', 134, 'astronaut1')
        self.assertEqual("[(1, 'brian1', 134, 'astronaut1')]",
                         self.dedsert.__str__())
        self.dedsert.add_user('brian2', 1345, 'astronaut2')
        self.assertEqual("[(1, 'brian1', 134, 'astronaut1'), (2, 'brian2', 1345, 'astronaut2')]",
                         self.dedsert.__str__())

    # write a second test to check our table is dropped and recreated
    def test_sql_connector2(self):
        self.dedsert.add_user('mary', 34, 'developer')
        self.assertEqual("[(1, 'mary', 34, 'developer')]",
                         self.dedsert.__str__())


if __name__ == "__main__":
    unittest.main()
