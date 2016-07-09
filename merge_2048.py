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
                final_line.append(num*2)
                new_line = line[index+2:]
                compare_and_add(new_line, final_line)
                break
            else:
                final_line.append(num)
        else:
            if len(line) == 1:
                final_line.append(num)  
                
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    output_line = []
    final_line = []
   
    for index, num in enumerate(line):
        if num != 0:
            output_line.append(num)
            
    while len(line) > len(output_line):
        output_line.append(0)
        
    compare_and_add(output_line, final_line)
    
    while len(line) > len(final_line):
        final_line.append(0)
    
    return final_line