import collections
from random import choice
Card = collections.namedtuple('Card', ['牌面', '花色']) # rank牌面    Suit花色
suit_values = dict(黑桃=3, 红心=2, 方块=1, 梅花=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')    #Rank(牌面 指数字2-10 JQKA)
    suits = '黑桃 方块 梅花 红心'.split()  #黑桃 方块 梅花 红心
    # suits = 'spades diamonds clubs hearts'.split()  #黑桃 方块 梅花 红心
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        # print(self._cards)
        # self._cards = [Card(牌面='2', 花色='黑桃'), Card(牌面='3', 花色='黑桃'), Card(牌面='4', 花色='黑桃')....
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.牌面)
    return rank_value * len(suit_values) + suit_values[card.花色]
  
deck = FrenchDeck()
# print("随机选择了：")
# print(choice(deck))
#  Card(牌面='J', 花色='红心')
for card in sorted(deck, key=spades_high):  #sorted() 函数对所有可迭代的对象进行排序操作 sorted(iterable, key=None, reverse=False)
    print(card)
# Card(牌面='2', 花色='梅花')
# Card(牌面='2', 花色='方块')
# Card(牌面='2', 花色='红心')
# Card(牌面='2', 花色='黑桃')
# Card(牌面='3', 花色='梅花')
# Card(牌面='3', 花色='方块')


# print(deck[12::13])
# print(suit_values)
# print(deck[11::13])
# print(choice(deck))
# print(deck[-1])
# beer_card = Card('7', 'diamonds')
# print(beer_card)
