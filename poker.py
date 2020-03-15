import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "{}{}".format(self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_three(self):
        for i in range (5):
            for j in range (i+1,5):
                for k in range (i+2,5):
                    if self.cards[i].get_rank()==self.cards[j].get_rank()==self.cards[k].get_rank():
                        return True
        return False

    def is_poker(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(i + 2, 5):
                    for l in range (i+3,5):
                        if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank()==self.cards[l].get_rank:
                            return True
        return False

    def is_flush(self):
        for i in range (5):
            if len(set(self.suit))==1:
                return True
        return False

    def is_twopair(self):

                        if self.cards[i].get_rank() == self.cards[j].get_rank() and self.cards[k]== self.cards[l].get_rank() and self.cards[i] != self.cards[k]:
                            return True

    def is_full (self):
        for i in range(5):
            if hand = is_twopair and is_three:
            return True
        return False

    def is_straight(self):
        for i in range (5):
            if hand.sorted == hand and len(hand)== 5:
                return True
        return False




new_deck = Deck()
new_deck.shuffle()
print(new_deck)
hand = Hand(new_deck)
print(hand)