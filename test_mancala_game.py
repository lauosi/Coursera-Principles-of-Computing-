"""
Template testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create two games
    game = game_class()
    game2 = game_class()
    
    # add tests using suite.run_test(....) here

    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([0]), "Test #0: init")

    # check the str and get_num_seeds methods
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    game.set_board(config1)   
    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")
    
    suite.run_test(game.is_game_won(), False, "Test #2: is_game_won") 
    config2 = [5, 0, 0, 0, 0, 0, 0]    
    game2.set_board(config2)
    suite.run_test(game2.is_game_won(), True, "Test #2: is_game_won")
    
    suite.run_test(game.choose_move(), 5, "Test #3: choose_move")
    suite.run_test(game2.choose_move(), 0, "Test #3: choose_move")
    
    #suite.run_test(game.apply_move(5), , "Test #4: apply_move")
    #suite.run_test(game.choose_move(1), , "Test #4: apply_move")
    
    

    
    
    # report number of tests and failures
    suite.report_results()
