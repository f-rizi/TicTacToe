class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.reset()

    # This function is called whenever a new game is started.
    # all the cells in the board are set to '.'
    # that shows nobody has selected these cells
    def reset(self):
        self.board = [['.'] * self.size for i in range(self.size)]
        self.player = 0

    def click(self, row, column):
        if not self.have_empty_cell():
            return "game is finished, start a new one"

        winner = self.get_winner()

        # If someone has won the game, do nothing
        if winner != 0:
            return "player %d won the game, start a new one" \
                   % self.get_player()

        # If clicked cell is already selected do nothing
        if self.board[row][column] != ".":
            return "This cell is not empty, select another cell"

        self.player = (self.player + 1) % 2

        if self.player == 1:
            self.board[row][column] = "X"
        else:
            self.board[row][column] = "O"

        winner = self.get_winner()

        if winner != 0:
            return "player %d is the winner" % self.get_player()

    def have_empty_cell(self):
        for i in range(self.size):
            if "." in self.board[i]:
                return True

    def get_winner(self):
        cols_rows_diags = self.get_cols_rows_diags()

        if ["X"] * self.size in cols_rows_diags:
            return 1
        elif ["O"] * self.size in cols_rows_diags:
            return 2

        return 0

    # This function returns a list containing all the rows,
    # columns and two diagonals of the board. This list will
    #  be used to determine the winner.
    def get_cols_rows_diags(self):
        cols_rows_diags = []

        # diagonal
        cols_rows_diags.append([self.board[i][i] for i in range(self.size)])

        # reverse diagonal
        cols_rows_diags.append([self.board[self.size - i - 1][i]
                                for i in range(self.size)])

        for i in range(self.size):
            # ith row
            cols_rows_diags.append([self.board[i][j]
                                    for j in range(self.size)])
            # ith column
            cols_rows_diags.append([self.board[j][i]
                                    for j in range(self.size)])

        return cols_rows_diags

    def get_player(self):
        return self.player + 1
