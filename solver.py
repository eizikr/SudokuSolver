import threading
from constants import BOARD, SIZE, SOLVED_BOARD
import time


class Solver(threading.Thread):
    def __init__(self, event) -> None:
        self.event = event
        self.current_square = [0,0]
  
        threading.Thread.__init__(self)
    

    def run(self):
        self.backtracking(BOARD, 0, 0)

    def display(self,matrix):
        # Print the board
        for row in range(SIZE):
            for col in range(SIZE): 
                print(matrix[row][col], end = " ")  
            print()

    def isSolve(self, matrix, row, col, num):
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

    def backtracking(self,matrix, row, col):
        if self.event.is_set():
            print('The backtracking thread was stopped prematurely.')
            exit(1)
        # If done with the matrix    
        if (row == SIZE -1 and col == SIZE):
            return True
        
        # If done with this row
        if (col == SIZE):
            row += 1
            col = 0

        # If this spot is emptey (row, col) continue to next
        if (matrix[row][col] != 0):
            return self.backtracking(matrix, row, col + 1)

        self.current_square = [row,col]

        # Test numbers for this spot (row, col)
        for num in range(1, SIZE + 1):
            if self.isSolve(matrix, row, col, num):
                matrix[row][col] = num
                time.sleep(0.018)


                if self.backtracking(matrix, row, col + 1) == True:
                    return True
                
            time.sleep(0.018)
            
            self.current_square = [row,col]
            matrix[row][col] = 0

        # If no solution for this spot (row,col) return False and continue the previus from where we stoped in the loop
        return False




 
