
from constants import SIZE, BOARD

def display(matrix):
    # Print the board
    for row in range(SIZE):
        for col in range(SIZE): 
            print(matrix[row][col], end = " ")  
        print()

def isSolve(matrix, row, col, num):
    # Check columns
    for col_pos in range (9):
        if matrix[row][col_pos] == num:
            return False
    # Check rows
    for row_pos in range(9):
        if matrix[row_pos][col] == num:
            return False
        
    # Check 3X3 square
    first_row = row - (row % 3)
    first_col = col - (col % 3)
    for row_offset in range(3):
        for col_offset in range(3):
            if(matrix[row_offset + first_row][col_offset + first_col] == num):
                return False
            
    # This is the right place
    return True

def sudoku(matrix, row, col):

    # If done with the matrix    
    if (row == SIZE -1 and col == SIZE):
        return True
    
    # If done with this row
    if (col == SIZE):
        row += 1
        col = 0

    # If this spot is emptey (row, col) continue to next
    if (matrix[row][col] != 0):
        return sudoku(matrix, row, col + 1)

    # Test numbers for this spot (row, col)
    for num in range(1, SIZE + 1, 1):

        if isSolve(matrix, row, col, num):
            matrix[row][col] = num

            if sudoku(matrix, row, col + 1) == True:
                return True
        
        matrix[row][col] = 0

    # If no solution for this spot (row,col) return False and continue the previus from where we stoped in the loop    
    return False

if(sudoku(BOARD, 0, 0)):display(BOARD)
else: print('no solution')


 
