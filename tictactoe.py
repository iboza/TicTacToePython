import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    PLAYER_X = "X"
    PLAYER_O = "O"

    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.player_turn = TicTacToe.PLAYER_X
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(master, text="", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        # Centrar la ventana en el centro del monitor
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = int((screen_width / 2) - (master.winfo_width() / 2))
        y = int((screen_height / 5) - (master.winfo_height() / 2))
        master.geometry(f"+{x}+{y}")

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.player_turn
            self.buttons[row][col].config(text=self.player_turn)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player_turn} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.player_turn = TicTacToe.PLAYER_O if self.player_turn == TicTacToe.PLAYER_X else TicTacToe.PLAYER_X

    def check_winner(self):
        # Verificar filas
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Verificar columnas
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        # Verificar diagonales
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.player_turn = TicTacToe.PLAYER_X
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
