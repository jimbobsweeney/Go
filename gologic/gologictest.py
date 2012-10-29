'''
Created on 26 Oct 2012

@author: BAM
'''

import unittest
import gologic

#test for my classes
class class_tests(unittest.TestCase):pass

#test my game class
class game_tests(class_tests):
    
    #test game constructor
    def test_new_game(self):
        self.testgame = gologic.game(13)
        assert self.testgame.gameboard.grid[(12,12)] == None
        with self.assertRaises(KeyError):
            print (self.testgame.gameboard.grid[(13,0)])
        with self.assertRaises(KeyError):
            print (self.testgame.gameboard.grid[(-1,0)])
        assert self.testgame.groups == []
        self.testgame.dead_stones[1] = 10
    
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group(self):
        self.testgame = gologic.game(19)
        self.testgame.groups.append(gologic.group((5,5),0)) 
        self.testmove = gologic.move((4,5),0)
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 1,"There should be one adjacent group to this move"
        self.testgame.groups.append(gologic.group((3,5),1))
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_op_groups) == 1,"There should be one adjacent opponent group to this move" 
        
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group_2(self):
        self.testgame = gologic.game(19)
        self.testgame.groups.append(gologic.group((5,5),0)) 
        self.testgame.groups.append(gologic.group((3,5),0)) 
        self.testgame.groups.append(gologic.group((4,6),0)) 
        self.testgame.groups.append(gologic.group((4,4),0))
        self.testmove = gologic.move((4,5),0) 
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 4,"There should be 4 adjacent groups to this move"
      
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group_3(self):
        self.testgame = gologic.game(19)
        self.testgame.groups.append(gologic.group((5,5),0))
        self.testgame.groups[0].add_position((4,4))
        self.testgame.groups[0].add_position((5,4))
        self.testgame.groups[0].add_position((3,4))
        self.testgame.groups[0].add_position((3,5))      
        self.testmove = gologic.move((4,5),0)
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 1,"There should be one adjacent group to this move"  
  
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group_4(self):
        self.testgame = gologic.game(19)
        self.testgame.groups.append(gologic.group((5,5),0))
        self.testgame.groups[0].add_position((4,4))
        self.testgame.groups[0].add_position((5,4))
        self.testgame.groups.append(gologic.group((3,4),0))
        self.testgame.groups[1].add_position((3,5)) 
        self.testgame.groups.append(gologic.group((4,6),0))     
        self.testmove = gologic.move((4,5),0)
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 3,"There should be 3 adjacent groups to this move" 
 
    #test the merge group function
    def test_merge_group(self):
        self.testgame = gologic.game(30)
        self.testgame.groups.append(gologic.group((5,5),0))
        self.testgame.groups[0].add_position((4,4))
        self.testgame.groups[0].add_position((5,4))
        self.testgame.groups.append(gologic.group((3,4),0))
        self.testgame.groups[1].add_position((3,5)) 
        self.testgame.groups.append(gologic.group((4,6),0))
        self.testmergelist = [self.testgame.groups[0],self.testgame.groups[1],self.testgame.groups[2]]
        self.testgame.merge_groups(self.testmergelist)
        assert len(self.testgame.groups) == 1,"Should only be one group after this merge"
        
    #test the kill group function
    def test_kill_group(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((5,5),1,15)
        self.testgame.gameboard.add_stone((4,4),1,15)
        self.testgame.gameboard.add_stone((5,4),1,15)
        self.testgame.groups.append(gologic.group((5,5),1))
        self.testgame.groups[0].add_position((4,4))
        self.testgame.groups[0].add_position((5,4))
        assert len(self.testgame.groups) == 1,"There should be 1 group"
        print self.testgame.dead_stones[0]
        self.testgame.kill_group(self.testgame.groups[0])
        assert len(self.testgame.groups) == 0,"There should be 0 groups after killing group"
        for position, value in self.testgame.gameboard.grid.items():
            assert value == None,"Board should be empty"
        
    #test make a move function
    def test_make_a_move(self):
        self.testgame = gologic.game(19)
        self.testmove = gologic.move((5,5),0)
        self.testgame.make_a_move(self.testmove)
        assert len(self.testgame.groups) == 1,"There should be 1 group"
        #assert self.testgame.gameboard.grid == 1,"There should be 1 group"
        
        
#test my board class
class board_tests(class_tests):
    
    #test new board instantiation    
    def test_new_board(self):
        self.testboard = gologic.board(19)
        assert self.testboard.grid[(0,0)] == None
        assert self.testboard.grid[(18,18)] == None
     
    #test bad board size    
    def test_bad_board_size(self):
        with self.assertRaises(gologic.bad_board_size_error):
            self.testboard = gologic.board(-5)
        
    #test out of range stone placement, less than zero and greater than gridsize in x and y    
    def test_position_xy_out_of_range(self):
        self.testboard = gologic.board(19)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone((-1,0),1,15)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone((5,-1),1,15)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone((19,0),1,15)
        with self.assertRaises(gologic.position_xy_out_of_range_error):
            self.testboard.add_stone((5,19),1,15)

    #test add_stone in already occupied position  
    def test_position_occupied(self):
        self.testboard = gologic.board(19)
        with self.assertRaises(gologic.position_occupied_error):
            self.testboard.add_stone((0,0),1,15)
            self.testboard.add_stone((0,0),0,16)


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
        self.testgroup = gologic.group((3,5),0)
        assert self.testgroup.positions[0][0] == 3 , "x position should be 3"
        assert self.testgroup.positions[0][1] == 5 , "y position should be 5"
       
    #test am_i_alive function    
    def test_am_i_alive(self):
        self.testboard = gologic.board(13)
        self.testgroup = gologic.group((3,3),0)
        assert self.testgroup.am_i_alive(self.testboard.grid) == True, "group should have more than 0 liberties"
         
        self.testgroup2 = gologic.group((0,0),0)
        self.testboard.grid[(1,0)] = gologic.stone(1,2)
        self.testboard.grid[(0,1)] = gologic.stone(1,3)
        assert self.testgroup2.am_i_alive(self.testboard.grid) == False, "group should have 0 liberties"
     
        self.testgroup3 = gologic.group((10,10),0)
        self.testboard.grid[(11,10)] = gologic.stone(1,2)
        self.testboard.grid[(9,10)] = gologic.stone(1,3)
        self.testboard.grid[(10,11)] = gologic.stone(1,4)
        self.testboard.grid[(10,9)] = gologic.stone(1,5)
        assert self.testgroup3.am_i_alive(self.testboard.grid) == False, "group should have 0 liberties"
 
    #test am_i_alive function    
    def test_am_i_alive2(self):
        self.testgame = gologic.game(9)
        self.testgame.groups.append(gologic.group((5,5),0))
        self.testgame.groups[0].add_position((4,4))
        assert self.testgame.groups[0].am_i_alive(self.testgame.gameboard.grid) == True, "group should have more than 0 liberties"
 
    #test am_i_alive function    
    def test_am_i_alive3(self):
        self.testgame = gologic.game(9)
        self.testgame.groups.append(gologic.group((4,5),0))
        self.testgame.groups[0].add_position((4,4))
        self.testgame.gameboard.add_stone((4,4),0,15)
        self.testgame.gameboard.add_stone((4,5),0,16)
        self.testgame.gameboard.add_stone((4,3),1,17)
        self.testgame.gameboard.add_stone((4,6),1,18)
        self.testgame.gameboard.add_stone((3,4),1,19)
        self.testgame.gameboard.add_stone((3,5),1,20)
        self.testgame.gameboard.add_stone((5,4),1,21)
        self.testgame.gameboard.add_stone((5,5),1,22)
        assert self.testgame.groups[0].am_i_alive(self.testgame.gameboard.grid) == False, "group should have 0 liberties"
 
#test my move class
class move_tests(class_tests):
    
    #test new move instantiation    
    def test_new_move(self):
        self.testmove = gologic.move((5,5),0)
        assert self.testmove.position == (5,5)
        assert self.testmove.colour == 0
        assert self.testmove.adjacent_groups == []


if __name__ == "__main__":
    unittest.main()    