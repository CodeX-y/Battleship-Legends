from player import player
from grid import grid
import unittest

# Tests for the player class

class test_player(unittest.TestCase):

    def test_add_ship(self):
        testP = player(1, grid(10,10), grid(10,10))
        actual = testP.add_ship("testShip", {"length" : 4, "identifier" : "T"}, ["a1", "a4"])
        assertTrue(1)
    def test_defeated(self):
        pass
    def test_hit_ship(self):
        pass


