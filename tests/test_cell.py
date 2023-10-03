import unittest
# from game.cell import Cell
from game.models import Tile
from game.board import Board



class TestCell(unittest.TestCase):
    def testHorizontalPuntaje(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'V', 'TORNADO')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.wordCurrentPointsNumber(), 30)


    def testHorizontalPuntaje2(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(5, 0, 'H', 'PISO')
        tablero.returnPointsAndMultiplier()
        self.assertEqual((tablero.wordCurrentPointsList()), [3, 3, 4, 1])
        self.assertEqual(tablero.wordCurrentPointsNumber(), 11)


    def testHorizontalPuntaje2(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(3, 2, 'H', 'SALVAJES')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.wordCurrentPointsNumber(), 36)


    def testVerticalPuntaje(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H', 'TORNADO')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.puntosActuales, 20)
    
        
    def testVerticalPuntaje2(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 5, 'V', 'NXLTORNADO')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.puntosActuales, 25)


    def testVerticalPuntaje3(self): 
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 0, 'V', 'HONDA')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.puntosActuales, 28)


    def testVerticalAndHorizontal(self): 
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'V', 'TORNADO')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.puntosActuales, 30)
        tablero.writeInBoard(0, 2, 'H', 'TORNADO')
        tablero.returnPointsAndMultiplier()
        self.assertEqual(tablero.puntosActuales, 20)



if __name__ == '__main__':
    unittest.main()