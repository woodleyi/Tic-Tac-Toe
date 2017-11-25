"""
Tic-Tac-Toe
Ian S. Woodley

A quick console application of 2-player Tic Tac Toe.
"""

class Game:
    def __init__(self):
        self.board = [ [(r * 3) + c for c in range(3)] for r in range(3) ]

    def displayBoard(self):
        for row in self.board:
            for col in row:
                print("{} ".format(col), end='')
            print('\n')

    def checkForWin(self, p):
        def checkRows():
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] != p:
                        break
                else:
                    return True
            return False

        def checkColumns():
            for c in range(3):
                for r in range(3):
                    if self.board[r][c] != p:
                        break
                else:
                    return True
            return False

        def checkDiagonals():
            for d in range(3):
                if self.board[d][d] != p:
                    for d in range(3):
                        if self.board[d][2-d] != p:
                            return False
            return True

        def checkForTie():
            for row in self.board:
                for col in row:
                    if type(col) == int:
                        return False
            return True

        # Check all win conditions
        for func in ( checkRows, checkColumns, checkDiagonals ):
            if func():
                return 1    # Winner
        if checkForTie():
            return -1       # Tie game
        return 0            # Game continues

    def resetBoard(self):
        self.board = [ [(r * 3) + c for c in range(3)] for r in range(3) ]

    def play(self):
        player = 'X'
        done = False

        while not done:
            while 1:
                print("\nPlayer %s's turn\n" % player)
                self.displayBoard()
                try:
                    idx = int(input("\nSelect an open position. "))
                    assert 0 <= idx < 9
                    
                    row = idx // 3
                    col = idx % 3

                    if type(self.board[row][col]) == int:
                        self.board[row][col] = player
                    else:
                        raise ValueError("Invalid position.")

                    state = self.checkForWin(player)
                    if state == 1:
                        self.displayBoard()
                        print("PLAYER %s WINS!!!" % player)
                        break
                    elif state == 0:
                        player = 'X' if player == 'O' else 'O'
                    else:
                        self.displayBoard()
                        print("TIE GAME!")
                        break
                except:
                    print("Invalid input, try again.")
            while 1:
                ipt = input("Play again? (Y/N)")
                if ipt.lower() == 'y':
                    self.resetBoard()
                    break
                elif ipt.lower() == 'n':
                    done = True
                    break
                else:
                    print("Invalid input: %s" % ipt)

if __name__ == "__main__":
    game = Game()
    game.play()
