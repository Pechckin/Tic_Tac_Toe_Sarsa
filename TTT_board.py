class Board(object):
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([0, 0, 0])

    def move(self, who, where):
        assert (who == 1 or who == 2)
        assert (self.board[where[0]][where[1]] == 0)
        self.board[where[0]][where[1]] = who

    def delete(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0

    def get_possible_actions(self):
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    res.append((i, j))

        return res

    def get_color(self, pos):
        return self.board[pos[0]][pos[1]]

    def get_winner(self):

        for i in range(3):
            who = self.board[i][0]
            if who == 0:
                continue

            for j in range(1, 3):
                if self.board[i][j] != who:
                    break
            else:
                return who

        for j in range(3):
            who = self.board[0][j]
            if who == 0:
                continue

            for i in range(1, 3):
                if self.board[i][j] != who:
                    break
            else:
                return who

        who = self.board[0][0]
        if who != 0:
            for i in range(1, 3):
                if self.board[i][i] != who:
                    break
            else:
                return who

        who = self.board[2][0]
        if who != 0:
            for i in range(2):
                if self.board[i][2 - i] != who:
                    break
            else:
                return who

        return 0

    def can_be_played(self):
        if len(self.get_possible_actions()) == 0:
            return False
        if self.get_winner():
            return False
        return True

    def __str__(self):
        return str(self.board[0]) + '\n' + \
               str(self.board[1]) + '\n' + \
               str(self.board[2]) + '\n'
