from game_modules.game_class import GameClass

mode = 0
while(mode not in ["1", "2"]):
    mode = input("To be player 1, enter 1\nTo be player 2, enter 2:\n")
    if(mode == "1"):
        is_p1 = True   # If user is player1.
    elif(mode == "2"):
        is_p1 = False  # If user is player2.
    else:
        print("Enter either 1 or 2.")

turn = -1
while(turn <= 0):
    turn = int(input("Enter the max. number of turns: "))
    if(turn <= 0):
        print("Max. turn number should be a positive integer.")

game = GameClass()

game.print_board()
print()

terminated = False

#if(is_p1):
while(turn > 0 and not terminated):
    piece = input("Choose piece to move: ")
    dest = input("Choose the new position for " + piece + ": ")

    if(game.move(piece, dest, is_p1) == 1):
        print("Player moves the piece at " + piece + " to " + dest)
        terminated, p1_win, p2_win = game.is_terminal()
        game.print_board()
        turn -= 1

if(p1_win):
    print("Player1 has won!")
elif(p2_win):
    print("Player2 has won!")
elif(turn == 0):
    print("Game has reached the turn limit.")
    # game.calculate_scores()

#else:
#    print("Work in progress.")