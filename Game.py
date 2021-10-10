from MatrixGame import MatrixGame

if __name__ == '__main__':
    print ('MatrixGame is starting...' )
    game = MatrixGame()
    game.setup()
    try:
        game.loop()
    except KeyboardInterrupt:
        print ('Cleaning up...' )
        game.destroy()
