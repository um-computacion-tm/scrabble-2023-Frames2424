import unittest
from game.player import Player, TilesOutOfRange
from game.models import Tile, BagTiles


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_startTurn(self):
        player_1 = Player()
        player_1.startTurn()
        self.assertEqual(
            (player_1.turn),
            True)
        
    def test_startAndEndTurn(self):
        player_1 = Player()
        player_1.startTurn()
        self.assertEqual(
            (player_1.turn),
            True)
        player_1.endTurn()
        self.assertEqual((player_1.turn),
                          False)
        
if __name__ == '__main__':
    unittest.main()
