class GameFunctions():

    @staticmethod
    def move(board, piece, dest, is_p1, last_moves):
        if(len(piece) != 2 or len(dest) != 2):
            return -1, -1

        p_x = GameFunctions.change_type(piece[0])
        p_y = int(piece[1])-1

        if(p_x not in [0, 1, 2, 3, 4, 5]):
            return -1, -1
        if(p_y not in [0, 1, 2, 3, 4, 5]):
            return -1, -1
        if(is_p1 and board[p_x][p_y] != "X"):
            return -1, -1
        if((not is_p1) and board[p_x][p_y] != "O"):
            return -1, -1

        d_x = GameFunctions.change_type(dest[0])
        d_y = int(dest[1])-1

        if(d_x not in [0, 1, 2, 3, 4, 5]):
            return -1, -1
        if(d_y not in [0, 1, 2, 3, 4, 5]):
            return -1, -1
        if(p_x != d_x and p_y != d_y):   # No diagonal moves.
            return -1, -1

        if(p_x == d_x and (abs(d_y-p_y) != 1) or
           p_y == d_y and (abs(d_x-p_x) != 1)):
            return -1, -1

        if(last_moves[0] == d_x and last_moves[1] == d_y and
           last_moves[2] == p_x and last_moves[3] == p_y):
            return -1, -1

        if(board[d_x][d_y] == "e"):
            board[d_x][d_y] = board[p_x][p_y]
            board[p_x][p_y] = "e"

            last_moves[0], last_moves[1] = p_x, p_y
            last_moves[2], last_moves[3] = d_x, d_y

            board = GameFunctions.delete(board)
            return board, last_moves
        else:
            return -1, -1

    @staticmethod
    def find_liberties(board):

        # I may need to use actual liberty
        # values instead of boolean values,
        # it would be better for a heuristic function.

        liberties= [[True, True, True, True, True, True],
                    [True, True, True, True, True, True],
                    [True, True, True, True, True, True],
                    [True, True, True, True, True, True],
                    [True, True, True, True, True, True],
                    [True, True, True, True, True, True]]

        for i in range(6):
            for j in range(6):
                if(board[i][j] == "e"):
                    liberties[i][j] = True
                else:
                    liberties[i][j] = False
        
        for k in range(10):
            for i in range(6):
                for j in range(6):
                    if(board[i][j] != "e"):
                        if(board[i][j] == "O"):
                            t = "X"   # t is opponent.
                        else:
                            t = "O"   # t is opponent.
                        
                        if(j-1 >= 0 and board[i][j-1] != t and liberties[i][j-1]):
                            liberties[i][j] = True
                        elif(i-1 >= 0 and board[i-1][j] != t and liberties[i-1][j]):
                            liberties[i][j] = True
                        elif(j+1 <= 5 and board[i][j+1] != t and liberties[i][j+1]):
                            liberties[i][j] = True
                        elif(i+1 <= 5 and board[i+1][j] != t and liberties[i+1][j]):
                            liberties[i][j] = True
        
        return liberties
    
    @staticmethod
    def delete(board):
        liberties = GameFunctions.find_liberties(board)

        for i in range(6):
            for j in range(6):
                if(board[i][j] != "e" and not liberties[i][j]):
                    board[i][j] = "e"
        
        return board
    
    @staticmethod
    def is_terminal(board, last_moves_x, last_moves_o):
        board = GameFunctions.delete(board)

        valid_move_x = False   # Check if player1 has any valid moves.
        valid_move_o = False   # Check if player2 has any valid moves.
        
        for k in range(2):
            if(k==0):
                p = "X"
                last_p_x, last_p_y = last_moves_x[0], last_moves_x[1]
                last_d_x, last_d_y = last_moves_x[2], last_moves_x[3]
            elif(k==1):
                p = "O"
                last_p_x, last_p_y = last_moves_o[0], last_moves_o[1]
                last_d_x, last_d_y = last_moves_o[2], last_moves_o[3]

            valid_move = False
            
            # If there are no pieces left for either player,
            # board[i][j] == p part will never be true and
            # consequently valid_move will stay False.

            for i in range(6):
                for j in range(6):
                    if(board[i][j] == p and last_d_x != i and last_d_y != j ):
                        if(j-1 >= 0 and board[i][j-1] == "e" and last_p_x != i and last_p_y != j-1):
                            valid_move = True
                        if(i-1 >= 0 and board[i-1][j] == "e" and last_p_x != i-1 and last_p_y != j):
                            valid_move = True
                        if(j+1 <= 5 and board[i][j+1] == "e" and last_p_x != i and last_p_y != j+1):
                            valid_move = True
                        if(i+1 <= 5 and board[i+1][j] == "e" and last_p_x != i+1 and last_p_y != j):
                            valid_move = True

            if(k==0):
                valid_move_x = valid_move
            elif(k==1):
                valid_move_o = valid_move

        # Is the game terminated, if p1 has valid moves, if p2 has valid moves
        return (not (valid_move_x and valid_move_o)), valid_move_x, valid_move_o
    
    @staticmethod
    def change_type(i):
        letters = ["a", "b", "c", "d", "e", "f"]

        if(type(i) == int):
            return letters[i]
        elif(type(i) == str):
            return letters.index(i)
        return -1

    @staticmethod
    def is_valid(board, piece, dest):
        p_x, p_y = GameFunctions.change_type(piece[0]), int(piece[1])-1
        d_x, d_y = GameFunctions.change_type(dest[0]), int(dest[1])-1