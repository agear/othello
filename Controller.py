from Board import Board
from View import View
from typing import List
import turtle, random, time


class Controller:
    """TODO"""
    def __init__(self, dimensions: int=8):
        self.board = Board(dimensions)
        self.view = View(dimensions)


    # def gameloop(self) -> None:
    #     """TODO"""
    #     self.draw_board()
    #     while not self.board.gameover:
    #         if bool(self.board.get_legal(0)):
    #             print(self.board)
    #             legal = self.board.get_legal(player=0)
    #             print("Legal moves for white: ", legal)
    #             self.play(player=0)
    #
    #         if bool(self.board.get_legal(1)):
    #             print(self.board)
    #             legal = self.board.get_legal(player=1)
    #             print("Legal moves for black: ", legal)
    #             self.play(player=1)
    #     print("Game over")
    #     self.getWinner()

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

    def update_view(self, updated: List[tuple], player: int) -> None:
        """TODO"""
        self.view.erase_previous_legal()

        for coordinate in updated:
            row = coordinate[0]
            col = coordinate[1]
            self.view.draw_tile(row=row, col=col, color=self.board.layout[row][col].color)

        if player is 1:
            self.view.draw_all_legal(self.board.get_legal(player=0))


    def translate(self, x: float) -> int:
        """TODO"""
        left_boarder = -(self.view.dimensions/2 * self.view.square)
        value = -1
        for section in range(int(left_boarder), int(x), int(self.view.square)):
            value += 1
        # print(value)
        return value

    def play(self, row: int, col: int, player: int):
        updated = self.board.place(row=row, col=col, player=player)
        self.view.draw_tile(row=row, col=col, color=player)
        self.update_view(updated=updated, player=player)

    def clickPlay(self, x: int, y: int) -> None:
        """TODO"""

        # Prevent input until after AI plays
        self.view.screen.onscreenclick(None)

        # Player 0 plays x, y if legal
        row = self.translate(-y)
        col = self.translate(x)
        if not self.board.is_gameover():
            try:

                self.play(row=row, col=col, player=0)
                # updated = self.board.place(row=row, col=col, player=0)
                #
                # self.view.draw_tile(row=row, col=col, color=0)
                # self.update_view(updated)
                if self.board.is_gameover():
                    print("Game over")
                    self.getWinner()
                    time.sleep(5)
                    turtle.bye()

                # Computer plays
                # TODO loop if no legal white moves???
                time.sleep(1)
                legalAImoves = self.board.get_legal(player=1)
                random_move = random.choice(tuple(legalAImoves))
                # updated = self.board.place(row=random_move[0], col=random_move[1], player=1)
                # self.view.draw_tile(row=random_move[0], col=random_move[1], color=1)
                # self.update_view(updated)
                self.play(row=random_move[0], col=random_move[1], player=1)
                print("White points: {}\nBlack points: {}".format(self.board.white_points, self.board.black_points))
                if not bool(self.board.get_legal(player=0)):
                    while not bool(self.board.get_legal(player=0)):
                        print("No Legal moves for white!")
                        time.sleep(1)
                        legalAImoves = self.board.get_legal(player=1)
                        random_move = random.choice(tuple(legalAImoves))
                        updated = self.board.place(row=random_move[0], col=random_move[1], player=1)
                        self.view.draw_tile(row=random_move[0], col=random_move[1], color=1)
                        self.update_view(updated)
                        print("White points: {}\nBlack points: {}".format(self.board.white_points,
                                                                          self.board.black_points))
                        if self.board.gameover:
                            print("Game over")
                            self.getWinner()
                            time.sleep(5)
                            turtle.bye()
                # Return control to player
                self.view.screen.onscreenclick(self.clickPlay)
                if self.board.gameover:
                    print("Game over")
                    self.getWinner()
                    time.sleep(5)
                    turtle.bye()

                # Draw players legal moves
                # legal_player_moves = self.board.get_legal(player=0)
                # print("LEGAL: ", legal_player_moves)
                # self.view.draw_all_legal(legal=legal_player_moves)

            except:
                print("Illegal move, try again")
                legal = self.board.get_legal(player=0)
                print("Legal moves: ", legal)

                # Return control to player
                self.view.screen.onscreenclick(self.clickPlay)



def main():
    game = Controller()
    game.view.screen.onscreenclick(game.clickPlay)

    game.draw_board()
    turtle.done()

main()
