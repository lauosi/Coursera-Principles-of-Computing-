"""
Merge function for 2048 game.
"""

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
