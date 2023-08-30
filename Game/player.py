from game.models import BagTiles
class TilesOutOfRange(Exception):
    pass

class Player:
    def __init__(self):
        self.score = 0
        self.tiles = []
        self.turn = False

    def getTiles(self, cant, bag = BagTiles):
        if cant  > 0 and cant <= 7:
            if cant + len(self.tiles) <= 7:
                for k in range(cant):
                    self.tiles.append(bag.take(1))
            else: 
                raise TilesOutOfRange()
        else: 
            raise TilesOutOfRange()

    def startTurn(self):
        self.turn = True

    def endTurn(self):
        self.turn = False


                
