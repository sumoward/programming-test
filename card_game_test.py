"""
Unit test for card game

"""

import unittest
from card_game import Card_Game


class annagramTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Card_Game()

    def test_integer_find(self):
        self.assertTrue(2, len( self.game.deal()))
        player1, player2 = self.game.deal()
        # use sets to make sure values are unique
        self.assertEqual(5,  len(set(player1)))
        self.assertEqual(5,  len(set(player1)))
        # they have no elements in common
        self.assertEqual(0,  len(set(player1) & set(player2)))


if __name__ == "__main__":
    unittest.main()
