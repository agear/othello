from Board import Board
from View import View
import turtle
import random

class Controller:
    """TODO"""
    def __init__(self):
        self.board = Board()
        self.view = View()
        self.x = None
        self.y = None
        # self.view.draw_board()

    def gameloop(self):
        """TODO"""
        print("Inside Game loop...")
        self.draw_board()
        print("Finished drawing the board...")
        # self.view.screen.onscreenclick(clicked)
        while not self.board.gameover:
            if bool(self.board.get_legal(0)):
                print(self.board)
                legal = self.board.get_legal(player=0)
                print("Legal moves for white: ", legal)
                self.play(player=0)

            if bool(self.board.get_legal(1)):
                print(self.board)
                legal = self.board.get_legal(player=1)
                print("Legal moves for black: ", legal)
                self.play(player=1)
        print("Game over")
        self.getWinner()

    def play(self, player: int) -> None:
        """TODO"""

        play = True
        # self.update_view()
        while play:
            text = "It's player {}'s turn: ".format(player+1)
            # self.view.screen.onscreenclick(clicked)
            move = input(text)
            try:
                action = tuple(int(x) for x in move.split(","))
                row = action[0]
                col = action[1]
                try:
                    updated = self.board.place(row=row, col=col, player=player)
                    print("Player ", player + 1, " chose row: ", row, " col: ", col)
                    self.view.draw_tile(row=row, col=col, color=player)
                    self.update_view(updated)
                    print("White points: {}\nBlack points: {}".format(self.board.white_points, self.board.black_points))
                    play = False
                except:
                    print("Illegal move, try again")
                    legal = self.board.get_legal(player=player)
                    print("Legal moves: ", legal)
            except:
                print("A move must be two ints separated by a comma: int, int")



    def getWinner(self):
        """TODO"""
        if self.board.white_points > self.board.black_points:
            print("White player wins with {} points!".format(self.board.white_points))
            print(self.board)
            return 0
        elif self.board.black_points > self.board.white_points:
            print("Black player wins with {} points!".format(self.board.black_points))
            print(self.board)
            return 1
        else:
            print("It's a draw!")
            print(self.board)
            return None

    def draw_board(self):
        print("Drawing board....")
        self.view.draw_board()
        print("Finished drawing board...")

    def update_view(self, updated):
        print("Updating view...")
        for coordinate in updated:
            row = coordinate[0]
            col = coordinate[1]
            self.view.draw_tile(row=row, col=col, color=self.board.layout[row][col].color)
        # for row in range(self.board.dimensions):
        #     for col in range(self.board.dimensions):
        #         if self.board.layout[row][col].occupied:
        #             self.view.draw_tile(row=row, col=col, color=self.board.layout[row][col].color)

    # def getPos(self):
    #     turtle.onscreenclick(clicked)

    def translate(self, x):
        if -200 < x and x < -150:
            return 0
        elif -150 < x and x < -100:
            return 1
        elif -100 < x and x < -50:
            return 2
        elif -50 < x and x < 0:
            return 3
        elif 0 < x and x < 50:
            return 4
        elif 50 < x and x < 100:
            return 5
        elif 100 < x and x < 150:
            return 6
        elif 150 < x and x < 200:
            return 7
        else:
            return None

    def clicked(self, x, y):
        self.x = self.translate(x)
        self.y = self.translate(-y)
        print("self.x ", self.x, "self.y: ", self.y)

    def clickPlay(self, x, y):
        # Player 0 plays x, y if legal
        row = self.translate(-y)
        col = self.translate(x)
        print("Row: ", row, "Col: ", col)
        try:
            updated = self.board.place(row=row, col=col, player=0)
            print("Player chose row: ", row, " col: ", col)
            self.view.draw_tile(row=row, col=col, color=0)
            self.update_view(updated)
            legalAImoves = self.board.get_legal(player=1)
            print("LegalAImoves: ", legalAImoves)
            random_move = random.choice(tuple(legalAImoves))
            print("Random move: ", random_move)
            updated = self.board.place(row=random_move[0], col=random_move[1], player=1)
            self.view.draw_tile(row=random_move[0], col=random_move[1], color=1)
            self.update_view(updated)
            print("White points: {}\nBlack points: {}".format(self.board.white_points, self.board.black_points))
            # play = False
        except:
            print("Illegal move, try again")
            legal = self.board.get_legal(player=0)
            print("Legal moves: ", legal)

        # Computer plays

def main():
    # screen = turtle.Screen()
    game = Controller()
    game.view.screen.onscreenclick(game.clickPlay)
    # screen.onscreenclick(clicked)
    print("Made a controller...")

    game.draw_board()
    # game.gameloop()
    turtle.listen()
    turtle.done()

main()
# turtle.done()
