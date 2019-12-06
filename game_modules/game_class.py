from game_modules.game_functions import GameFunctions as gf

class GameClass():
    def __init__(self):

        self.board=[["X", "X", "e", "e", "O", "O"],
                    ["X", "X", "e", "e", "O", "O"],
                    ["e", "e", "e", "e", "e", "e"],
                    ["e", "e", "e", "e", "e", "e"],
                    ["O", "O", "e", "e", "X", "X"],
                    ["O", "O", "e", "e", "X", "X"]]
        
        self.liberties=[[True, True, True, True, True, True],
                        [True, True, True, True, True, True],
                        [True, True, True, True, True, True],
                        [True, True, True, True, True, True],
                        [True, True, True, True, True, True],
                        [True, True, True, True, True, True]]

                                           # Order is:
        self.last_moves_x = [0, 0, 0, 0]   # moved piece's x, moved piece's y, destination x, destination y
        self.last_moves_o = [0, 0, 0, 0]   # p_x, p_y, d_x, d_y

    def move(self, piece, dest, is_p1):
        if(is_p1):
            last_moves = self.last_moves_x   # Order should be exactly
        else:                                # p_x, p_y, d_x, d_y
            last_moves = self.last_moves_o

        valid_board, last_moves = gf.move(self.board, piece, dest, is_p1, last_moves)

        if(valid_board == -1):
            print("Please make a valid move!")
            return -1

        self.board = valid_board

        if(is_p1):
            self.last_moves_x = last_moves
        else:
            self.last_moves_o = last_moves
        
        return 1

    def is_terminal(self):
        terminated, p1_win, p2_win = gf.is_terminal(self.board, self.last_moves_x, self.last_moves_o)
        return terminated, p1_win, p2_win

    def print_board(self):
        print("   1 2 3 4 5 6")
        for i in range(6):
            print(gf.change_type(i), end=" |")
            for j in range(6):
                if(self.board[i][j] == "e"):
                    print(" ", end="|")
                else:
                    print(self.board[i][j], end="|")
            print()
    
    def get_last_moves(self):
        return self.last_moves_x, self.last_moves_o