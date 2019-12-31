from Board import Board
from View import View
from typing import List
import turtle, random, time


class Controller:
    """TODO"""
    def __init__(self, dimensions: int=8):
        self.board = Board(dimensions)
        self.view = View(dimensions)


    def gameloop(self) -> None:
        """TODO"""
        self.draw_board()
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
        while play:
            text = "It's player {}'s turn: ".format(player+1)
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
            return 0
        elif self.board.black_points > self.board.white_points:
            print("Black player wins with {} points!".format(self.board.black_points))
            return 1
        else:
            print("It's a draw!")
            return None

    def draw_board(self):
        """TODO"""
        self.view.draw_board()

    def update_view(self, updated: List[tuple]) -> None:
        """TODO"""
        for coordinate in updated:
            row = coordinate[0]
            col = coordinate[1]
            self.view.draw_tile(row=row, col=col, color=self.board.layout[row][col].color)


    def translate(self, x: float) -> int:
        """TODO"""
        left_boarder = -(self.view.dimensions/2 * self.view.square)
        value = -1
        for section in range(int(left_boarder), int(x), int(self.view.square)):
            value += 1
        print(value)
        return value


    def clickPlay(self, x: int, y: int) -> None:
        """TODO"""
        # Player 0 plays x, y if legal
        row = self.translate(-y)
        col = self.translate(x)
        if not self.board.gameover:
            try:
                updated = self.board.place(row=row, col=col, player=0)
                self.view.draw_tile(row=row, col=col, color=0)
                self.update_view(updated)
                self.view.screen.onscreenclick(None)
                # Computer plays
                time.sleep(3)
                legalAImoves = self.board.get_legal(player=1)
                random_move = random.choice(tuple(legalAImoves))
                updated = self.board.place(row=random_move[0], col=random_move[1], player=1)
                self.view.draw_tile(row=random_move[0], col=random_move[1], color=1)
                self.update_view(updated)
                print("White points: {}\nBlack points: {}".format(self.board.white_points, self.board.black_points))
                self.view.screen.onscreenclick(self.clickPlay)
                if self.board.gameover:
                    print("Game over")
                    self.getWinner()
                    time.sleep(5)
                    turtle.bye()
            except:
                print("Illegal move, try again")
                legal = self.board.get_legal(player=0)
                print("Legal moves: ", legal)



def main():
    game = Controller()
    game.view.screen.onscreenclick(game.clickPlay)

    game.draw_board()
    turtle.done()

main()
