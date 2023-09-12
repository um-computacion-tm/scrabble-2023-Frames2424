import unittest
from game.dictionary import Dictionary
from game.scrabble import ScrabbleGame


class TestCell(unittest.TestCase):
    def testTrue(self):
        diccionario = Dictionary()
        self.assertEqual((diccionario.isValid('SI')), True)

    def testFalse(self):
        diccionario = Dictionary()
        self.assertEqual((diccionario.isValid('NO')), False)

    def testNotTrueNotFalse(self):
        diccionario = Dictionary()
        self.assertEqual((diccionario.isValid('BICICLETA')), None)
