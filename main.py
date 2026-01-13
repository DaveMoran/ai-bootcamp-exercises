"""
Exercise 1: Deck of Cards

A simple Deck of Cards class that utlilizes special methods for most
of its needs
"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class DeckOfCards:
    def __init__(self):
        deck = []

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, idx):
        return self.deck[idx]
