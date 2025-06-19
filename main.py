import tkinter #To create graphical user interface (GUIs)

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

#Window Setup
window = tkinter.Tk() #Create the game window
window.title("Tic Tac Toe")
window.resizable(False, False) #Disable window resizing (Both Horizontal & Vertical)

frame = tkinter.Frame(window) #Create a frame widget inside the main window to organize other widgets

#Create a label widget inside the frame
label = tkinter.Label(frame, text = current_player + "'s turn", font = ("Consalas", 20), background = color_gray,
                      foreground = "white") #Display the current player's turn with modified font & background

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text = "", font = ("Consales", 50, "bold"),
                                                                      background = color_gray, foreground = color_blue, 
                                                                      width = 4, height = 1)

label.grid(row = 0, column = 0)
frame.pack() #Add the frame to the window using the pack layout manager

window.mainloop() #Keeps the window open until the user closes it