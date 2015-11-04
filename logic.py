class TicTacToe:
    def __init__(self):
        self.board = [[".", ".", "."],
                      [".", ".", "."],
                      [".", ".", "."]]

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
        for i in range(3):
            if "." in self.board[i]:
                return True

    def get_winner(self):
        results = self.get_results()

        if ["X", "X", "X"] in results:
            return 1
        elif ["O", "O", "O"] in results:
            return 2

        return 0

    def get_results(self):
        result = []

        result.append([self.board[0][0],
                       self.board[1][1],
                       self.board[2][2]])

        result.append([self.board[0][2],
                       self.board[1][1],
                       self.board[2][0]])

        for i in range(3):
            result.append([self.board[i][0],
                           self.board[i][1],
                           self.board[i][2]])

            result.append([self.board[0][i],
                           self.board[1][i],
                           self.board[2][i]])
        return result

    def get_player(self):
        return self.player + 1

    def print_board(self):
        for i in range(3):
            print(self.board[i])

    def print_result(self, result):
        print "result is: "
        for i in range(8):
            print(result[i])
