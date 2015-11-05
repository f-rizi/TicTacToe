class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.board = [['.'] * self.size for i in range(self.size)]

        self.player = 0


    def click(self, row, column):
        if not self.have_empty_cell():
            return "game is finished, start a new one"

        winner = self.get_winner()

        if winner != 0:
            return "player %d won the game, start a new one" \
                   % self.get_player()

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
        results = self.get_results()

        if ["X"] * self.size in results:
            return 1
        elif ["O"] * self.size in results:
            return 2

        return 0

    def get_results(self):
        result = []

        result.append([self.board[i][i] for i in range(self.size)])

        result.append([self.board[self.size - i - 1][i] for i in range(self.size)])

        for i in range(self.size):
            result.append([self.board[i][j] for j in range(self.size)])

            result.append([self.board[j][i] for j in range(self.size)])
        return result

    def get_player(self):
        return self.player + 1
