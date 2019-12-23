from Board import Board

class Controller:
    """TODO"""
    def __init__(self):
        self.board = Board(4)

    def play(self, player):
        """TODO"""
        play = True
        while play:
            text = "It's player {}'s turn: ".format(player+1)
            move = input(text)
            try:
                action = tuple(int(x) for x in move.split(","))
                row = action[0]
                col = action[1]
                try:
                    self.board.place(row=row, col=col, player=player)
                    print("Player ", player + 1, " chose row: ", row, " col: ", col)
                    play = False
                except:
                    print("Illegal move, try again")
                    legal = self.board.getLegal(player=player)
                    print("Legal moves: ", legal)
            except:
                print("A move must be two ints separated by a comma: int, int")


    def gameloop(self):
        """TODO"""
        while not self.board.gameover:
            # print("...")
            if bool(self.board.getLegal(0)):
                print(self.board)
                legal = self.board.getLegal(player=0)
                print("Legal moves for white: ", legal)
                self.play(player=0)

            if bool(self.board.getLegal(1)):
                print(self.board)
                legal = self.board.getLegal(player=1)
                print("Legal moves for black: ", legal)
                self.play(player=1)
        print("Game over")
        self.getWinner()

    def getWinner(self):
        whiteCount = 0
        blackCount = 0
        for row in range(self.board.dimensions):
            for col in range(self.board.dimensions):
                if self.board.layout[row][col].color == 0:
                    whiteCount += 1
                elif self.board.layout[row][col].color == 1:
                    blackCount += 1

        if whiteCount > blackCount:
            print("White player wins with {} points!".format(whiteCount))
            print(self.board)
            return 0
        elif blackCount > whiteCount:
            print("Black player wins with {} points!".format(blackCount))
            print(self.board)
            return 1
        else:
            print("It's a draw!")
            print(self.board)
            return None


def main():
    game = Controller()
    game.gameloop()

main()
