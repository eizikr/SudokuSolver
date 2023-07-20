import threading
from constants import BOARD, SIZE, PLAYER_BOARD
import time


class Solver(threading.Thread):
    def __init__(self, event) -> None:
        self.event = event          # To stop the algorithm thread when exit 
        self.current_square = [0,0] # To track which square the algorithm care now
        threading.Thread.__init__(self)


    def run(self):
        self.backtracking(BOARD, 0, 0)

    def print_board(self,matrix):
        print (" -----------------------")
        
        for row in range(SIZE):
            for col in range(SIZE): 

                if (not col):
                    print("|", end = " ")
                
                print(matrix[row][col], end = " " if col % 3 != 2 or col == SIZE - 1 else " | ")  
         
                if (col == SIZE - 1):
                    print("|")
         
            if(row % 3 == 2 and row != SIZE - 1):
                print ("| --------------------- |")
        
        print (" -----------------------")
        
    def isLegal(self, matrix, row, col, num):
        # Check columns
        for col_pos in range (9):
            if matrix[row][col_pos] == num and col_pos != col:
                return False
        # Check rows
        for row_pos in range(9):
            if matrix[row_pos][col] == num and row_pos != row:
                return False
        # Check 3X3 square
        first_row = row - (row % 3)
        first_col = col - (col % 3)
        for row_offset in range(3):
            for col_offset in range(3):
                current_row = row_offset + first_row
                current_col = col_offset + first_col

                if(matrix[current_row][current_col] == num and current_row != row and current_col != col):
                    return False

        # Legal square
        return True


    def backtracking(self,matrix, row, col):
        # Kill thread if exit the program
        if self.event.is_set():
            print('The backtracking thread was stopped prematurely.')
            exit(1)

        # If done with the whole matrix    
        if (row == SIZE -1 and col == SIZE):
            return True
        
        # If done with this row
        if (col == SIZE):
            row += 1
            col = 0

        # If this spot is not emptey (row, col) continue to next
        if (matrix[row][col] != 0):
            return self.backtracking(matrix, row, col + 1)


        self.current_square = [row,col]

        # Test numbers for this spot (row, col)
        for num in range(1, SIZE + 1):
            if self.isLegal(matrix, row, col, num):
                matrix[row][col] = num
                time.sleep(0.018)

                if self.backtracking(matrix, row, col + 1) == True:
                    return True
                
            time.sleep(0.018)
            
            self.current_square = [row,col]
            matrix[row][col] = 0

        # If no solution for this spot (row,col) return False and continue the previus from where we stoped in the loop
        return False




 
