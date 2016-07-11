"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def compare_and_add(line, final_line):
    """
    Function that helps merge function to merge 
    a single row or column.
    """
    for index, num in enumerate(line):
        if index < len(line)-1:
            if num == line[index+1]:
                # if numbers are equal append them
                # to the final list and run the function again
                # on new list (without the merged numbers)
                final_line.append(num*2)
                new_line = line[index+2:]
                compare_and_add(new_line, final_line)
                # do not continue this loop if you merged
                break
            else:
                # if numbers are different simply add the
                # number and continue this loop
                final_line.append(num)
                new_line = line[index+1:]
                compare_and_add(new_line, final_line)
                break
        else:
            # if there is only one number left it cannot merge
            # append it to the list
            if len(line) == 1:
                final_line.append(num)  
                
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    output_line = []
    final_line = []
   
    for num in line:
        # move numbers left
        if num != 0:
            output_line.append(num)
        
    compare_and_add(output_line, final_line)
    
    # add the missing zeros
    while len(line) > len(final_line):
        final_line.append(0)
    
    return final_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.get_directions()
        # create grid
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # create empty grid
        self._grid = [[0 for dummy_col in range(self.get_grid_width())]
                   for dummy_row in range(self.get_grid_height())]
        
        # add two initial tiles
        self.new_tile()
        self.new_tile()
         
    def get_directions(self):
        """
        Return a dictionary with directions for a move method.
        """
        self._directions = {}
        self._directions[UP] = [(0, num) for num in range(self.get_grid_width())]
        self._directions[DOWN] = [(self.get_grid_height()-1, num) for num in range(self.get_grid_width())]
        self._directions[LEFT] = [(num, 0) for num in range(self.get_grid_height())]
        self._directions[RIGHT] = [(num, self.get_grid_width()-1) for num in range(self.get_grid_height())]
        
        return self._directions
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        correct_move = False
        
        if direction == UP or direction == DOWN:
            num_tiles = self.get_grid_height()  
        elif direction == LEFT or direction == RIGHT:
            num_tiles = self.get_grid_width()
        
        initial_tiles = self._directions[direction]
        for tile in initial_tiles:
            temp = []
            for num in range(num_tiles):
                row = tile[0] + num * OFFSETS[direction][0]
                col = tile[1] + num * OFFSETS[direction][1]
                temp.append(self._grid[row][col])
                
            merged = merge(temp)
            for num in range(num_tiles):
                row = tile[0] + num * OFFSETS[direction][0]
                col = tile[1] + num * OFFSETS[direction][1]
                if self._grid[row][col] != merged[num]:
                    correct_move = True
                self._grid[row][col] = merged[num]
        if correct_move:
            self.new_tile()
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        while True:
                # select square
                col = random.randrange(self.get_grid_width())
                row = random.randrange(self.get_grid_height())
                # keep looking for an empty square
                # break the loop while is found

                if self._grid[row][col] == 0:
                    # for 90% cases set number 2, for 10% set number 4
                    if random.random() >= 0.1:
                        self._grid[row][col] = 2
                    else:
                        self._grid[row][col] = 4
                    break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

#poc_2048_gui.run_gui(TwentyFortyEight(3, 3))

