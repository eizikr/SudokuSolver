
BOARD_SIZE = 600

# Use later
WINDOW_WIDTH = 650 
WINDOW_HEIGHT = 750
BOARDER_START_X = (WINDOW_WIDTH - BOARD_SIZE) / 2
BOARDER_START_Y =  (WINDOW_WIDTH - BOARD_SIZE) / 2

SIZE = 9
MAX_MISTAKES = 3
SQUARE_SIZE = BOARD_SIZE / SIZE

NUMBER_POS_START = SQUARE_SIZE / 3.5

LINES_COLOR=(0,0,0)

BOARD = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

PLAYER_BOARD = [x[:] for x in BOARD]
