import unittest
from game.cell import Cell
from game.models import Tile
from game.board import Board


class TestCell(unittest.TestCase):
    def testHorizontalPuntaje(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'V', 'ARASAKA')
        self.assertEqual(tablero.returnPointsAndMultiplier(), 30)

    def testHorizontalPuntaje2(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(5, 0, 'H', 'CAFE')
        self.assertEqual((tablero.wordCurrentPoints()), [3, 3, 4, 1])
        self.assertEqual((tablero.returnPointsAndMultiplier()), 11)

    def testHorizontalPuntaje2(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(3, 2, 'H', 'SALVARAN')
        self.assertEqual((tablero.returnPointsAndMultiplier()), 36)


    def testVerticalPuntaje(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H', 'ARASAKA')
        self.assertEqual(tablero.returnPointsAndMultiplier(), 20)
        
    def testVerticalPuntaje2(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 5, 'V', 'SILVERHAND')
        self.assertEqual(tablero.returnPointsAndMultiplier(), 25)

    def testVerticalPuntaje3(self): 
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 0, 'V', 'TOKYO')
        self.assertEqual(tablero.returnPointsAndMultiplier(), 28)

    def testVerticalAndHorizontal(self): 
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'V', 'ARASAKA')
        self.assertEqual(tablero.returnPointsAndMultiplier(), 30)
        tablero.writeInBoard(0, 2, 'H', 'ARASAKA')
        self.assertEqual(tablero.returnPointsAndMultiplier(), 20)



if __name__ == '__main__':
    unittest.main()
