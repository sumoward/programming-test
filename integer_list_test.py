"""
Unit test for integer

"""

import unittest
from integer_list import integer_find


class annagramTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_integer_find(self):
        number = 23
        self.assertFalse(integer_find(number))
        number = 1936
        self.assertTrue(integer_find(number))
        number = 7777
        self.assertFalse(integer_find(number))


if __name__ == "__main__":
    unittest.main()
