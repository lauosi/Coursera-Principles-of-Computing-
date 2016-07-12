"""
Game Tic-Tac-Toe with Monte Carlo simulation
(teach computer so it would never loose a game)
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided
#import user41_FJQgE9i6G2_3 as poc_ttt_testsuite 

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 20        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player): 
    """
    Play a game starting with the given player by making random moves. 
    """
    
    while board.check_win() == None:
        # choose randomly one of empty squares
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        player = provided.switch_player(player)
    return

def mc_update_scores(scores, board, player):
    """
    Score the completed board and update the scores grid.
    """
    dim = board.get_dim()
    winner = board.check_win()
    
    # if there was a tie "score table" does not change
    if winner != provided.DRAW:
        for row in range(dim):
            for col in range(dim):
                # if the square was empty do not change its value
                # in the "score table"
                if board.square(row, col) != provided.EMPTY:
                    if winner == player:
                        if player == board.square(row, col):
                            scores[row][col] += SCORE_CURRENT
                        else:
                            scores[row][col] -= SCORE_OTHER
                    else:
                        if player == board.square(row, col):
                            scores[row][col] -= SCORE_CURRENT
                        else:
                            scores[row][col] += SCORE_OTHER

def get_best_move(board, scores):
    """
    Find all of the empty squares with the maximum 
    score and randomly return one of them as a tuple. 
    """
    empty_squares = board.get_empty_squares()
    dim = board.get_dim()
    
    # you can choose the best move only if there are 
    # squares lelt to choose from
    
    if empty_squares:
        # find the best value in flat "score list"
        # using only squares (row, col) that are empty
        best_value = max([scores[row][col] for row in range(dim) 
                          for col in range(dim)if (row, col) in empty_squares])
        
        # find all squares with the highest value that are available (empty)
        best_squares = [(row, col) for row in range(dim) for col in range(dim) 
                        if (row, col) in empty_squares and 
                        scores[row][col] == best_value]
        return random.choice(best_squares)
        
        
    
def mc_move(board, player, trials):
    """
    Use the Monte Carlo simulation to return a move 
    for the machine player in the form of a tuple.
    """
    # create "score list" that will be used for every trial
    scores = [[0 for dummy_col in range(board.get_dim())]
             for dummy_row in range(board.get_dim())]
    
    # find the best move using Monte Carlo simulation
    for dummy in range(trials):
        testing_board = board.clone()
        mc_trial(testing_board, player)
        mc_update_scores(scores, testing_board, player)
    return get_best_move(board, scores)
  
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
