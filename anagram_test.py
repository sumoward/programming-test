"""
Unit test for anagram

"""

import unittest
from anagram import anagram


class annagramTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_annagram(self):
        word = 'dog'
        word_list = ['cat', 'dog', 'got', 'sheep', 'GOT', 'cat', 'DOG', 'god']
        self.assertEqual(['god'], anagram(word, word_list))
        word_list = ['cat', 'dog', 'got', 'sheep', 'GOT', 'cat', 'DOG']
        self.assertEqual([], anagram(word, word_list))
        word_list = ['god', 'god', 'god']
        self.assertEqual(['god'], anagram(word, word_list))
        word = 'aeprs'
        # has 12 anagrams
        word_list = ['cat', 'dog', 'got', 'sheep', 'GOT', 'cat', 'DOG', 'god',
                     'apers', 'apres', 'asper', 'pares', 'parse', 'pears',
                     'prase', 'presa', 'rapes', 'reaps', 'spare', 'spear']
        self.assertEqual(['apers', 'apres', 'asper', 'pares',
                          'parse', 'pears', 'prase', 'presa',
                          'rapes', 'reaps', 'spare',
                          'spear'], anagram(word, word_list))
        self.assertEqual(12, len(anagram(word, word_list)))


if __name__ == "__main__":
    unittest.main()
