from game.models import BagTiles
class TilesOutOfRange(Exception):
    pass

class Player:
    def __init__(self):
        self.score = 0
        self.tiles = []
        self.turn = False
        
    def startTurn(self):
        self.turn = True

    def endTurn(self):
        self.turn = False


                
# branch
