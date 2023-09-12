from game.models import BagTiles, Tile


class Board:
    def __init__(self):
        self.board = []
        self.wordPoints = []

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
    
    def writeVerticalWord(self, startX, startY, word):
        self.wordPoints = []
        values = BagTiles().tiles
        for letter in word:
            if self.board[startX][startY] == '4':
                self.board[startX][startY] = letter
                self.wordPoints.append(values[letter] * 2)
                startX += 1
            elif self.board[startX][startY] == '5':
                self.board[startX][startY] = letter
                self.wordPoints.append(values[letter] * 3)
                startX += 1
            elif self.board[startX][startY] == '*'  or (self.board[startX][startY] == '0' or '1' or letter):
                if self.board[startX][startY] != letter:
                    self.board[startX][startY] = letter
                    self.wordPoints.append(values[letter])
                    startX += 1
                else:
                    self.wordPoints.append(values[letter])
                    startX += 1

    def writeHorizontalWord(self, startX, startY, word):
        self.wordPoints = []
        values = BagTiles().tiles
        for letter in word:
            if self.board[startX][startY] == '4':
                self.board[startX][startY] = letter
                self.wordPoints.append(values[letter] * 2)
                startY += 1
            elif self.board[startX][startY] == '5':
                self.board[startX][startY] = letter
                self.wordPoints.append(values[letter] * 3)
                startY += 1
            elif self.board[startX][startY] == '*'  or (self.board[startX][startY] == '0' or '1' or letter):
                if self.board[startX][startY] != letter:
                    self.board[startX][startY] = letter
                    self.wordPoints.append(values[letter])
                    startY += 1
                else:
                    self.wordPoints.append(values[letter])
                    startY += 1

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

# branch