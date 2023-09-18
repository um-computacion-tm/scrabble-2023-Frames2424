import unittest
from game.models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tile_II(self):
        tile = Tile('B', 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 2)


class TestBagTiles(unittest.TestCase):
    def testPuntajes_I(self):
        values = BagTiles().tiles
        self.assertEqual(values['A'], 1)

    def testPuntajes_II(self):
        values = BagTiles().tiles
        self.assertEqual(values['Z'], 10)


if __name__ == '__main__':
    unittest.main()
