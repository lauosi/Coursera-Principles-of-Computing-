"""
Mini-max Tic-Tac-Toe Player
to play in http://www.codeskulptor.org/
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    winner = board.check_win()
    other_player = provided.switch_player(player)
    best_score = -2
    
    # base case, return invalid move
    if winner != None:
        return (SCORES[winner], (-1, -1))
    
    # check out all possible moves
    for allowed_move in board.get_empty_squares():
        clone_board = board.clone()
        clone_board.move(allowed_move[0], allowed_move[1], player)
        result = mm_move(clone_board, other_player)
        # factor SCORES[player] allows to always maximize 
        score = result[0] * SCORES[player]
        
        # if we cannot do better return score
        if score == 1:
            return (score * SCORES[player], allowed_move)
        
        # look for best move
        elif score > best_score:
            best_score = score
            best_move = allowed_move
    
    return (best_score * SCORES[player], best_move)
            

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
