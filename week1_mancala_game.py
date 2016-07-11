"""
Implementation of the mini-project: Solitaire Mancala.
"""
#import user41_xgirkWlas8_3 as poc_mancala_testsuite 

class  SolitaireMancala():
    """
    Simple class that implements Mancala
    """
    def __init__(self):
        """
        Create an empty store with no houses.
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Set new board to the game
        """
        self._board = list(configuration)
        
    def __str__(self):
        """
        Prints out the board.
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)
    
    def get_num_seeds(self, house_num):
        """
        Returns number of seeds in given house.
        """
        return self._board[house_num]
    
    def is_legal_move(self, house_num): 
        """
        Returns True while the move is legal,
        otherwise returns false.
        """
        if house_num == 0:
            return False
        elif self._board[house_num] == house_num:
            return True
        else:
            return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            seeds = self._board[house_num]
            self._board[house_num] = 0
            for seed in range(seeds):
                self._board[house_num - 1 - seed] += 1
                
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for num in range(len(self._board)):
            if self.is_legal_move(num):
                return num
        return 0
    
    def is_game_won(self):
        """
        """
        for house_seeds in self._board[1:]:
            if house_seeds != 0:
                return False
        return True
    
    def plan_moves(self):
        """
        Return sequence of shortest legal moves until none are available
        Not used in GUI version, only for machine testing
        """
        moves = []
        temp_board = self._board[:]
        while self.choose_move() != 0:
            move = self.choose_move()
            moves.append(move)
            self.apply_move(move)
        self._board = temp_board
        return moves
         
    
#game = SolitaireMancala()
#game.set_board([0, 0, 1, 1, 3, 5, 0])
#moves = game.plan_moves()
#print moves
#print game

#poc_mancala_testsuite.run_suite(SolitaireMancala)          