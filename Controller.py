from Board import Board

class Controller:
    """TODO"""
    def __init__(self):
        self.board = Board()

    def play(self, player):
        """TODO"""
        play = True
        while play:
            text = "It's player {}'s turn: ".format(player+1)
            move = input(text)
            action = tuple(int(x) for x in move.split(","))
            row = action[0]
            col = action[1]
            try:
                self.board.place(row=row, col=col, player=player)
                print("Player ", player+1, " chose row: ", row, " col: ", col)
                play = False
            except:
                print("Illegal move, try again")

    def gameloop(self):
        """TODO"""
        while not self.board.gameover:
            print(self.board)
            self.board.getLegal(player=0)
            self.play(player=0)
            print(self.board)
            self.play(player=1)


def main():
    game = Controller()
    game.gameloop()

main()
