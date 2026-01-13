"""
Exercise 1: Deck of Cards

A simple Deck of Cards class that utlilizes special methods for most
of its needs
"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class DeckOfCards:
    ranks = [str(n) for n in range(2, 11) + list("JQKA")]
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, idx):
        return self.deck[idx]
