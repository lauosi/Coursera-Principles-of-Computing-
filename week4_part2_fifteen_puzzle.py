"""
Principles of Computing (Part 2)
Week 4
Loyd's Fifteen puzzle - solver and visualizer
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods
    
    def zero_invariant(self, target_row, target_col):
        """
        Helper invariant that checks if zero is at the correct spot
        """
        # check if tile 0 is positioned at (target_row, target_col)
        if self.get_number(target_row, target_col) != 0:
            print 
            print " 0 is not at right position "
            return False
        return True
    
    def without_zero_invariant(self, target_row, target_col):
        """
        Helper invariant that does not check if 0 is at the correct spot
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        row = self.get_height() - 1 
        col = self.get_width() - 1
        
        # check if all tiles in rows i + 1 or below and to the right are 
        # positioned at their solved location
        while (row, col) != (target_row, target_col):
            if self.current_position(row, col) != (row, col):
                print "current position is not the right one"
                return False
            if col != 0:
                col -= 1
            else:
                col = self.get_width() - 1
                row -= 1
        # return True if all three conditions are true
        return True
    
    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        
        return self.zero_invariant(target_row, target_col) and self.without_zero_invariant(target_row, target_col)
        
    def possition_tile(self, target_row, target_col, current_row, current_col):
        """
        Helper function: Place correct tile at target 
        position. Returns a move string
        """
        # scenario when the tile is in the same row
        if current_row == target_row:
            if target_col == current_col + 1:
                move = "l"
            elif target_col < current_col:
                move = (current_col - target_col) * "r" + "ulldr" * (current_col - target_col - 1) + "ulld"
            else:
                move = (target_col - current_col) * "l" + "urrdl" * (target_col - current_col - 1)
            
        # scenario when the tile is exactly above zero:
        elif current_col == target_col:
            move =(target_row - current_row) * "u" + (target_row - current_row - 1) * "lddru" + "ld"
            
        # scenario when the tile is on the left site:
        elif current_col < target_col:
            # when tile is further on the left
            if current_row != 0:
                move = (target_row - current_row) * "u" + (target_col - current_col) * "l" + "u" + (target_col - current_col) * "r" + "dl" + (target_row - current_row) * "druld"
            else:
                move = (target_row - current_row) * "u" + (target_col - current_col) * "l" + (target_col - current_col - 1) * "drrul" + (target_row - current_row) * "druld"
            # scenario when the tile is on the right site:
        else:
            if current_row != 0:
                if target_col == current_col - 1:
                    move = (target_row - current_row) * "u" + "rulld" + (target_row - current_row) * "druld"
                else:
                    move =(target_row - current_row) * "u" + (current_col - target_col) * "r" + "ulldr" * (current_col - target_col - 1) + "ulld" +  (target_row - current_row) * "druld"
            # when tile is further on the left
            else:
                move =(target_row - current_row) * "u" + (current_col - target_col) * "r" + "dllur" * (current_col - target_col - 1) + "dllu" +  (target_row - current_row) * "druld"
        
        return move

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col)
        
        current_row, current_col = self.current_position(target_row, target_col)
        move = self.possition_tile(target_row, target_col, current_row, current_col)
        self.update_puzzle(move)
        assert self.lower_row_invariant(target_row, target_col - 1)
        return move
    
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0)
        
        self.update_puzzle("ur")
        current_row, current_col = self.current_position(target_row, 0)
        
        if (target_row, 0) == (current_row, current_col):
            move = (self.get_width() - 2) * "r"
        else:
            move = self.possition_tile(target_row - 1, 1, current_row, current_col)
            # the move string for a 3×2 puzzle 
            move += "ruldrdlurdluurddlu" + (self.get_width() - 1) * "r"
       
        self.update_puzzle(move)
        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return "ur" + move

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.zero_invariant(0, target_col):
            return False
        try:
            if not self.without_zero_invariant(1, target_col - 1):
                return False
        except AssertionError:
            if not self.without_zero_invariant(1, target_col):
                return False
            
        for col in range(target_col + 1, self.get_width()):
            if self.current_position(0, col) != (0, col):
                print "row0: current position is not the right one"
                return False
        return True
        

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.lower_row_invariant(1, target_col):
            return False
        
        for col in range(target_col + 1, self.get_width()):
            if self.current_position(0, col) != (0, col):
                print "row0: current position is not the right one"
                return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        self.update_puzzle("ld")
        
        if self.row1_invariant(target_col - 1):
            return "ld"
        else:
            current_row, current_col = self.current_position(0, target_col)
            move = self.possition_tile(1, target_col - 1, current_row, current_col)
            move += "urdlurrdluldrruld"
            self.update_puzzle(move)

        assert self.row1_invariant(target_col - 1)
        return "ld" + move

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col)
        
        current_row, current_col = self.current_position(1, target_col)
        move = self.possition_tile(1, target_col, current_row, current_col) + "ur"
        self.update_puzzle(move)
        
        assert self.row0_invariant(target_col)
        return move

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1)
        move = "ul"
        self.update_puzzle(move)
        
        for dummy_iter in range(2):
            if self.row0_invariant(0):
                return move
            self.update_puzzle("drul")
            move += "drul"
        
        assert self.row0_invariant(0)
        return move
        
    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        move = ""
        row = self._height - 1
        col = self._width - 1
        
        if self.row0_invariant(0):
            return move
        
        while self.get_number(row, col) != 0:
            try:
                self.update_puzzle("r")
                move += "r"
            except AssertionError:
                pass
            
            try:
                self.update_puzzle("d")
                move += "d"
            except AssertionError:
                pass
        
        while (row, col) != (1, self._width - 1):
            if col != 0:
                move += self.solve_interior_tile(row, col)
                col -= 1
            else:
                move += self.solve_col0_tile(row)
                col = self._width - 1
                row -= 1
        
        while (row, col) != (1, 1):
            move += self.solve_row1_tile(col)
            move += self.solve_row0_tile(col)
            col -= 1
        
        move += self.solve_2x2()
        
        return move

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
        
