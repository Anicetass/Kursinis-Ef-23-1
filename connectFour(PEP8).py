import numpy as np
import pygame
from datetime import datetime
import os

# Const
ROWS = 6
COLS = 7
UNIT_SIZE = 100
EXTRA_ROWS = 1
P1_COLOR = (255, 0, 0)  # Red
P2_COLOR = (0, 0, 255)  # Blue
BACK_COLOR = (0, 0, 0)  # Black
BLANK_COLOR = (70, 70, 70)  # Gray
TEXT_COLOR = (255, 255, 255)  # White
filename = os.path.basename(__file__)
LOG_NAME = os.path.splitext(filename)[0] + ".log.txt"
SETUP_FILE = os.path.splitext(filename)[0] + ".setup.txt"
STALL_TIME = 3000


class BoardGame:
    def __init__(self, rows, cols):
        self._board = np.full((rows, cols), 0)
        self.game_over = False
        self.game_quit = False

    def print_board(self):
        print(self._board)


class ConnectFour(BoardGame):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)

    def __next_open_row(self, col):
        for r in reversed(range(ROWS)):
            if self._board[r][col] == 0:
                return r

    def valid_move(self, col):  # Column not full
        if self._board[0][col] == 0:
            return True
        return False

    def place_piece(self, col, piece):
        row = self.__next_open_row(col)
        self._board[row][col] = piece
        logger = Logger()
        logger.log_event(f"PLAYER_{piece}.move:[r:{abs(row-ROWS)},c:{col+1}]")
        return False

    def check_win(self, piece):
        # Horizontal
        for c in range(COLS - 3):
            for r in range(ROWS):
                if (self._board[r][c] == piece and self._board[r][c+1] == piece
                        and self._board[r][c+2] == piece and self._board[r][c+3] == piece):
                    return True
        # Vertical
        for c in range(COLS):
            for r in range(ROWS - 3):
                if (self._board[r][c] == piece and self._board[r+1][c] == piece
                        and self._board[r+2][c] == piece and self._board[r+3][c] == piece):
                    return True
        # Positively sloped diagonals
        for c in range(COLS - 3):
            for r in range(ROWS - 3):
                if (self._board[r][c] == piece and self._board[r+1][c+1] == piece
                        and self._board[r+2][c+2] == piece and self._board[r+3][c+3] == piece):
                    return True
        # Negatively sloped diagonals
        for c in range(COLS - 3):
            for r in range(3, ROWS):
                if (self._board[r][c] == piece and self._board[r-1][c+1] == piece
                        and self._board[r-2][c+2] == piece and self._board[r-3][c+3] == piece):
                    return True

    def check_draw(self):
        if np.all(self._board != 0):
            return True


class Display:
    def __init__(self, Game):
        self.game = Game

    def board_setup(self, screen, player, FONT):
        screen.fill(BACK_COLOR)
        self.board_top_text(f"PLAYER {player} TURN", FONT, screen)

        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.circle(screen, BLANK_COLOR,
                                   ((c*UNIT_SIZE+UNIT_SIZE/2), (r*UNIT_SIZE+UNIT_SIZE/2+UNIT_SIZE*EXTRA_ROWS)), RADIUS)

    def update_board(self, screen):
        for c in range(COLS):
            for r in range(ROWS):
                if self.game._board[r][c] == 1:
                    pygame.draw.circle(screen, P1_COLOR,
                                       ((c*UNIT_SIZE+UNIT_SIZE/2), (r*UNIT_SIZE+UNIT_SIZE/2+UNIT_SIZE*EXTRA_ROWS)), RADIUS)
                elif self.game._board[r][c] == 2:
                    pygame.draw.circle(screen, P2_COLOR,
                                       ((c*UNIT_SIZE+UNIT_SIZE/2), (r*UNIT_SIZE+UNIT_SIZE/2+UNIT_SIZE*EXTRA_ROWS)), RADIUS)

    def _clear_board_top(self, screen):
        pygame.draw.rect(screen, BACK_COLOR, (0, 0, WIDTH, UNIT_SIZE*EXTRA_ROWS))

    def board_top_text(self, message, FONT, screen, color=TEXT_COLOR):
        self._clear_board_top(screen)
        text = FONT.render(message, 1, color)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, UNIT_SIZE//2)
        screen.blit(text, text_rect)
        return 0


