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
            raise position_xy_out_of_range_error,'position does not exist'
        if self.grid[x][y] != None:
            raise position_occupied_error,'position is already occupied by a stone'  
        self.grid[x][y] = stone(colour,order)

  
class stone():
    def __init__(self,colour,order):
        if order < 0: 
            raise bad_stone_order_error,'Stone order cannot be less than 0'
        self.colour = colour
        self.order = order

  
class group():
    def __init__(self,x,y,colour):
        self.colour = colour
        self.positions = [[x,y]]
     
    """function to check if group is alive, if it finds one liberty it stops looking 
    if it completes the loop without finding any then the group is dead 
    The only relevant quantities of liberties a group can have are '0' or 'more than 0'"""  
    def am_i_alive(self,grid):
        for position in self.positions:
            x = position[0]
            y = position[1]
            for i in [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]:
                if i[0] > 0 and i[1] > 0:
                    if grid[i[0]] in grid:
                        #print i[0]
                        if grid[i[0]][i[1]] in grid[i[0]]:
                            print i
                            print grid[i[0]][i[1]]
                            if grid[i[0]][i[1]] == None:
                                return True
        return False

    def addposition(self):
        pass
    
    def die(self):
        pass


if __name__ == '__main__':
    testboard = board(13)
    testboard.grid[1][0]= stone(0,0)
    testboard.grid[0][1]= stone(0,0)
    testgroup = group(0,0,0)
    print testgroup.am_i_alive(testboard.grid) 
    pass