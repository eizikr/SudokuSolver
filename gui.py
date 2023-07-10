
from threading import Thread
from solver import Solver
from constants import BOARD, BOARD_SIZE, LINES_COLOR, NUMBER_POS_START, SIZE, SQUARE_SIZE
import pygame

class Sudoku():

    def __init__(self) -> None:
        pygame.init()

        self.font = pygame.font.Font('freesansbold.ttf', int(SQUARE_SIZE / 2))
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        pygame.display.set_caption('Sudoku solver')
        self.bt_alg_running = False
        self.solver = Solver()


    def drawBoardLines(self):
        # Draw lines
        for i in range(1, SIZE):
            line_weight = 3 if i == 3 or i == 6 else 1
            offset = SQUARE_SIZE * i
            pygame.draw.line(self.screen, LINES_COLOR, (0, offset), (BOARD_SIZE, offset), line_weight)
            pygame.draw.line(self.screen, LINES_COLOR, (offset, 0), (offset, BOARD_SIZE), line_weight)

    def isCurrentSquare(self, row, col):
        return row == self.solver.current_square[0] and col == self.solver.current_square[1] and self.bt_alg_running

    def drawAndUpdateNumbers(self):
        # Draw numbers
        for i in range(0,SIZE):
            for j in range(0,SIZE):
                color = 'red' if self.isCurrentSquare(row=i, col=j) else 'black'
                text = self.font.render(f"{BOARD[i][j] if self.bt_alg_running != 0 else '' if BOARD[i][j] == 0 else BOARD[i][j]}", True, color, 'white')
                self.screen.blit(text,(NUMBER_POS_START + SQUARE_SIZE * j ,NUMBER_POS_START + SQUARE_SIZE * i))

    def run(self):
        self.gameLoop()

    def gameLoop(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and not self.bt_alg_running:
                    self.bt_alg_running = True
                    keys = pygame.key.get_pressed()             
                    if keys[pygame.K_SPACE]:
                        Thread(target=self.solver.run).start()

            # Draw on screen
            self.screen.fill('white')
            self.drawBoardLines()
            self.drawAndUpdateNumbers()


            pygame.display.flip()
        
        pygame.quit()
        


        



        
