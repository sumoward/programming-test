import unittest
from lotto import lotto_day
import datetime


class annagramTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sql_connector1(self):
        self.assertEqual(datetime.date(2014, 8, 2),
                         lotto_day())
        self.assertEqual(datetime.date(2014, 7, 19),
                         lotto_day('2014-07-18'))
        self.assertEqual(datetime.date(2015, 1, 1),
                         lotto_day('2014-12-31'))

if __name__ == "__main__":
    unittest.main()