class Logger:
    _instance = None
    _log_list = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = LOG_NAME
        return cls._instance

    def log_event(self, event):
        current_time = datetime.now().strftime("%H:%M:%S")
        self._log_list.append(f"{current_time} game.{event}\n")

    def export_log_to_txt(self):
        with open(self.log_file, "w") as file:
            for log in self._log_list:
                file.write(f"{log}")


class FileSetup:
    def __check_file_exists(self, setup_file):
        return os.path.exists(setup_file)

    def setup_from_file(self, setup_file):
        global ROWS, COLS, UNIT_SIZE

        if self.__check_file_exists(setup_file):
            with open(setup_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if '=' in line and line.count('=') == 1:
                        variable, value = line.split('=')
                        variable = variable.strip()
                        value = value.strip()
                        if value.isdigit():
                            value = int(value)
                            if variable == 'ROWS' and 4 <= value <= 9:
                                ROWS = value
                            elif variable == 'COLS' and 4 <= value <= 9:
                                COLS = value
                            elif variable == 'UNIT_SIZE' and 50 <= value <= 150:
                                UNIT_SIZE = value


def runtime_decorator(func):
    def wrapper():
        logger = Logger()
        start_time = datetime.now()
        execute_function = func()
        end_time = datetime.now()
        total_time = end_time - start_time
        minutes = total_time.total_seconds() // 60
        seconds = total_time.total_seconds() % 60
        if minutes > 0:
            logger.log_event(f"RUNTIME:{int(minutes)}:{seconds:.2f}min")
        else:
            logger.log_event(f"RUNTIME:{seconds:.2f}sec")
        return execute_function
    return wrapper


@runtime_decorator
def connect_four_game():

    game = ConnectFour(ROWS, COLS)
    display = Display(game)
    logger = Logger()
    logger.log_event("START")

    # Turn and player setup
    turn = 1
    player = 1

    # Pygame setup
    pygame.init()
    FONT = pygame.font.SysFont("stylus", FONT_SIZE)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CONNECT FOUR")

    # Board display setup
    display.board_setup(SCREEN, player, FONT)
    pygame.display.update()

    # Main loop
    while not game.game_over:

        # Event handler
        for event in pygame.event.get():
            # Close window
            if event.type == pygame.QUIT:
                logger.log_event("QUIT")
                game.game_over = True
                game.game_quit = True

            elif event.type == pygame.KEYDOWN:
                # Escape to end
                if event.key == pygame.K_ESCAPE:
                    logger.log_event("QUIT")
                    game.game_over = True
                    game.game_quit = True

                # Move input
                for move in range(COLS):
                    if event.key == getattr(pygame, f"K_{move+1}"):  # Column input starts from 1

                        # Validate move
                        if game.valid_move(move) == True:
                            game.place_piece(move, player)
                            display.update_board(SCREEN)

                            # If game over
                            if game.check_win(player):
                                logger.log_event(f"END:PLAYER_{player}.WINS")
                                winner_color = globals()[f"P{player}_COLOR"]
                                display.board_top_text(f"PLAYER {player} WINS!", FONT, SCREEN, winner_color)
                                game.game_over = True
                                break
                            elif game.check_draw():
                                logger.log_event(f"END:DRAW")
                                display.board_top_text(f"DRAW", FONT, SCREEN)
                                game.game_over = True
                                break

                            # Next player
                            player = turn % 2 + 1
                            turn += 1
                            display.board_top_text(f"PLAYER {player} TURN", FONT, SCREEN)

                        # If invalid move
                        else:
                            logger.log_event(f"PLAYER_{player}.INVALID.move.FULL_COLUMN")

        # Update display
        pygame.display.update()

        # Wait time
        if game.game_over == True and game.game_quit == False:
            logger.log_event(f"TOTAL_TURNS:{turn}")
            pygame.time.wait(STALL_TIME)

    # Close Pygame
    pygame.quit()


# Import const from file
setup = FileSetup()
setup.setup_from_file(SETUP_FILE)

# Const calculations
WIDTH = COLS * UNIT_SIZE
HEIGHT = (ROWS + EXTRA_ROWS) * UNIT_SIZE
RADIUS = UNIT_SIZE / 2 - 5
FONT_SIZE = int(UNIT_SIZE * 0.75)

# Run game
connect_four_game()

# Export log
logger = Logger()
logger.export_log_to_txt()