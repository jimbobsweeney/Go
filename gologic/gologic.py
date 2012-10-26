'''
Created on 26 Oct 2012

@author: BAM
'''
#Set up exceptions
class go_logic_error(Exception): pass
class bad_board_size_error(go_logic_error): pass
class bad_stone_order_error(go_logic_error): pass
class stone_xy_out_of_range_error(go_logic_error): pass

class game():
    def __init__(self,size):
        self.gameboard = board(size)
        self.groups = []


class board():
    def __init__(self,size):
        if size < 2: 
            raise bad_board_size_error,'Board size cannot be less than 2'
        self.grid = [[None]*size for _ in range(size)] 
        
    def add_stone(self,x,y,colour,order):
        if x > len(self.grid)-1 or x < 0 or y > len(self.grid[0])-1 or y < 0:
            raise stone_xy_out_of_range_error,'position does not exist'
        self.grid[x][y] = stone(colour,order)

  
class stone():
    def __init__(self,colour,order):
        if order < 0: 
            raise bad_stone_order_error,'Stone order cannot be less than 0'
        self.colour = colour
        self.order = order

  
class group():
    def __init__(self,position):
        self.grid = [position] 


if __name__ == '__main__':
    pass