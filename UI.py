import tkMessageBox
from Tkinter import *
from logic import TicTacToe


class TicTacToeTk:
    def __init__(self, size):
        self.size = size
        self.game = TicTacToe(size)
        self.root = self.create_root_window()
        self.grid = self.create_grid()

        b = Button(self.root, text=":)",
                   command=self.on_click_new_game)
        b.grid(row=self.size, column=1)

    def run(self):
        self.root.mainloop()

    def create_root_window(self):
        root = Tk()
        root.resizable(width=FALSE, height=FALSE)
        return root

    def create_grid(self):
        grid = [[
            StringVar() for j in range(self.size)
        ] for i in range(self.size)]

        colors = ["white", "gray"]

        for i in range(self.size):
            for j in range(self.size):
                label = Label(self.root,
                              bg=colors[(i + j) % 2],
                              fg=colors[(i + j + 1) % 2],
                              height=3, width=8,
                              textvariable=grid[i][j])
                label.bind('<Button-1>',
                           lambda event, r=i, c=j: self.on_click_cell(r, c))

                label.grid(row=i, column=j)

        return grid

    def on_click_new_game(self):
        self.game.reset()
        self.update_view()

    def on_click_cell(self, row, column):
        self.game.click(row, column)
        self.update_view()
        winner = self.game.get_winner()
        if winner != 0:
            tkMessageBox.showinfo("Winner",
                                  "Player %d is the winner!" % winner)
        elif not self.game.have_empty_cell():
            tkMessageBox.showinfo("Draw",
                                  "Game ended without a winner!")

    def update_view(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.game.board[i][j] != '.':
                    self.grid[i][j].set(self.game.board[i][j])
                else:
                    self.grid[i][j].set('')

TicTacToeTk(4).run()
