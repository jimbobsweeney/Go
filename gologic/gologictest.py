'''
Created on 26 Oct 2012

@author: BAM
'''

import unittest
import gologic

#test for my classes
class class_tests(unittest.TestCase):pass

#test my board class
class board_tests(class_tests):
    
    #test new board instantiation    
    def test_new_board(self):
        self.testboard = gologic.board(19)
        assert self.testboard.grid[0][0] == None
        assert self.testboard.grid[18][18] == None
        
    #test bad board size    
    def test_bad_board_size(self):
        with self.assertRaises(gologic.bad_board_size_error):
            self.testboard = gologic.board(-5)
            
    #test out of range stone placement, less than zero and greater than gridsize in x and y    
    def test_position_xy_out_of_range(self):
        self.testboard = gologic.board(19)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone(-1,0,1,15)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone(5,-1,1,15)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone(19,0,1,15)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone(5,19,1,15)

    #test add_stone in already occupied position  
    def test_position_occupied(self):
        self.testboard = gologic.board(19)
        with self.assertRaises(gologic.position_occupied_error):
            self.testboard.add_stone(0,0,1,15)
            self.testboard.add_stone(0,0,0,16)


#test my stone class
class stone_tests(class_tests):
    
    #test new stone instantiation    
    def test_new_stone(self):
        self.teststone = gologic.stone(0,15)
        assert self.teststone.colour == 0
        assert self.teststone.order == 15
        
    #test bad stone order    
    def test_bad_stone_order(self):
        with self.assertRaises(gologic.bad_stone_order_error):
            self.teststone = gologic.stone(0,-2)

#test my group class
class group_tests(class_tests):
        
    #test new group    
    def test_new_group(self):
        self.testgroup = gologic.group(3,5,0)
        assert self.testgroup.positions[0][0] == 3 , "x position should be 3"
        assert self.testgroup.positions[0][1] == 5 , "y position should be 5"
        
    #test am_i_alive function    
    def test_am_i_alive(self):
        self.testboard = gologic.board(13)
        self.testgroup = gologic.group(3,3,0)
        assert self.testgroup.am_i_alive(self.testboard.grid) == True, "group should have more than 0 liberties"
        
        self.testgroup2 = gologic.group(0,0,0)
        self.testboard.grid[1][0] = gologic.stone(1,2)
        self.testboard.grid[0][1] = gologic.stone(1,3)
        assert self.testgroup2.am_i_alive(self.testboard.grid) == False, "group should have 0 liberties"
        
        self.testgroup3 = gologic.group(10,10,0)
        self.testboard.grid[11][10] = gologic.stone(1,2)
        self.testboard.grid[9][10] = gologic.stone(1,3)
        self.testboard.grid[10][11] = gologic.stone(1,4)
        self.testboard.grid[10][9] = gologic.stone(1,5)
        assert self.testgroup3.am_i_alive(self.testboard.grid) == False, "group should have 0 liberties"

if __name__ == "__main__":
    unittest.main()    