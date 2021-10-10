from Matrix import Matrix
from MatrixPlayer import MatrixPlayer
import numpy
from pynput import keyboard

class MatrixGame(Matrix):
    neutral_x = range(120, 130);
    neutral_y = range(120, 130);
    down_x = range(245, 255)
    down_y = range(120, 130)
    up_x = range(0, 10)
    up_y = range(120, 130)
    left_x = range(120, 130)
    left_y = range(245, 255)
    right_x = range(120, 130)
    right_y = range(0, 10)
    player1 = MatrixPlayer()
    player2 = MatrixPlayer()

    p1_title = [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,1,0],
        [0,1,0,1,0,1,1,0],
        [0,1,0,1,0,0,1,0],
        [0,1,1,1,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0],
    ]

    p1_winner = [
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [1,0,0,1,1,0,0,1],
        [1,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0],
    ]

    p2_title = [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,0,1,1,0],
        [0,1,0,1,0,0,1,0],
        [0,1,0,1,0,1,1,0],
        [0,1,1,1,0,1,0,0],
        [0,1,0,0,0,1,0,0],
        [0,1,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0],
    ]

    p2_winner = [
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0],
        [1,0,0,0,1,0,0,1],
        [1,0,0,1,0,0,0,1],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0],
    ]

    columns = [
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
    ]

    resetMatrix = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    startMatrix = [
        [1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    def setup(self):
        Matrix.setup(self)
        listener = keyboard.Listener(on_press = self.on_press, on_release = self.on_release)
        listener.start()

    def moveDown(self, player):
        player.board[player.position[0]][player.position[1]] = 0
        if (player.position[1] == 7):
            player.position[1] = -1
        player.position[1] = player.position[1] + 1
        player.board[player.position[0]][player.position[1]] = 1
        player.moves.append([player.position[0], player.position[1]])
        self.buzz()

    def moveUp(self, player):
        player.board[player.position[0]][player.position[1]] = 0
        if (player.position[1] == 0):
            player.position[1] = 7
        player.position[1] = player.position[1] - 1
        player.board[player.position[0]][player.position[1]] = 1
        player.moves.append([player.position[0], player.position[1]])
        self.buzz()

    def moveLeft(self, player):
        player.board[player.position[0]][player.position[1]] = 0
        if (player.position[0] == 0):
            player.position[0] = 7
        player.position[0] = player.position[0] - 1
        player.board[player.position[0]][player.position[1]] = 1
        player.moves.append([player.position[0], player.position[1]])
        self.buzz()

    def moveRight(self, player):
        player.board[player.position[0]][player.position[1]] = 0
        if (player.position[0] == 7):
            player.position[0] = -1
        player.position[0] = player.position[0] + 1
        player.board[player.position[0]][player.position[1]] = 1
        player.moves.append([player.position[0], player.position[1]])
        self.buzz()

    def on_joy(self, x, y):
        if x in self.neutral_x and y in self.neutral_y:
            pass
        if x in self.down_x and y in self.down_y:
            self.moveDown(self.player1)
        if x in self.up_x and y in self.up_y:
            self.moveUp(self.player1)
        if x in self.left_x and y in self.left_y:
            self.moveLeft(self.player1)
        if x in self.right_x and y in self.right_y:
            self.moveRight(self.player1)

    def on_press(self, key):
        if key == keyboard.Key.down:
            self.moveDown(self.player2)
        if key == keyboard.Key.up:
            self.moveUp(self.player2)
        if key == keyboard.Key.left:
            self.moveLeft(self.player2)
        if key == keyboard.Key.right:
            self.moveRight(self.player2)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def compareMoves(self, p1, p2):
        for move, position in enumerate(p2):
            try:
                if not position == p1[move]:
                    return False 
            except IndexError:
                return False
        return True

    def loop(self):
        while(True):
            self.player1.resetAll()
            self.player2.resetAll()

            for i in range(1, 500):
                self.displayMatrix(numpy.transpose(self.p1_title))

            while(len(self.player1.moves) < 5):
                val_Y = self.adc.analogRead(0)
                val_X = self.adc.analogRead(1)
                self.on_joy(val_X, val_Y)
                self.displayMatrix(self.player1.board)
            
            self.player1.resetBoard()

            for i in range(1, 500):
                self.displayMatrix(numpy.transpose(self.p2_title))

            while(len(self.player2.moves) < 5):
                self.displayMatrix(self.player2.board)
                if not self.compareMoves(self.player1.moves, self.player2.moves):
                    break
            
            if self.compareMoves(self.player1.moves, self.player2.moves):
                for i in range(1, 50):
                    self.displayMatrix(numpy.transpose(self.p2_winner))
                    self.buzz_won()
            else:
                for i in range(1, 50):
                    self.displayMatrix(numpy.transpose(self.p1_winner))
                    self.buzz_won()

            self.player1.resetAll()
            self.player2.resetAll()
