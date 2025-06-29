from random import randint


class Deck:
    ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
    suits = ["clubs", "spades", "diamonds", "hearts"]

    def __init__(self, deck=None):
        if deck == None:
            self.cards = [(rank, suit) for rank in Deck.ranks for suit in Deck.suits]
        else:
            self.cards = deck

    # print the deck
    def print_deck(self):
        for rank, suit in self.cards:
            print(f"{rank} of {suit}")

    # shuffle the deck
    def shuffle(self):
        for i in range(self.number_of_cards()):
            random_place = randint(0, self.number_of_cards() - 1)
            tmp = self.cards[i]
            self.cards[i] = self.cards[random_place]
            self.cards[random_place] = tmp

    # peek the first card on the deck
    def peek_first(self):
        return self.cards[0]

    # peek the last card on the deck
    def peek_last(self):
        return self.cards[-1]

    # deal the first card on the deck
    def deal_first(self):
        return self.cards.pop(0)

    # deal the last card on the deck
    def deal_last(self):
        return self.cards.pop(-1)

    # deal the specified number of cards
    def deal(self, number_of_cards=1):
        dealt_cards = []
        for i in range(number_of_cards):
            dealt_cards.append(self.deal_first())

        return dealt_cards

    def number_of_cards(self):
        return len(self.cards)
