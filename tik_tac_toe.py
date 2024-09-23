import tkinter as tk
from tkinter import messagebox

# Create the main game class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize the board
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        # Create buttons for the 3x3 grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text=" ", font=("Arial", 40), width=5, height=2,
                                                   command=lambda r=row, c=col: self.on_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 20), command=self.reset_game)
        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 20), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=1)
        self.play_again_button.grid(row=3, column=2, columnspan=2)

    # Handle button click
    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.is_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken.")

    # Check if there is a winner
    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for row in self.board:
            if row.count(player) == 3:
                return True
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count(player) == 3:
                return True
        if [self.board[i][i] for i in range(3)].count(player) == 3:
            return True
        if [self.board[i][2-i] for i in range(3)].count(player) == 3:
            return True
        return False

    # Check if the game is a draw
    def is_draw(self):
        return all([self.board[row][col] != " " for row in range(3) for col in range(3)])

    # Disable buttons after the game is over
    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"

    # Reset the game
    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = " "
                self.buttons[row][col]["state"] = "normal"

# Main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
