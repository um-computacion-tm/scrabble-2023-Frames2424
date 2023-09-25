from game.models import BagTiles, Tile


class Board:
    def __init__(self):
        self.board = []
        self.wordPoints = []
        self.condicionCero = False
        self.condicionUno = False

    def initialBoard(self):
        initialBoard = [
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
]
        self.board = initialBoard

    def mostrarTableroActual(self):
        for fila in self.board:
            print(fila)
    
    def wordCurrentPoints(self):
        return self.wordPoints

    def initVariables(self):
        self.wordPoints = []
        self.condicionCero = False
        self.condicionUno = False

    def appendValuesInWordPoints(self, letter, multiplier):
        values = BagTiles().tiles
        self.wordPoints.append(values[letter] * multiplier)
    
    def writeInBoard(self, startX, startY, direction, word):
        self.initVariables()
        for letter in word:
            if self.board[startX][startY] == '4':
                self.board[startX][startY] = letter
                self.appendValuesInWordPoints(letter, 2)

            elif self.board[startX][startY] == '5':
                self.board[startX][startY] = letter
                self.appendValuesInWordPoints(letter, 3)


            elif self.board[startX][startY] == '0':
                self.board[startX][startY] = letter
                self.appendValuesInWordPoints(letter, 1)
                self.condicionCero = True


            elif self.board[startX][startY] == '1':
                self.board[startX][startY] = letter
                self.appendValuesInWordPoints(letter, 1)
                self.condicionUno = True

            elif self.board[startX][startY] == '*'  or letter:
                if self.board[startX][startY] != letter:
                    self.board[startX][startY] = letter
                    self.appendValuesInWordPoints(letter, 1)
                else:
                    self.appendValuesInWordPoints(letter, 1)
                    
            if direction == 'H':
                startY += 1    
            if direction == 'V':
                startX += 1

    def verifyVerticalWord(self, palabra):
        for k in range(15):
            columna_to_string = ''.join(fila[k] for fila in self.board)
            index = columna_to_string.find(palabra)
            if index != -1:
                return True
            else:
                continue

    def verifyHorizontalWord(self, palabra):
        for j in range(15):
            row_to_string = ''.join(str(elemento) for elemento in self.board[j])
            index = row_to_string.find(palabra)
            if index != -1:
                return True
            else:
                continue


    def returnPointsAndMultiplier(self):
        simple = sum(self.wordPoints)
        if self.condicionCero == True:
            return simple * 2
        
        if self.condicionUno == True:
            return simple * 3
        
        else: 
            return simple
