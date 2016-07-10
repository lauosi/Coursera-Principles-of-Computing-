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
        self.grid_height = grid_height
        self.grid_width = grid_width
        # create grid
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # create empty grid
        self.grid = [[0 for col in range(self.grid_width)]
                   for row in range(self.grid_height)]
        
        # add two initial tiles
        self.new_tile()
        self.new_tile()
        
        return self.grid
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        pass
    
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
            if self.grid[row][col] == 0:
                # for 90% cases set number 2, for 10% set number 4
                if random.random() >= 0.1:
                    self.grid[row][col] = 2
                else:
                    self.grid[row][col] = 4
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

game = TwentyFortyEight(4, 4)
poc_2048_gui.run_gui(game)
