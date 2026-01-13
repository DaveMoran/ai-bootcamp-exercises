import unittest

from main import DeckOfCards


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.testDeck = DeckOfCards()
