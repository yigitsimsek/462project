from game_modules.game_functions import GameFunctions as gf

class GameAgent():

    def __init__(self, is_p1):
        self.is_p1 = is_p1
        self.pieces = []
    
    def decide(self, board, last_moves_x, last_moves_o):
        if(self.is_p1):
            p = "X"
        else:
            p = "O"

        for i in range(6):
            for j in range(6):
                if(board[i][j] == p):
                    self.pieces.append(gf.change_type(i) + str(j+1))

        depth = 10

        self.minimax(board, depth, last_moves_x, last_moves_o)

    def minimax(self, board, depth, last_moves_x, last_moves_o):
        action = self.max_value(board, depth, last_moves_x, last_moves_o)
        return action

    # Returns a utility value.
    def max_value(self, board, depth, last_moves_x, last_moves_o):
        if(depth == 0):
            return self.calculate_score(board)
        else:
            val = float('-inf')

            actions = []
            for piece in self.pieces:
                p_x, p_y = gf.change_type(piece[0]), int(piece[1])-1
                
                if(self.is_p1):
                    if(p_y-1 >= 0):
                        dest = gf.change_type(p_x) + str(p_y)
                        gf.move(board, piece, dest, self.is_p1, last_moves_x)
                    if(p_x-1 >= 0):
                        dest = gf.change_type(p_x-1) + str(p_y+1)
                        gf.move(board, piece, dest, self.is_p1, last_moves_x)
                    if(p_y+1 <= 5):
                        dest = gf.change_type(p_x) + str(p_y+2)
                        gf.move(board, piece, dest, self.is_p1, last_moves_x)
                    if(p_x+1 <= 5):
                        dest = gf.change_type(p_x+1) + str(p_y+1)
                        if(gf.move(board, piece, dest, self.is_p1, last_moves_x))
                else:
                    if(p_y-1 >= 0):
                        dest = gf.change_type(p_x) + str(p_y)
                        gf.move(board, piece, dest, self.is_p1, last_moves_o)
                    if(p_x-1 >= 0):
                        dest = gf.change_type(p_x-1) + str(p_y+1)
                        gf.move(board, piece, dest, self.is_p1, last_moves_o)
                    if(p_y+1 <= 5):
                        dest = gf.change_type(p_x) + str(p_y+2)
                        gf.move(board, piece, dest, self.is_p1, last_moves_o)
                    if(p_x+1 <= 5):
                        dest = gf.change_type(p_x+1) + str(p_y+1)
                        gf.move(board, piece, dest, self.is_p1, last_moves_o)


    def min_value(self, board, depth, last_moves):
        print("min in progress.")
                    


    def calculate_score(self, board):
        return 1
    