# ----- Global Variables -----

#Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#If game is still going
game_still_going = True

#Who won? or Tie?
winner = None

#Who turn is it?
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play a game of tic tac toe
def play_game():

    display_board()

    #While the game is still going
    while game_still_going:
        
        #Handle single turn of an arbitrary player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#Handle single turn of an arbitrary player
def handle_turn(player):
    position = input("Choose a position from 1-9: ")

    #Convert the input from string to integer,
    #then subtract 1 to match Python's 0-based index
    #(User thinks in 1–9, but Python uses 0–8)
    #We only subtract 1 for the code's logic,
    #because Python list indexing starts at 0, not 1.
    position = int(position) - 1

    board[position] = "X"

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #Setup global variable
    global winner

    #Check rows
    row_winner = check_row()
    #Check column
    column_winner = check_column()
    #Check diagonals
    diagonal_winner = check_diagonals()

    #Get the winner
    if row_winner:
        winner = row_winner()
    elif column_winner:
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None
    return

def check_row():
    return

def check_column():
    return

def check_diagonals():
    return

def check_if_tie():
    return

def flip_player():
    return

play_game()