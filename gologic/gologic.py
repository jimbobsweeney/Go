'''
Created on 26 Oct 2012

@author: BAM
'''
#Set up exceptions
class go_logic_error(Exception): pass
class bad_board_size_error(go_logic_error): pass
class bad_stone_order_error(go_logic_error): pass
class position_xy_out_of_range_error(go_logic_error): pass
class position_occupied_error(go_logic_error): pass

#function to return von neumann neighbourhood of a position
def get_von_neumann(position):
    x = position[0]
    y = position[1]
    return [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]


class game():
    def __init__(self,size):
        self.gameboard = board(size)
        self.groups = []
        
    """Check for adjacent groups when placing a stone"""
    def check_for_group(self,move):
        for i in get_von_neumann(move.position): #iterate through von neumann neighbourhood of proposed stone placement position
            for group in self.groups: #iterate through all groups
                is_adjacent = False
                for position in group.positions: #iterate through all positions in each group
                    while is_adjacent == False:
                        if move.colour == group.colour and x == postition[0] and y == position[1]:
                            move.adjacent_groups.append(group)
                            is_adjacent = True 
        
        
class move():
    def __init__(self,position,colour):
        self.position = position
        self.colour = colour
        self.adjacent_groups = []
                
"""Board class contins 2d list of positions"""
class board():
    def __init__(self,size):
        if size < 2: 
            raise bad_board_size_error,'Board size cannot be less than 2'
        self.grid = {}
        for x in range(size):
            for y in range(size):
                self.grid[(x,y)] = None   
    
    """add stone to board"""
    def add_stone(self,position,colour,order):
        if position not in self.grid:
            raise position_xy_out_of_range_error,'position does not exist'
        if self.grid[position] != None:
            raise position_occupied_error,'position is already occupied by a stone'  
        self.grid[position] = stone(colour,order)

""" Stone class is very simple, just records colour and order placed"""  
class stone():
    def __init__(self,colour,order):
        if order < 0: 
            raise bad_stone_order_error,'Stone order cannot be less than 0'
        self.colour = colour
        self.order = order

  
class group():
    def __init__(self,position,colour):
        self.colour = colour
        self.positions = [position]
     
    """function to check if group is alive, if it finds one liberty it stops looking 
    if it completes the loop without finding any then the group is dead 
    The only relevant quantities of liberties a group can have are '0' or 'more than 0'"""  
    def am_i_alive(self,grid):
        for position in self.positions: #iterate through all positions in group
            for vn_position in get_von_neumann(position): #check von neumann neighbourhood of each one
                if vn_position in grid: #check if neighbour cell is actually on board
                        if grid[vn_position] == None:
                            return True
        return False

    def addposition(self):
        pass
    
    def die(self):
        pass


if __name__ == '__main__':
    testboard = board(13)
    testboard.grid[(1,0)]= stone(0,0)
    testboard.grid[(0,1)]= stone(0,0)
    testgroup = group((0,0),0)
    print testgroup.am_i_alive(testboard.grid)
    pass