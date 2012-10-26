'''
Created on 26 Oct 2012

@author: BAM
'''
#Set up exceptions
class go_logic_error(Exception): pass
class bad_board_size_error(go_logic_error): pass
class bad_stone_order_error(go_logic_error): pass


class board():
    def __init__(self,size):
        if size < 2: 
            raise bad_board_size_error,'Board size cannot be less than 2'
        self.grid = [[None]*size for _ in range(size)] 

  
class stone():
    def __init__(self,colour,order):
        if order < 0: 
            raise bad_stone_order_error,'Stone order cannot be less than 0'
        self.colour = colour
        self.order = order
  

if __name__ == '__main__':
    pass