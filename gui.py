
import math
from threading import Event
from solver import Solver
from constants import *
import pygame

class Sudoku():

    def __init__(self) -> None:
        self.solver_event = Event()
        self.solver = Solver(event=self.solver_event)
        self.board = PLAYER_BOARD
        self.guesses_dict = {}

        
        self.solver.print_board(PLAYER_BOARD)

        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', int(SQUARE_SIZE / 2))
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Sudoku solver')
        self.bt_alg_running = False
        self.guessed_number = None
        self.marked_square = None
        self.marked_idx = None
        self.mistakes = 0
        self.mistake_pos_y = (BOARDER_START_Y + BOARD_SIZE) + 40
        self.mistake_pos_x = 40

    def drawBoardLines(self):
        # Draw lines
        pygame.draw.rect(self.screen, (0, 0, 0), (BOARDER_START_X, BOARDER_START_Y, BOARD_SIZE, BOARD_SIZE), 4)

        for i in range(1, SIZE):
            line_weight = 3 if i == 3 or i == 6 else 1
            offset = SQUARE_SIZE * i
            pygame.draw.line(self.screen, LINES_COLOR, (BOARDER_START_X, BOARDER_START_Y + offset), (BOARDER_START_X + BOARD_SIZE, BOARDER_START_Y + offset), line_weight)
            pygame.draw.line(self.screen, LINES_COLOR, (BOARDER_START_X + offset, BOARDER_START_Y), (BOARDER_START_X + offset, BOARDER_START_Y + BOARD_SIZE), line_weight)

    def isCurrentSquare(self, row, col):
        return row == self.solver.current_square[0] and col == self.solver.current_square[1] and self.bt_alg_running

    def drawAndUpdateNumbers(self):
        # Draw numbers
        for i in range(0,SIZE):
            for j in range(0,SIZE):
                color = 'red' if self.isCurrentSquare(row=i, col=j) else 'black'
                text = self.font.render(f"{self.board[i][j] if self.bt_alg_running != 0 else '' if self.board[i][j] == 0 else self.board[i][j]}", True, color, 'white')
                self.screen.blit(text,(BOARDER_START_X + 5 + NUMBER_POS_START + SQUARE_SIZE * j ,BOARDER_START_Y + NUMBER_POS_START + SQUARE_SIZE * i))

    def run(self):
        self.gameLoop()
        pygame.quit()

    def getClickerSquare(self, x, y):
        
        square_start_x = BOARDER_START_X + math.floor((x - BOARDER_START_X) / SQUARE_SIZE) * SQUARE_SIZE
        square_start_y = BOARDER_START_Y + math.floor((y - BOARDER_START_Y) / SQUARE_SIZE) * SQUARE_SIZE
        
        if (BOARDER_START_X + BOARD_SIZE <= square_start_x or square_start_x < BOARDER_START_X):
            return None
        
        if (BOARDER_START_Y + BOARD_SIZE <= square_start_y or square_start_y < BOARDER_START_Y):
            return None

        return square_start_x, square_start_y

    def drawMarkedSquare(self):
        if(self.marked_square != None):
                pygame.draw.rect(self.screen, 'red',(self.marked_square[0], self.marked_square[1], SQUARE_SIZE + 2, SQUARE_SIZE + 2), 3)

    def checkGuess(self):
        
        if (not self.solver.isLegal(self.board, self.marked_idx[1], self.marked_idx[0], self.guesses_dict[self.marked_square])):
            self.mistakes += 1
        else:
            self.board[self.marked_idx[1]][self.marked_idx[0]] = self.guesses_dict[self.marked_square]
        del self.guesses_dict[self.marked_square]

    def drawMistakes(self):
        text = self.font.render(f"Mistakes: {self.mistakes}", True, "red", 'white')
        self.screen.blit(text,(self.mistake_pos_x, self.mistake_pos_y))


    def gameLoop(self):

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.solver_event.set()

                
                if event.type == pygame.KEYDOWN and not self.bt_alg_running:
                    
                    keys = pygame.key.get_pressed()
                    
                    if keys[pygame.K_SPACE]:
                        self.board = BOARD
                        self.bt_alg_running = True
                        self.guesses_dict.clear()
                        self.solver.start()

                    if event.unicode.isnumeric() and self.marked_square != None and BOARD[self.marked_idx[1]][self.marked_idx[0]] == 0:
                        number_pressed = int(event.unicode)
                        self.guesses_dict[self.marked_square] = number_pressed

                    if keys[pygame.K_BACKSPACE] and self.marked_square in self.guesses_dict:
                        del self.guesses_dict[self.marked_square]
                    
                    if keys[pygame.K_RETURN] and self.marked_square in self.guesses_dict.keys():
                        self.checkGuess()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_point = pygame.mouse.get_pos()
                    self.marked_square = self.getClickerSquare(clicked_point[0], clicked_point[1])
                    if self.marked_square is None:
                        self.marked_idx = None
                    else:
                        self.marked_idx = (int(self.marked_square[0] / SQUARE_SIZE), int(self.marked_square[1] / SQUARE_SIZE))

            # Draw on screen
            self.screen.fill('white')
            self.drawBoardLines()
            self.drawAndUpdateNumbers()
            self.drawMarkedSquare()
            self.drawMistakes()

            for item in self.guesses_dict:
                font = pygame.font.Font('freesansbold.ttf', int(SQUARE_SIZE / 4))
                
                text = font.render(f"{self.guesses_dict[item]}", True, (9,71,9), 'white')
                self.screen.blit(text,(10 +item[0], 10 + item[1]))

            if self.mistakes == MAX_MISTAKES:
                running = False

            pygame.display.flip()
        




        



        
