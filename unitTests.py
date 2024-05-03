import unittest
from connectFour import ConnectFour,ROWS,COLS

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.game = ConnectFour(ROWS, COLS)

    def test_place_piece(self):
        self.game.place_piece(0, 1)
        self.assertEqual(self.game._board[5][0], 1) #Player 1 piece placed in the bottom row of the first column

        self.game.place_piece(0, 2)
        self.assertEqual(self.game._board[4][0], 2) #Player 2 piece placed on top of the 1st player piece

    def test_valid_move(self):
        #All moves are valid
        for col in range(COLS):
            self.assertTrue(self.game.valid_move(col))
        
        #Fill up 1st column
        for _ in range(ROWS):
            self.game.place_piece(0, 1)
        
        #1st column move is invalid
        self.assertFalse(self.game.valid_move(0)) 

        #All other columns remain valid (except 1st col)
        for col in range(1, COLS): 
            self.assertTrue(self.game.valid_move(col))

    def test_check_win_horizontal(self):
        #Place player 1 pieces horizontally on the board
        self.game._board[0][0]=1
        self.game._board[0][1]=1
        self.game._board[0][2]=1
        self.game._board[0][3]=1
        self.assertTrue(self.game.check_win(1))  # Player 1 should win horizontally

        #Place player 2 pieces horizontally on the board
        self.game._board[5][3]=2
        self.game._board[5][4]=2
        self.game._board[5][5]=2
        self.game._board[5][6]=2
        self.assertTrue(self.game.check_win(2)) # Player 2 should win horizontally

    def test_check_win_vertical(self):
        #Place player 1 pieces vertically on the board
        self.game._board[0][0]=1
        self.game._board[1][0]=1
        self.game._board[2][0]=1
        self.game._board[3][0]=1

        self.assertTrue(self.game.check_win(1))  #Player 1 should win vertically

        #Place player 2 pieces vertically on the board
        self.game._board[2][6]=2
        self.game._board[3][6]=2
        self.game._board[4][6]=2
        self.game._board[5][6]=2
        self.assertTrue(self.game.check_win(2)) #Player 2 should win vertically

    def test_check_win_diagonal(self):
        #Place player 1 pieces diagonally (sloped positively) on the board
        self.game._board[5][0]=1
        self.game._board[4][1]=1
        self.game._board[3][2]=1
        self.game._board[2][3]=1
        self.assertTrue(self.game.check_win(1)) #Player 1 should win diagonally
        
        #Place player 1 pieces diagonally (sloped negatively) on the board
        self.game._board[5][6]=2
        self.game._board[4][5]=2
        self.game._board[3][4]=2
        self.game._board[2][3]=2
        self.assertTrue(self.game.check_win(2)) #Player 2 should win diagonally


    def test_check_draw(self):
        self.assertFalse(self.game.check_draw())  #No draw at the start of the game
        # Fill the entire board with alternating pieces
        for i in range(ROWS):
            for j in range(COLS):
                if (i + j) % 2 == 0:
                    self.game.place_piece(j, 1)
                else:
                    self.game.place_piece(j, 2)
        self.assertTrue(self.game.check_draw())  # The game should be a draw when the board is full

unittest.main()