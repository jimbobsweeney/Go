'''
Created on 26 Oct 2012

@author: BAM
'''

import unittest
import gologic

#test for my classes
class class_tests(unittest.TestCase):pass


#test my interface class
class interface_tests(class_tests):
    
    #play test game
    def test_gameplay(self):
        test_interface = gologic.interface()
        test_interface.newgame(13)
        test_interface.try_move((2,2))#black
        test_interface.try_move((2,1))#white
        test_interface.try_move((2,3))#black
        assert len(test_interface.game.groups) == 2,"should be 2 groups now"
        test_interface.try_move((2,0))#white
        assert len(test_interface.game.groups) == 2,"should be 2 groups now"
        test_interface.try_move((1,1))#black
        assert len(test_interface.game.groups) == 3,"should be 3 groups now"
        test_interface.pass_turn()
        test_interface.try_move((1,0))
        test_interface.pass_turn()
        test_interface.try_move((3,1))
        test_interface.pass_turn()
        test_interface.try_move((3,0))
        assert len(test_interface.game.groups) == 3,"should be 3 groups now"
        assert test_interface.game.dead_stones[1] == 2,"should be 2 dead white stones"
        test_interface.pass_turn()
        test_interface.try_move((2,1))
        assert len(test_interface.game.groups) == 1,"should be 1 group now"
        assert len(test_interface.game.groups[0].positions) == 7,"Group should have 7 stones in it"
     
    #play test game
    def test_gameplay_the_ladder(self):
        test_interface = gologic.interface()
        test_interface.newgame(13)
        test_interface.try_move((4,3))#black
        test_interface.try_move((3,3))#white
        test_interface.try_move((4,2))
        test_interface.pass_turn()
        test_interface.try_move((3,4))
        test_interface.pass_turn()
        test_interface.try_move((2,3))
        test_interface.try_move((3,2))
        test_interface.try_move((3,1))
        test_interface.try_move((2,2))
        test_interface.try_move((1,2))
        test_interface.try_move((2,1))
        test_interface.try_move((2,0))
        test_interface.try_move((1,1))
        test_interface.try_move((0,1))
        test_interface.try_move((1,0))
        test_interface.try_move((0,0))
        assert test_interface.game.dead_stones[1] == 6,"should be 6 dead white stones"
        for group in test_interface.game.groups: assert group.colour == 0,"All groups should be black"
        assert len(test_interface.game.groups) == 7,"should be 7 groups now"
        
    #play test game
    def test_gameplay_multikill(self):
        test_interface = gologic.interface()
        test_interface.newgame(19)
        test_interface.pass_turn()
        test_interface.try_move((3,1))#white
        test_interface.try_move((3,2))#black
        test_interface.try_move((2,2))
        test_interface.try_move((2,3))
        test_interface.try_move((1,3))
        test_interface.try_move((3,4))
        test_interface.try_move((2,4))
        test_interface.try_move((4,3))
        test_interface.try_move((3,5))
        test_interface.pass_turn()
        test_interface.try_move((4,4))
        test_interface.pass_turn()
        test_interface.try_move((5,3))
        test_interface.pass_turn()
        test_interface.try_move((4,2))
        test_interface.pass_turn()
        assert len(test_interface.game.groups) == 12,"should be 12 groups now"
        test_interface.try_move((3,3))
        assert len(test_interface.game.groups) == 9,"should be 9 groups now"
        assert test_interface.game.dead_stones[0] == 4,"should be 4 dead black stones"
        for group in test_interface.game.groups: assert group.colour == 1,"All groups should be white"
        test_interface.pass_turn()
        test_interface.try_move((2,3))
        assert len(test_interface.game.groups) == 6,"should be 6 groups now"
        
    #play test game
    def test_gameplay_corner(self):
        test_interface = gologic.interface()
        test_interface.newgame(9)
        test_interface.try_move((8,7))#black
        test_interface.try_move((8,8))#white
        test_interface.try_move((7,8))#black
        for group in test_interface.game.groups: assert group.colour == 0,"All groups should be black"
        assert len(test_interface.game.groups) == 2,"should be 2 groups now"
        
    #play test game
    def test_gameplay_box(self):
        test_interface = gologic.interface()
        test_interface.newgame(9)
        test_interface.try_move((2,2))#black
        test_interface.try_move((3,3))#white
        test_interface.try_move((2,3))#black
        test_interface.try_move((3,4))#white
        test_interface.try_move((2,4))#black
        test_interface.try_move((3,5))#white
        test_interface.try_move((2,5))#black
        test_interface.try_move((4,5))#white
        test_interface.try_move((2,6))#black
        test_interface.try_move((5,5))#white
        test_interface.try_move((3,6))#black
        test_interface.try_move((5,4))#white
        test_interface.try_move((4,6))#black
        test_interface.try_move((5,3))#white
        test_interface.try_move((5,6))#black
        test_interface.try_move((4,3))#white
        test_interface.try_move((6,6))#black
        test_interface.pass_turn()
        test_interface.try_move((6,5))#black
        test_interface.pass_turn()
        test_interface.try_move((6,4))#black
        test_interface.pass_turn()
        test_interface.try_move((6,3))#black
        test_interface.pass_turn()
        test_interface.try_move((6,2))#black
        test_interface.pass_turn()
        test_interface.try_move((5,2))#black
        test_interface.pass_turn()
        test_interface.try_move((4,2))#black
        test_interface.pass_turn()
        test_interface.try_move((3,2))#black
        assert len(test_interface.game.groups) == 2,"should be 2 groups now"
        test_interface.pass_turn()
        test_interface.try_move((4,4))#black
        assert test_interface.game.dead_stones[1] == 8,"should be 8 dead white stones"
        assert len(test_interface.game.groups) == 2,"should be 2 group now"
        for group in test_interface.game.groups: assert group.colour == 0,"All groups should be black"
        assert len(test_interface.game.groups[0].positions) == 16,"Group should have 16 stones in it"
        
    #play test game
    def test_illegal_move(self):
        test_interface = gologic.interface()
        test_interface.newgame(9)
        test_interface.try_move((1,8))#black
        test_interface.pass_turn()
        test_interface.try_move((0,7))#black
        legality = test_interface.try_move((0,8))#white
        assert legality == False
        
        
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
        self.testgame.gameboard.add_stone((5,5),0,1)
        self.testgame.groups.append(gologic.group((5,5),0,self.testgame.gameboard.grid)) 
        self.testmove = gologic.move((4,5),0)
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 1,"There should be one adjacent group to this move"
        self.testgame.gameboard.add_stone((3,5),1,1)
        self.testgame.groups.append(gologic.group((3,5),1,self.testgame.gameboard.grid))
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_op_groups) == 1,"There should be one adjacent opponent group to this move" 
      
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group_2(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((5,5),0,1)
        self.testgame.groups.append(gologic.group((5,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((3,5),0,1) 
        self.testgame.groups.append(gologic.group((3,5),0,self.testgame.gameboard.grid)) 
        self.testgame.gameboard.add_stone((4,6),0,1)
        self.testgame.groups.append(gologic.group((4,6),0,self.testgame.gameboard.grid)) 
        self.testgame.gameboard.add_stone((4,4),0,1)
        self.testgame.groups.append(gologic.group((4,4),0,self.testgame.gameboard.grid))
        self.testmove = gologic.move((4,5),0) 
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 4,"There should be 4 adjacent groups to this move"
       
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group_3(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((5,5),0,1)
        self.testgame.groups.append(gologic.group((5,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((4,4),0,1)
        self.testgame.groups[0].add_position((4,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((5,4),0,1)
        self.testgame.groups[0].add_position((5,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((3,4),0,1)
        self.testgame.groups[0].add_position((3,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((3,5),0,1)
        self.testgame.groups[0].add_position((3,5),self.testgame.gameboard.grid)      
        self.testmove = gologic.move((4,5),0)
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 1,"There should be one adjacent group to this move"  
  
    #test the check for adjacent groups to a proposed move function 
    def test_check_for_group_4(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((5,5),0,1)
        self.testgame.groups.append(gologic.group((5,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((4,4),0,1)
        self.testgame.groups[0].add_position((4,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((5,4),0,1)
        self.testgame.groups[0].add_position((5,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((3,4),0,1)
        self.testgame.groups.append(gologic.group((3,4),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((3,5),0,1)
        self.testgame.groups[1].add_position((3,5),self.testgame.gameboard.grid) 
        self.testgame.gameboard.add_stone((4,6),0,1)
        self.testgame.groups.append(gologic.group((4,6),0,self.testgame.gameboard.grid))     
        self.testmove = gologic.move((4,5),0)
        self.testgame.check_for_group(self.testmove)
        assert len(self.testmove.adjacent_groups) == 3,"There should be 3 adjacent groups to this move" 
 
    #test the merge group function
    def test_merge_group(self):
        self.testgame = gologic.game(30)
        self.testgame.gameboard.add_stone((5,5),0,1)
        self.testgame.groups.append(gologic.group((5,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((4,4),0,1)
        self.testgame.groups[0].add_position((4,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((5,4),0,1)
        self.testgame.groups[0].add_position((5,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((3,4),0,1)
        self.testgame.groups.append(gologic.group((3,4),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((3,5),0,1)
        self.testgame.groups[1].add_position((3,5),self.testgame.gameboard.grid) 
        self.testgame.gameboard.add_stone((4,6),0,1)
        self.testgame.groups.append(gologic.group((4,6),0,self.testgame.gameboard.grid))
        self.testmergelist = [self.testgame.groups[0],self.testgame.groups[1],self.testgame.groups[2]]
        self.testgame.merge_groups(self.testmergelist)
        assert len(self.testgame.groups) == 1,"Should only be one group after this merge"
        assert len(self.testgame.groups[0].positions) == 6 ,"Group should have 6 positions"
        assert self.testgame.gameboard.grid[(4,6)].my_group == self.testgame.groups[0],"Stones my_group var should have been set to remaining group"
       
    #test the kill group function
    def test_kill_group(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((5,5),1,15)
        self.testgame.gameboard.add_stone((4,4),1,15)
        self.testgame.gameboard.add_stone((5,4),1,15)
        self.testgame.groups.append(gologic.group((5,5),1,self.testgame.gameboard.grid))
        self.testgame.groups[0].add_position((4,4),self.testgame.gameboard.grid)
        self.testgame.groups[0].add_position((5,4),self.testgame.gameboard.grid)
        assert len(self.testgame.groups) == 1,"There should be 1 group"
        self.testgame.kill_group(self.testgame.groups[0])
        assert len(self.testgame.groups) == 0,"There should be 0 groups after killing group"
        for position, value in self.testgame.gameboard.grid.items():
            assert value == None,"Board should be empty"
        assert self.testgame.dead_stones[1] == 3,"3 white stones should have died"
      
    #test sim_move function
    def test_sim_move(self):
        self.testgame = gologic.game(19)
        self.testmove = gologic.move((5,5),0)
        sim_game = self.testgame.sim_move(self.testmove)
        assert len(sim_game.groups) == 1,"There should be 1 group"
        assert len(sim_game.groups[0].positions) == 1,"There should be 1 position in the group"
        
    #test sim_move function
    def test_sim_move2(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((4,5),0,15)
        self.testgame.groups.append(gologic.group((4,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((6,5),0,15)
        self.testgame.groups.append(gologic.group((6,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,6),0,15)
        self.testgame.groups.append(gologic.group((5,6),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,4),0,15)
        self.testgame.groups.append(gologic.group((5,4),0,self.testgame.gameboard.grid))
        self.testmove = gologic.move((5,5),0)
        sim_game = self.testgame.sim_move(self.testmove)
        assert len(sim_game.groups) == 1,"There should be 1 group"
        assert len(sim_game.groups[0].positions) == 5,"There should be 5 positions in the group"
        
    #test make_a_move function
    def test_make_a_move(self):
        self.testgame = gologic.game(19)
        self.testmove = gologic.move((5,5),0)
        legality = self.testgame.make_a_move(self.testmove)
        assert legality != False,"this move should be legal"

    #test make_a_move function
    def test_make_a_move2(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((4,5),1,15)
        self.testgame.groups.append(gologic.group((4,5),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((6,5),1,15)
        self.testgame.groups.append(gologic.group((6,5),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,6),1,15)
        self.testgame.groups.append(gologic.group((5,6),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,4),1,15)
        self.testgame.groups.append(gologic.group((5,4),1,self.testgame.gameboard.grid))
        self.testmove = gologic.move((5,5),0)
        legality = self.testgame.make_a_move(self.testmove)
        assert legality == False,"this move should be illegal"
        
   #test make_a_move function
    def test_make_a_move3(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((4,5),1,15)
        self.testgame.groups.append(gologic.group((4,5),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((6,5),1,15)
        self.testgame.groups.append(gologic.group((6,5),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,6),1,15)
        self.testgame.groups.append(gologic.group((5,6),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,4),1,15)
        self.testgame.groups.append(gologic.group((5,4),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((4,4),0,15)
        self.testgame.groups.append(gologic.group((4,4),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((5,3),0,15)
        self.testgame.groups.append(gologic.group((5,3),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((6,4),0,15)
        self.testgame.groups.append(gologic.group((6,4),0,self.testgame.gameboard.grid))
        self.testmove = gologic.move((5,5),0)
        legality = self.testgame.make_a_move(self.testmove)
        assert legality != False,"this move should be legal" 
        assert len(self.testgame.groups) == 7,"should be 7 groups after this move has been made"  
        assert legality.dead_stones[1] == 1,"One white stone should have died"
        
    #test make_a_move function
    def test_make_a_move4(self):
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((3,4),0,10)
        self.testgame.groups.append(gologic.group((3,4),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((3,5),0,10)
        self.testgame.groups[0].add_position((3,5),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((2,3),1,10)
        self.testgame.groups.append(gologic.group((2,3),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((2,4),1,10)
        self.testgame.groups[1].add_position((2,4),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((2,5),1,10)
        self.testgame.groups[1].add_position((2,5),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((4,4),1,10)
        self.testgame.groups.append(gologic.group((4,4),1,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((4,5),1,10)
        self.testgame.groups[1].add_position((4,5),self.testgame.gameboard.grid)
        self.testgame.gameboard.add_stone((3,6),1,10)
        self.testgame.groups.append(gologic.group((3,6),1,self.testgame.gameboard.grid))
        self.testmove = gologic.move((3,3),1)
        legality = self.testgame.make_a_move(self.testmove)
        assert legality != False,"this move should be legal"
        assert len(legality.groups) == 3,"should be 3 groups after this move has been made"  
        assert legality.dead_stones[0] == 2,"2 black stones should have died"

        
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
        self.testgame = gologic.game(19)
        self.testgame.gameboard.add_stone((3,5),1,15)
        self.testgroup = gologic.group((3,5),0,self.testgame.gameboard.grid)
        assert self.testgroup.positions[0][0] == 3 , "x position should be 3"
        assert self.testgroup.positions[0][1] == 5 , "y position should be 5"
       
    #test am_i_alive function    
    def test_am_i_alive(self):
        self.testboard = gologic.board(13)
        self.testboard.grid[(3,3)] = gologic.stone(0,2)
        self.testgroup = gologic.group((3,3),0,self.testboard.grid)
        assert self.testgroup.am_i_alive(self.testboard.grid) == True, "group should have more than 0 liberties"
        
        self.testboard.grid[(0,0)] = gologic.stone(0,2) 
        self.testgroup2 = gologic.group((0,0),0,self.testboard.grid)
        self.testboard.grid[(1,0)] = gologic.stone(1,2)
        self.testboard.grid[(0,1)] = gologic.stone(1,3)
        assert self.testgroup2.am_i_alive(self.testboard.grid) == False, "group should have 0 liberties"
        
        self.testboard.grid[(10,10)] = gologic.stone(0,2)
        self.testgroup3 = gologic.group((10,10),0,self.testboard.grid)
        self.testboard.grid[(11,10)] = gologic.stone(1,2)
        self.testboard.grid[(9,10)] = gologic.stone(1,3)
        self.testboard.grid[(10,11)] = gologic.stone(1,4)
        self.testboard.grid[(10,9)] = gologic.stone(1,5)
        assert self.testgroup3.am_i_alive(self.testboard.grid) == False, "group should have 0 liberties"
 
    #test am_i_alive function    
    def test_am_i_alive2(self):
        self.testgame = gologic.game(9)
        self.testgame.gameboard.add_stone((5,5),0,1)
        self.testgame.groups.append(gologic.group((5,5),0,self.testgame.gameboard.grid))
        self.testgame.gameboard.add_stone((4,4),0,1)
        self.testgame.groups[0].add_position((4,4),self.testgame.gameboard.grid)
        assert self.testgame.groups[0].am_i_alive(self.testgame.gameboard.grid) == True, "group should have more than 0 liberties"
 
    #test am_i_alive function    
    def test_am_i_alive3(self):
        self.testgame = gologic.game(9)
        self.testgame.gameboard.add_stone((4,4),0,15)
        self.testgame.gameboard.add_stone((4,5),0,16)
        self.testgame.groups.append(gologic.group((4,5),0,self.testgame.gameboard.grid))
        self.testgame.groups[0].add_position((4,4),self.testgame.gameboard.grid)
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