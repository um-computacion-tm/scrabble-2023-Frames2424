def testPuntajes_II(self):
        values = BagTiles().tiles
        self.assertEqual(values['Z'], 10)
    # @patch('random.shuffle')
    # def test_bag_tiles(self, patch_shuffle):
    #     bag = BagTiles()
    #     self.assertEqual(
    #         len(bag.tiles),
    #         5,
    #     )
    #     self.assertEqual(
    #         patch_shuffle.call_count,
    #         1,
    #     )
    #     self.assertEqual(
    #         patch_shuffle.call_args[0][0],
    #         bag.tiles,
    #     )


    # def test_take_initial(self):
    #     bag = BagTiles()
    #     initial_tiles = len(bag.tiles)
    #     initial_take_tiles = bag.take(7)
    #     self.assertEqual(
    #         len(initial_take_tiles),
    #         7,
    #     )
    #     self.assertEqual(
    #         len(bag.tiles),
    #         initial_tiles - 7,
    #     )

    # def test_put_I(self):
    #     bag = BagTiles()
    #     currently_tiles = len(bag.tiles)
    #     put_tiles = [Tile('A', 1), Tile('Z', 10), Tile('Y', 4)]
    #     bag.put(put_tiles)
    #     self.assertEqual(
    #         len(bag.tiles),
    #         currently_tiles + 3,
    #     )


if __name__ == '__main__':