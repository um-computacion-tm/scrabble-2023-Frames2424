import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
    def __repr__(self):
        return f"({self.letter}, {self.value})"

class BagTiles:
    def __init__(self):
        self.tiles = []
        for _ in range(12):
            self.tiles.append(Tile('A', 1))
            self.tiles.append(Tile('E', 1))
        for _ in range(9):
            self.tiles.append(Tile('O', 1))
        for _ in range(6):
            self.tiles.append(Tile('I', 1))
            self.tiles.append(Tile('S', 1))                         
        for _ in range(5):
            self.tiles.append(Tile('N', 1))            
            self.tiles.append(Tile('R', 1))
            self.tiles.append(Tile('U', 1))
            self.tiles.append(Tile('D', 2)) 
        for _ in range(4):
            self.tiles.append(Tile('L', 1))
            self.tiles.append(Tile('T', 1))
            self.tiles.append(Tile('C', 3))
        for _ in range(2):
            self.tiles.append(Tile('B', 3))
            self.tiles.append(Tile('M', 3))
            self.tiles.append(Tile('P', 3))
            self.tiles.append(Tile('G', 2))
            self.tiles.append(Tile('H', 4))
            self.tiles.append(Tile(' ', 0))
        self.tiles.append(Tile('F', 4))
        self.tiles.append(Tile('V', 4))
        self.tiles.append(Tile('Y', 4))
        self.tiles.append(Tile('Ch', 5))
        self.tiles.append(Tile('Q', 5))
        self.tiles.append(Tile('J', 8))
        self.tiles.append(Tile('LL', 8))
        self.tiles.append(Tile('Ñ', 8))
        self.tiles.append(Tile('RR', 8))
        self.tiles.append(Tile('X', 8))
        self.tiles.append(Tile('Z', 10))                    
        random.shuffle(self.tiles)

    def shuffle_bag(self):
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        if count > len(self.tiles):
            count = len(self.tiles)
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
        

