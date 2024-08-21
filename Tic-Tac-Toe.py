import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

# Initialize variables for player names and symbols
player1_name = "P1"
player2_name = "P2"
player1_symbol = "X"
player2_symbol = "O"
current_chr = player1_symbol

# Function to set player names and update the status label
def set_player_names():
    global player1_name, player2_name
    player1_name = player1_name_entry.get()
    player2_name = player2_name_entry.get()
    if player1_name and player2_name:
        status_label.configure(text=f"{player1_name}'s turn")
        player_name_frame.pack_forget()
        play_area.pack(pady=10, padx=10)
        reset_button.pack(pady=10)

# Function to start a new game
def play_again():
    global current_chr
    current_chr = player1_symbol
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text=f"{player1_name}'s turn")
    play_again_button.pack_forget()

# Function to reset the game
def reset_game():
    global player1_symbol, player2_symbol
    set_player_names()

# Function to disable the game (when there's a win or draw)
def disable_game():
    for point in XO_points:
        point.button.configure(state=tk.DISABLED)
    play_again_button.pack()

# Function to check for win or draw conditions
def check_win():
    for possibility in winning_possibilities:
        if possibility.check(player1_symbol):
            status_label.configure(text=f"{player1_name} won!")
            disable_game()
            return
        elif possibility.check(player2_symbol):
            status_label.configure(text=f"{player2_name} won!")
            disable_game()
            return
    if len(X_points) + len(O_points) == 9:
        status_label.configure(text="Draw!")
        disable_game()

# Class representing a point on the Tic Tac Toe board
class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set, bg='lightgray')
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            if current_chr == player1_symbol:
                X_points.append(self)
                current_chr = player2_symbol
                status_label.configure(text=f"{player2_name}'s turn")
            elif current_chr == player2_symbol:
                O_points.append(self)
                current_chr = player1_symbol
                status_label.configure(text=f"{player1_name}'s turn")
            check_win()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == player1_symbol:
            X_points.remove(self)
        elif self.value == player2_symbol:
            O_points.remove(self)
        self.value = None

# Class representing a winning possibility (for rows, columns, and diagonals)
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def check(self, for_chr):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        if for_chr == player1_symbol:
            for point in X_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_chr == player2_symbol:
            for point in O_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])

# Define winning possibilities
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]

# Set up the UI elements
tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

# Frame for entering player names
player_name_frame = tk.Frame(root)
tk.Label(player_name_frame, text="Player 1 Name:", font=('Ariel', 15)).grid(row=0, column=0, padx=5, pady=5)
player1_name_entry = tk.Entry(player_name_frame, font=('Ariel', 15))
player1_name_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(player_name_frame, text="Player 2 Name:", font=('Ariel', 15)).grid(row=1, column=0, padx=5, pady=5)
player2_name_entry = tk.Entry(player_name_frame, font=('Ariel', 15))
player2_name_entry.grid(row=1, column=1, padx=5, pady=5)
set_names_button = tk.Button(player_name_frame, text="Set Names", font=('Ariel', 15), command=set_player_names)
set_names_button.grid(row=2, column=0, columnspan=2, pady=10)

# Status label
status_label = tk.Label(root, text="Enter names to start", font=('Ariel', 15), bg='green', fg='snow')
status_label.pack(fill=tk.X)

# Buttons for gameplay control
play_again_button = tk.Button(root, text='Play again', font=('Ariel', 15), command=play_again)
reset_button = tk.Button(root, text='Reset Game', font=('Ariel', 15), command=reset_game)

# Play area
play_area = tk.Frame(root, width=300, height=300, bg='white')
XO_points = []
X_points = []
O_points = []

# Create the grid of XOPoints
for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))

# Pack the player name entry frame
player_name_frame.pack(pady=10)

# Start the main loop
root.mainloop()
