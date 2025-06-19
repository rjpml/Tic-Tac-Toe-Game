import tkinter #To create graphical user interface (GUIs)

def set_title(row, column):
    global current_player

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player 

    if current_player == player_O:
        current_player = player_X
    else:
        current_player = player_O

    label["text"] = current_player + "'s turn"

def new_game():
    pass

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

#--------Window Setup--------
window = tkinter.Tk() #Create the game window
window.title("Tic Tac Toe")
window.resizable(False, False) #Disable window resizing (Both Horizontal & Vertical)
#--------Window Setup--------

frame = tkinter.Frame(window) #Create a frame widget inside the main window to organize other widgets

#---------Create a label widget inside the frame---------
label = tkinter.Label(
    frame, 
    text = current_player + "'s turn", 
    font = ("Consalas", 20), 
    background = color_gray,
    foreground = "white"
    ) #Display the current player's turn with modified font & background
#---------Create a label widget inside the frame--------- 


for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame, 
            text = "", #Empty button text
            font = ("Consales", 50, "bold"), #Big, bold font
            background = color_gray, 
            foreground = color_blue, 
            width = 4, 
            height = 1, 
            command = lambda row = row, column = column: set_title(row, column) #Button calls set_title with its row and column
        )
        board[row][column].grid(row = row + 1, column = column) #Place button in grid (row +1 to leave space for label)

button = tkinter.Button(
    frame, 
    text = "Restart", 
    font = ("Consolar", 20), 
    background = color_gray,
    foreground = "white",
    command = new_game
    )

button.grid(row = 4, column = 0, columnspan = 3, sticky = "we") #Place button on row 4, span 3 columns, stretch horizontally

label.grid(row = 0, column = 0, columnspan = 3, sticky = "we") #Place label at top row, span all 3 columns, stretch horizontally
frame.pack() #Add the frame to the window using the pack layout manager

#-------------Center the window-------------
window.update() #Updates window to get correct width & height

#Tkinter App Window
window_width = window.winfo_width() #Get window's width
window_height = window.winfo_height() #Get window's height

#Monitr Resolution
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#Standard Formula to center a Tkinter window
window_x = int((screen_width/2) - (window_width/2)) #X position to center the window
window_y = int((screen_height/2) - (window_height/2)) #Y position to center the window

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")  
#-------------Center the window-------------


window.mainloop() #Keeps the window open until the user closes it