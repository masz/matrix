class MatrixPlayer():
    board = [
        [1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    position = [0,0]
    moves = []

    def resetAll(self):
        for x in range(0,8):
            for y in range(0,8):
                self.board[x][y] = 0
                self.board[x][y] = 0

        self.board[0][0] = 1
        self.position = [0,0];
        self.moves = [];

    def resetBoard(self):
        for x in range(0,8):
            for y in range(0,8):
                self.board[x][y] = 0
                self.board[x][y] = 0

        self.board[0][0] = 1
        self.position = [0,0];
