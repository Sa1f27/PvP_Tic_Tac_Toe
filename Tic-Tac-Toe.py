import tkinter as tk
from tkinter import simpledialog

# Initialize the main window
root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

# Player names and symbols
player1_name = "Player 1"
player2_name = "Player 2"
player1_symbol = "X"
player2_symbol = "O"

def set_player_names():
    global player1_name, player2_name
    player1_name = simpledialog.askstring("Player 1", "Enter name for Player 1:")
    player2_name = simpledialog.askstring("Player 2", "Enter name for Player 2:")
    if player1_name and player2_name:
        status_label.configure(text=f"{player1_name}'s turn")

def play_again():
    global current_chr
    current_chr = player1_symbol
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text=f"{player1_name}'s turn")
    play_again_button.pack_forget()

def reset_game():
    global player1_symbol, player2_symbol
    set_player_names()

def disable_game():
    for point in XO_points:
        point.button.configure(state=tk.DISABLED)
    play_again_button.pack()

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

# Set up the main UI elements
tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()
status_label = tk.Label(root, text="Enter names to start", font=('Ariel', 15), bg='green', fg='snow')
status_label.pack(fill=tk.X)

play_again_button = tk.Button(root, text='Play again', font=('Ariel', 15), command=play_again)
reset_button = tk.Button(root, text='Reset Game', font=('Ariel', 15), command=reset_game)

play_area = tk.Frame(root, width=300, height=300, bg='white')
XO_points = []
X_points = []
O_points = []

for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))

play_area.pack(pady=10, padx=10)
reset_button.pack(pady=10)

# Start the player naming dialog
set_player_names()

# Start the main loop
root.mainloop()
