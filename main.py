import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def click(self, index):
        if not self.board[index]:
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                return True
        return False

    def reset(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
