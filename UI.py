import tkMessageBox
from Tkinter import *
from logic import TicTacToe

root = Tk()
game = TicTacToe()

grid = [
    [StringVar(), StringVar(), StringVar()],
    [StringVar(), StringVar(), StringVar()],
    [StringVar(), StringVar(), StringVar()]
]

root.resizable(width=FALSE, height=FALSE)
root.wm_title("TicTacToe, Player " + str(game.get_player()) + " select a cell")


def new_game():
    global game
    global grid

    game = TicTacToe()
    update_title()

    for i in range(3):
        for j in range(3):
            grid[i][j].set(' ')


def update_title(message=None):
    if message is None:
        root.wm_title("TicTacToe, Player " +
                      str(game.get_player()) +
                      " select a cell")
    else:
        root.wm_title(message)


def label_click(event, row, column):
    message = game.click(row, column)

    update_title(message)

    for i in range(3):
        for j in range(3):
            if game.board[i][j] != '.':
                grid[i][j].set(game.board[i][j])

    if game.get_winner() != 0:
        tkMessageBox.showinfo("Winner", "player %d is the winner"
                              % game.get_player())


colors = ["white", "gray"]
for i in range(3):
    for j in range(3):
        label = Label(root, bg=colors[0], fg=colors[1], height=5, width=15,
                      textvariable=grid[i][j])
        label.bind('<Button-1>',
                   lambda event, r=i, c=j: label_click(event, r, c))

        label.grid(row=i, column=j)
        colors.reverse()

b = Button(root, text="New Game", command=new_game)
b.grid(row=3, column=1)

root.mainloop()
