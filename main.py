import tkinter #To create graphical user interface (GUIs)

def set_title(row, column):
    global current_player #Access the global variable to track whose turn it is

    #Stops the function if the game is already over
    if (game_over):
        return

    #If the clicked cell is already occupied, do nothing
    if board[row][column]["text"] != "":
        return

    #Set the text of the clicked cell to the current player's symbol ("X" or "O")
    board[row][column]["text"] = current_player

    #Switch to the other player for the next turn
    if current_player == player_O:
        current_player = player_X
    else:
        current_player = player_O

    #Update the label to show whose turn it is
    label["text"] = current_player + "'s turn"

    winner()

def winner():
    global turns, game_over
    turns += 1

    #Check each row for winning combination
    for row in range(3): #Loop through all 3 rows (0, 1, 2)
        #Check if all 3 buttons in the current row have the same non-empty text
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            #Update the label to announce the winner (text from that column)
            label.config( 
                text = board[row][0]["text"] + " is the winner!", 
                foreground = color_yellow
            )
            #Highlight all 3 winning buttons in the row
            for column in range(3): #Loop over each column in the current row
                board[row][column].config(
                    foreground = color_yellow, 
                    background = color_light_gray
                )
            game_over = True #Set the game_over to stop further playing
            return #Exit the function after detecting a win
    
    #Check each column for a winning combination
    for column in range(3): #Loop through all 3 columns (0, 1, 2)
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(
                text = board[0][column]["text"] + " is the winner!", 
                foreground = color_yellow
            )
            #Highlight all 3 winning buttons in the column
            for row in range(3): #Loop over each column in the current column
                board[row][column].config(
                    foreground = color_yellow, 
                    background = color_gray
                )
            game_over = True #Set the game_over to setop further playing
            return #Exit the function after detecting a win
    
    #Check each diagonal for a winning combination
    for column in range(3):
        if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
            label.config(
                text = board[0][2]["text"] + " is the winner!",
                foreground = color_yellow
            )
            board[0][2].config(
                foreground = color_yellow, 
                background = color_light_gray
            )
            board[1][1].config(
                foreground = color_yellow,
                background = color_light_gray
            )
            board[2][0].config(
                foreground = color_yellow,
                background = color_light_gray
            )
            game_over = True
            return
    
    #Check if tie
    if (turns == 9):
        game_over = True
        label.config(
            text = "Tie!", 
            foreground = color_yellow
        )

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text = current_player + "'s turn", foreground = "white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(
                text = "", 
                foreground = color_blue, 
                background = color_gray
            )

#Game setup
player_X = "X"
player_O = "O"
current_player = player_X

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b4"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False

#-------------Window Setup-------------
window = tkinter.Tk() #Create the game window
window.title("Tic Tac Toe")
window.resizable(False, False) #Disable window resizing (Both Horizontal & Vertical)
#-------------Window Setup-------------

frame = tkinter.Frame(window) #Create a frame widget inside the main window to organize other widgets

#-------------Create a label widget inside the frame-------------
label = tkinter.Label(
    frame, 
    text = current_player + "'s turn", 
    font = ("Consalas", 20), 
    background = color_gray,
    foreground = "white"
    ) #Display the current player's turn with modified font & background
#-------------Create a label widget inside the frame------------- 


for row in range(3):
    for column in range(3):
        #Create a button for each cell in the 3x3 grid
        board[row][column] = tkinter.Button(
            frame, 
            text = "", #Empty button text
            font = ("Consales", 50, "bold"), #Big, bold font
            background = color_gray, 
            foreground = color_blue, 
            width = 4, 
            height = 1, 
            #Use lambda to pass the current row and column to the set_title function
            command = lambda row = row, column = column: set_title(row, column) 
        )
        board[row][column].grid(row = row + 1, column = column) #Place button in grid (row +1 to leave space for label)

#-------------Create a Restart Button to reset the game-------------
button = tkinter.Button(
    frame, 
    text = "Restart", 
    font = ("Consolar", 20), 
    background = color_gray,
    foreground = "white",
    command = new_game
)
#-------------Create a Restart Button to reset the game-------------

button.grid(
    row = 4, 
    column = 0, 
    columnspan = 3, 
    sticky = "we" #'w' = west (left), 'e' = east (right) → stretch horizontally
) 

label.grid(
    row = 0, 
    column = 0, 
    columnspan = 3, 
    sticky = "we" #'w' = west (left), 'e' = east (right) → stretch horizontally
)

frame.pack() #Add the frame to the window using the pack layout manager

#-------------Center the window-------------
window.update() #Updates window to get correct width & height

#Tkinter App Window
window_width = window.winfo_width() #Get window's width
window_height = window.winfo_height() #Get window's height

#Monitor Resolution
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#Standard Formula to center a Tkinter window
window_x = int((screen_width/2) - (window_width/2)) #X position to center the window
window_y = int((screen_height/2) - (window_height/2)) #Y position to center the window

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")  
#-------------Center the window-------------

window.mainloop() #Keeps the window open until the user closes it