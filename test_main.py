import random
import unittest

from main import DeckOfCards, Card


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.testDeck = DeckOfCards()

    def test_len(self):
        assert len(self.testDeck) == 52

    def test_getitem(self):
        assert isinstance(self.testDeck[0], Card)
        with self.assertRaises(IndexError):
            self.testDeck[52]

    def test_shuffle(self):
        beforeShuffleOne = self.testDeck[0]
        beforeShuffleTwo = self.testDeck[1]
        beforeShuffleThree = self.testDeck[2]

        random.shuffle(self.testDeck)

        afterShuffleOne = self.testDeck[0]
        afterShuffleTwo = self.testDeck[1]
        afterShuffleThree = self.testDeck[2]

        assert beforeShuffleOne != afterShuffleOne
        assert beforeShuffleTwo != afterShuffleTwo
        assert beforeShuffleThree != afterShuffleThree
