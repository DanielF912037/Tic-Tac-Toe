import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = [" " for _ in range(9)]  # represents a 3x3 board

# initialize player (x goes first)
current_player = "X"


# function to handle button clicks
def button_click(index):
    global current_player

    # check if button is clicked or game is over
    if board[index] == " " and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player)
        current_player = "O" \
            if current_player == "X" \
            else "X"
        check_winner()


# Function to check for if a winner or a draw
def check_winner():
    for combination in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        a, b, c = combination
        if board[a] == board[b] == board[c] != " ":
            messagebox.showinfo("Tic-Tac-Toe", f"Player {board[a]} wins!")
            reset_board()
            return True

    if " " not in board:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_board()
        return True

    return False


# Function to reset the game board
def reset_board():
    global current_player
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ")
    current_player = "X"


# create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the game board
buttons = [tk.Button(window, text=" ", font=('normal', 20), width=7, height=3, command=lambda i=i: button_click(i)) for i in range(9)]

# Grid layout for buttons
for i in range(3):
    for j in range(3):
        buttons[i * 3 + j].grid(row=i, column=j)

# Create a "Reset" button
reset_button = tk.Button(window, text="Reset", font=('normal', 14), command=reset_board)
reset_button.grid(row=3, column=1)

# Start the main loop
window.mainloop()