import turtle
from typing import Set

class View:

    def __init__(self, dimensions: int=8, square: int=50):
        self.dimensions = dimensions
        self.square = square
        self.circle = (square // 2)
        self.size = dimensions
        self.screen = turtle.Screen()
        self.othello = turtle.Turtle()
        self.legal = turtle.Turtle()
        self.last_legal_moves = []

        self.legal.penup()
        self.legal.speed(0)
        self.legal.hideturtle()

        corner = -self.dimensions * self.square / 2
        self.legal.setposition(corner, corner)

    def draw_board(self) -> None:
        ''' Function: draw_board
            Parameters: n, an int for # of squares
            Returns: nothing
            Does: Draws an nxn board with a green background
        '''

        turtle.setup(self.size * self.square + self.square, self.size * self.square + self.square)
        turtle.screensize(self.size * self.square, self.size * self.square)
        turtle.bgcolor('white')

        # Create the turtle to draw the board
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()
        # Line color is black, fill color is green
        self.othello.color("black", "forest green")

        # Move the turtle to the upper left corner
        corner = -self.dimensions * self.square / 2
        self.othello.setposition(corner, corner)

        # Draw the green background
        self.othello.begin_fill()
        for i in range(4):
            self.othello.pendown()
            self.othello.forward(self.square * self.dimensions)
            self.othello.left(90)
        self.othello.end_fill()

        # Draw the horizontal lines
        for i in range(self.dimensions + 1):
            self.othello.setposition(corner, self.square * i + corner)
            self.othello.pendown()
            self.othello.forward(self.square * self.dimensions)
            self.othello.penup()

        # Draw the vertical lines
        self.othello.left(90)
        for i in range(self.dimensions + 1):
            self.othello.setposition(self.square * i + corner, corner)
            self.othello.pendown()
            self.othello.forward(self.square * self.dimensions)
            self.othello.penup()

        # Draw start tiles
        self.draw_tile(row=3, col=3, color=0)
        self.draw_tile(row=3, col=4, color=1)
        self.draw_tile(row=4, col=3, color=1)
        self.draw_tile(row=4, col=4, color=0)

    def draw_tile(self, row: int, col: int, color: int) -> None:
        """TODO"""
        if color == 0: color = "white"
        elif color == 1: color = "black"

        row = -(row - 3)
        col = col - 3
        y = row * self.square + (self.square/2)
        x = col * self.square


        self.othello.penup()
        self.othello.goto(x, y)
        self.othello.pendown()
        self.othello.color("black", color)
        self.othello.begin_fill()
        self.othello.circle(self.circle)
        self.othello.end_fill()

    def draw_all_legal(self, legal: Set[tuple]) -> None:
        # Draw new legal moves
        for move in legal:
            self.draw_legal(row=move[0], col=move[1])

        # Reset previous legal moves
        self.last_legal_moves = legal

    def draw_legal(self, row: int, col: int) -> None:
        """TODO"""
        # if color == 0: color = "white"
        # elif color == 1: color = "black"

        row = -(row - 3)
        col = col - 3
        y = row * self.square
        x = col * self.square - (self.square/2)


        self.legal.penup()
        self.legal.goto(x, y)
        self.legal.pendown()
        self.legal.color("brown", "forest green")
        self.legal.begin_fill()
        self.legal.circle(self.circle)
        self.legal.end_fill()

    def erase_previous_legal(self) -> None:
        self.legal.clear()



    # def erase_legal(self, row: int, col: int) -> None:
    #     row = -(row - 3)
    #     col = col - 3
    #     y = row * self.square + (self.square/2)
    #     x = col * self.square
    #
    #
    #     self.othello.penup()
    #     self.othello.goto(x, y)
    #     self.othello.pendown()
    #     self.othello.color("forest green", "forest green")
    #     self.othello.begin_fill()
    #     self.othello.circle(self.circle-5)
    #     self.othello.end_fill()
