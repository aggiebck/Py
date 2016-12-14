# Determines whether a Sudoku solution is valid.

def valid_rows(soln):
    ''' Returns True if each row is valid 
        and False otherwise.
    ''' 
    result = True
    for element in soln:
        row = set(element)
        #print(row)
        if len(row) != 9:
            result = False
    #print(result)
    return result

def valid_cols(soln):
    ''' Returns True if each column
        is valid and False otherwise.
    '''
    result = True
    for i in range(0,9):
        col = []
        for element in soln:
            #print(element)
            col.append(element[i])
        col2 = set(col)
        if len(col2) != 9:
            result = False
    #print(result)
    return result

def valid_blocks(soln):
    ''' Checks each 3 x 3 block in the puzzle. 
        Returns True if each block is valid 
        and False otherwise.
    '''
    result = True
    sq_tl = [] #topleft
    sq_mt = [] #middletop
    sq_tr = [] #topright
    sq_ml = [] #midleft
    sq_mm = [] #mid-mid
    sq_mr = [] #midright
    sq_bl = [] #botleft
    sq_bm = [] #botmid
    sq_br = [] #botright  
    
    #top left 3x3
    for i in range(0,3):
        for a in range(0,3):
            sq_tl.append(soln[i][a])
    
    #top mid 3x3
    for i in range(0,3):
        for a in range(3,6):
            sq_mt.append(soln[i][a])
    
    #top right 3x3
    for i in range(0,3):
        for a in range(6,9):
            sq_tr.append(soln[i][a])
            
    #mid left 3x3
    for i in range(3,6):
        for a in range(0,3):
            sq_ml.append(soln[i][a])
            
    #mid mid 3x3
    for i in range(3,6):
        for a in range(3,6):
            sq_mm.append(soln[i][a])
            
    #mid right 3x3
    for i in range(3,6):
        for a in range(6,9):
            sq_mr.append(soln[i][a])
            
    #bot left 3x3
    for i in range(6,9):
        for a in range(0,3):
            sq_bl.append(soln[i][a])
                
    #bot mid 3x3
    for i in range(6,9):
        for a in range(3,6):
            sq_bm.append(soln[i][a])
                
    #bot right 3x3
    for i in range(6,9):
        for a in range(6,9):
            sq_br.append(soln[i][a])     
    
    biglist = []
    biglist.append(sq_tl)
    biglist.append(sq_mt)
    biglist.append(sq_tr)
    biglist.append(sq_ml)
    biglist.append(sq_mm)
    biglist.append(sq_mr)
    biglist.append(sq_bl)
    biglist.append(sq_bm)
    biglist.append(sq_br)
    #print(biglist)
    for i in biglist:
        bigset = set(i)
        if len(bigset) != 9:
            result = False        
    return result
       
    
  
def valid_soln(soln):
    ''' Returns True if a Sudoku solution is valid and False
        otherwise.
    '''
    
    # Check if rows are valid. 
    if not valid_rows(soln):
        return False

    # Check if columns are valid.
    if not valid_cols(soln):
        return False

    # Check if 3x3 submatrices (or blocks) are valid.
    if not valid_blocks(soln):
        return False        
    
    # If all checks pass, then the solution is valid.
    return True


def main():
    
    ''' The checking process begins here. '''
   
    # Get file name.
    file_name = input('Enter filename: ')
    
    # Open file and read its data.
    input_file = open(file_name)
    file_data = input_file.readlines()
   
    # Close file since the information from the file is
    # stored in the list file_data. While not necessary,
    # it is a good habit to close a file once you are 
    # done with it.  
    input_file.close()
    
    # sudoku_soln is populated with the data
    # from the solution file. sudoku_soln is a
    # tuple of tuples, where each tuple is of size
    # 9. Draw a picture of sudoku_soln before you
    # try to write the remaining code.
    
    # Also, when adding values to a tuple, if we
    # are only add one tuple, we must use a comma
    # at the end (see Lines A & B).
   
    sudoku_soln = ()
    for line in file_data:
        row = ()
        for value in line.strip():
            row += (int(value),)     # Line A
        sudoku_soln += (row,)        # Line B
            
    # Check and print results. 
    print()
    if valid_soln(sudoku_soln):
        print('Valid solution')
    else:
        print('Invalid solution')


main()
