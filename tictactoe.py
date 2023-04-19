import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.game_over = False

    def check_for_winner(self):
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '-':
                return self.board[i][0]

        # check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '-':
                return self.board[0][i]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            return self.board[0][2]

        # no winner yet
        return None

    def make_move(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToe()
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, width=10, height=5,
                                   font=('Helvetica', 24, 'bold'),
                                   command=lambda row=i, col=j: self.button_clicked(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.window, text="Reset", font=('Helvetica', 20),
                                      command=self.reset_game)
        self.reset_button.grid(row=3, column=1)

    def button_clicked(self, row, col):
        if not self.game.game_over:
            if self.game.make_move(row, col):
                self.buttons[row][col]['text'] = self.game.current_player
                winner = self.game.check_for_winner()
                if winner:
                    self.game.game_over = True
                    messagebox.showinfo("Game Over", f"{winner} wins!")
                else:
                    self.game.switch_player()

    def reset_game(self):
        self.game = TicTacToe()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = '-'
        self.game_over = False

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = TicTacToeGUI()
    app.run()
