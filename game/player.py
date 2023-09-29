class Player:
    def __init__(self):
        self.score = 0
        self.rack = []
        self.turn = False
    def startTurn(self):
        self.turn = True
    def endTurn(self):
        self.turn = False
    def sumScore(self, board):
        self.score += board.puntosActuales