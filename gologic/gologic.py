'''
Created on 26 Oct 2012

@author: BAM
'''

import copy

"""Set up exceptions"""
class go_logic_error(Exception): pass
class bad_board_size_error(go_logic_error): pass
class bad_stone_order_error(go_logic_error): pass
class position_xy_out_of_range_error(go_logic_error): pass
class position_occupied_error(go_logic_error): pass

"""function to return von neumann neighbourhood of a position"""
def get_von_neumann(position):
    x = position[0]
    y = position[1]
    return [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]


class game():
    def __init__(self,size):
        self.order = 1
        self.dead_stones = [0,0]
        self.gameboard = board(size)
        self.groups = []
        
    """Check for adjacent groups when placing a stone, Stones know which group they are in so this function is now very efficient
    Only the Von Neumann neoghbourhood of a move is checked to find which groups will be affected by the move
    There is a maximum of only four iterations and any irrelevant groups or positions in a group are not considered"""
    def check_for_group(self,move):
        for movepos in get_von_neumann(move.position): #iterate through von neumann neighbourhood of proposed stone placement position
            if self.gameboard.grid[(movepos)] != None:
                group = self.gameboard.grid[(movepos)].my_group
                if group not in move.adjacent_groups and group not in move.adjacent_op_groups:
                    if move.colour == group.colour:
                        move.adjacent_groups.append(group)
                    else:
                        move.adjacent_op_groups.append(group)
    
    def merge_groups(self,groups): 
        first = True
        for group in groups:
            if first == True:
                mergegroup = group
                first = False
            else:
                for position in group.positions:
                    mergegroup.add_position(position,self.gameboard.grid)
                self.groups.remove(group)
    
    def kill_group(self,group):
        score = 0
        for position in group.positions:
            score = score + 1
            self.gameboard.grid[position] = None
        self.groups.remove(group)
        self.dead_stones[group.colour] = self.dead_stones[group.colour] + score
    
    """High lvl function to make a move. First the move is simulated on a copy of the game"""
    def make_a_move(self,move):
        sim_game = copy.deepcopy(self)
        sim_game.check_for_group(move)
        if len(move.adjacent_groups) > 0:
            sim_game.merge_groups(move.adjacent_groups)
            #sim_game.groups[move]
                
        else: 
            sim_game.groups.append(group(move.position,move.colour))
            
        sim_game.gameboard.add_stone(move.position,move.colour,sim_game.order)
        sim_game.order = sim_game.order + 1
        for group in sim_game.groups: group.am_i_alive(sim_game.gameboard.grid)
    
    
class move():
    def __init__(self,position,colour):
        self.position = position
        self.colour = colour
        self.adjacent_groups = []
        self.adjacent_op_groups = []
                
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
        self.my_group = None

  
class group():
    def __init__(self,position,colour,grid):
        self.colour = colour
        self.positions = [position]
        grid[position].my_group = self
     
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

    def add_position(self,position,grid):
        self.positions.append(position)
        grid[position].my_group = self

if __name__ == '__main__':
    """
    testboard = board(13)
    testboard.grid[(1,0)]= stone(0,0)
    testboard.grid[(0,1)]= stone(0,0)
    testgroup = group((0,0),0)
    print testgroup.am_i_alive(testboard.grid)
    """
    pass