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
        
    def test_playerGetTile(self):
        player_1 = Player()
        bagGeneral = BagTiles()
        player_1.getTiles(2, bagGeneral)
        self.assertEqual(len(player_1.tiles), 2)

    def test_playerGetTileOutOfRange_I(self):
        player_1 = Player()
        bagGeneral = BagTiles()
        player_1.getTiles(4, bagGeneral)
        with self.assertRaises(TilesOutOfRange):
            player_1.getTiles(4, bagGeneral)
        player_1.getTiles(2, bagGeneral)
        self.assertEqual(len(player_1.tiles), 6)


    def test_playerGetTileOutOfRange_II(self):
        player_1 = Player()
        bagGeneral = BagTiles()
        with self.assertRaises(TilesOutOfRange):
            player_1.getTiles(8, bagGeneral)
        player_1.getTiles(2, bagGeneral)
        self.assertEqual(len(player_1.tiles), 2)







if __name__ == '__main__':
    unittest.main()
