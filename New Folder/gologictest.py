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
        

if __name__ == "__main__":
    unittest.main()    