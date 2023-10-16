#Importar recordar actualizar tiles
from game.Tiles import *

class Player:
    def __init__(self):
        self.tiles = []
        self.name = None
        self.score = 0
    
    
    def letters_str(self, tiles_group, match): 
        tiles_group = tiles_group.upper()
        for i in self.tiles:
            if i.letter in match:
                match[i.letter] += 1
            else:
                match[i.letter] = 1 
        for j in tiles_group:
            if j in match and match[j] >= 1:
                match[j] -= 1
            else:
                return False
            
        return True   
    
    def letters_tile(self, tiles_group, match):
        for i in self.tiles:
            if i.letter in match:
                match[i.letter] += 1
            else:
                match[i.letter] = 1 
        for j in tiles_group:
            if j.letter in match and match[j.letter] >= 1:
                match[j.letter] -= 1
            else:
                return False
            
        return True
    
    def letters(self, tiles_group):
        match = {}    
        if isinstance(tiles_group, str):    
            return self.letters_str(tiles_group, match)      
        else:       
            return self.letters_tile(tiles_group, match)
    
    def exchange_tile(self, bag:BagTiles, tile_exchange):
        for i in range(len(self.tiles)):
            if self.tiles[i] == tile_exchange:
                popped = self.tiles.pop(i)
                bag.put([popped])
                break
        bag.shuffle_bag()
        self.tiles.extend(bag.take(1))  
                
    def remove_tile(self, tile:Tile):
        for i in self.tiles:
            if i.letter == tile.letter:
                self.tiles.remove(i)
                break           
                    
                    
        
        
       
    
