import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        tablero = Board()
        self.assertEqual((tablero.board),[])

    def testTableroInicial(self):
        tablero = Board()
        tablero.initialBoard()
        self.assertEqual((tablero.board),[
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','4'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','*','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
])
    
    def testTableroConPalabrasGrafico(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 0, 'V', 'ARASAKA')
        self.assertEqual((tablero.board),[
    ['A','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
    ['R','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['A','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['S','*','*','1','*','*','*','4','*','*','*','1','*','*','*'],
    ['A','*','*','*','1','*','*','*','*','*','1','*','*','*','4'],
    ['K','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['A','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','*','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
])
                
    def testValidarEnVertical(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'V','ARASAKA')
        self.assertEqual((tablero.verifyVerticalWord('ARASAKA')), True)

    def testValidarEnVerticalFalso(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H','ARASAKA')
        self.assertEqual((tablero.verifyVerticalWord('CASA')), None)

    def testValidarEnHorizontal(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H', 'ARASAKA')
        self.assertEqual((tablero.verifyHorizontalWord('ARASAKA')), True)

    def testValidarEnHorizontalFalso(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H','ARASAKA')
        self.assertEqual((tablero.verifyHorizontalWord('AROSAKO')), None)

    def testListaDePuntaje_I(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H', 'ARASAKA')
        self.assertEqual((tablero.board),[
    ['0','*','A','R','A','S','A','K','A','*','*','4','*','*','0'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','4'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','*','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
])
        self.assertEqual((tablero.wordPoints), [1, 2, 1, 1, 1, 3, 1])

    def testListaDePuntajeAndDefCurrentWords(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 2, 'H','ARASAKA')
        tablero.writeInBoard(0, 5, 'V','SILVERHAND')
        self.assertEqual((tablero.board),[
    ['0','*','A','R','A','S','A','K','A','*','*','4','*','*','0'],
    ['*','1','*','*','*','I','*','*','*','5','*','*','*','1','*'],
    ['*','*','1','*','*','L','4','*','4','*','*','*','1','*','*'],
    ['4','*','*','1','*','V','*','4','*','*','*','1','*','*','*'],
    ['*','*','*','*','1','E','*','*','*','*','1','*','*','*','4'],
    ['*','5','*','*','*','R','*','*','*','5','*','*','*','5','*'],
    ['*','*','4','*','*','H','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','A','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','N','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','D','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
])
        self.assertEqual((tablero.wordCurrentPoints()), [1, 3, 1, 4, 1, 3, 4, 1, 1, 6])

    def testListaDePuntajeAndDefCurrentWordsHorizontal(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(5, 0, 'H', 'CAFE')
        self.assertEqual((tablero.wordCurrentPoints()), [3, 3, 4, 1])

    def testMismaLetraEnHorizontal(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.writeInBoard(0, 5, 'V', 'SILVERHAND')
        tablero.writeInBoard(0, 2, 'H','ARASAKA')
        self.assertEqual((tablero.board),[
    ['0','*','A','R','A','S','A','K','A','*','*','4','*','*','0'],
    ['*','1','*','*','*','I','*','*','*','5','*','*','*','1','*'],
    ['*','*','1','*','*','L','4','*','4','*','*','*','1','*','*'],
    ['4','*','*','1','*','V','*','4','*','*','*','1','*','*','*'],
    ['*','*','*','*','1','E','*','*','*','*','1','*','*','*','4'],
    ['*','5','*','*','*','R','*','*','*','5','*','*','*','5','*'],
    ['*','*','4','*','*','H','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','A','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','N','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','D','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
])
        




if __name__ == '__main__':
    unittest.main()
