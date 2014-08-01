"""
Write  a  console  application  that  simulates  of  a  card
game  that  mix  up  a   standard  deck  of  cards  and  then
deal  the  cards  to  the  players  without   using  the  same
card  more  than  once.

"""
import random


class Card_Game:
    pass

    def __init__(self):
        self.pack = ['Ac', '2c', '3c', '4c', '5c', '6c', '7c',
                     '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc',
                     'Ad', '2d', '3d', '4d', '5d', '6d',
                     '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd',
                     'Ah', '2h', '3h', '4h', '5h', '6h',
                     '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh',
                     'As', '2s', '3s', '4s', '5s', '6s',
                     '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks']
        self.player1 = []
        self.player2 = []

    def random_card(self):
        rank = random.choice(('A', '2', '3', '4',
                              '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'))
        suit = random.choice(('c', 'd', 'h', 's'))
        # print (rank, suit)
        card = rank + suit
        return card

    def deal_card(self):
        dealt = True
#         new_deck = self.pack
        while dealt:
            card = self.random_card()
            # print ('deck:',len(self.pack))
            # print (self.pack)
            # = str(rank + suit)
            # print(card)
            if card in self.pack:
                self.pack.remove(card)
                # print('inside ', card)
                dealt = False
                return card
            else:
                dealt = True
                # print('not')
                # break
                card = ''

    def deal(self):
        # new_deck = self.pack
        # card = self.random_card()
        # print(card)
        p1_len = len(self.player1)
        p2_len = len(self.player2)
        while p1_len < 5 and p2_len < 5:
            card = self.deal_card()
            # print(card)
            self.player1.append(card)
            p1_len = len(self.player1)
            # print('1:',self.player1)
            card = self.deal_card()
            # print(card)
            card = self.random_card()
            self.player2.append(card)
            p2_len = len(self.player2)
            # print('2:', self.player2)
        print(self.pack)
        print(self.player1, self.player2)
        return self.player1, self.player2


if __name__ == "__main__":
    game = Card_Game()
    game.deal()