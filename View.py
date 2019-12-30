import turtle

class View:

    def __init__(self, dimensions=8, square=50):
        self.dimensions = dimensions
        self.square = square
        self.circle = (square // 2)
        self.size = dimensions
        self.screen = turtle.Screen()
        self.othello = turtle.Turtle()

    def click(self, x, y):
        print(x, y)


    def draw_board(self):
        ''' Function: draw_board
            Parameters: n, an int for # of squares
            Returns: nothing
            Does: Draws an nxn board with a green background
        '''

        turtle.setup(self.size * self.square + self.square, self.size * self.square + self.square)
        turtle.screensize(self.size * self.square, self.size * self.square)
        turtle.bgcolor('white')
        # turtle.onscreenclick(self.click)

        print("Creating turtle...")
        # Create the turtle to draw the board
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()
        # Line color is black, fill color is green
        self.othello.color("black", "forest green")

        # Move the turtle to the upper left corner
        corner = -self.dimensions * self.square / 2
        self.othello.setposition(corner, corner)

        print("Drawing green background...")
        # Draw the green background
        self.othello.begin_fill()
        for i in range(4):
            self.othello.pendown()
            self.othello.forward(self.square * self.dimensions)
            self.othello.left(90)
        self.othello.end_fill()

        print("Drawing horizontal lines...")
        # Draw the horizontal lines
        for i in range(self.dimensions + 1):
            self.othello.setposition(corner, self.square * i + corner)
            self.othello.pendown()
            self.othello.forward(self.square * self.dimensions)
            self.othello.penup()

        print("Drawing verticle lines...")
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
        print("Returning...")
        # turtle.done()
        return

    def draw_tile(self, row, col, color):
        if color == 0: color = "white"
        elif color == 1: color = "black"

        row = -(row - 3)
        col = col - 3
        y = row * self.square + (self.square/2)
        x = col * self.square
        # print("col:", col, "x: ", x)
        # print("row: ", row ,"y: ", y)

        self.othello.penup()
        self.othello.goto(x, y)
        self.othello.pendown()
        self.othello.color("black", color)
        self.othello.begin_fill()
        self.othello.circle(self.circle)
        self.othello.end_fill()

# def main():
    # view = View()
    # view.draw_board()
    # view.draw_tile(row=0, col=0, color=0)
    # view.draw_tile(row=0, col=1, color=1)
    # view.draw_tile(row=0, col=2, color=0)
    # view.draw_tile(row=0, col=3, color=1)
    # view.draw_tile(row=0, col=4, color=0)
    # view.draw_tile(row=0, col=5, color=1)
    # view.draw_tile(row=0, col=6, color=0)
    # view.draw_tile(row=0, col=7, color=1)
    #
    # view.draw_tile(row=1, col=0, color=1)
    # view.draw_tile(row=1, col=1, color=0)
    # view.draw_tile(row=1, col=2, color=1)
    # view.draw_tile(row=1, col=3, color=0)
    # view.draw_tile(row=1, col=4, color=1)
    # view.draw_tile(row=1, col=5, color=0)
    # view.draw_tile(row=1, col=6, color=1)
    # view.draw_tile(row=1, col=7, color=0)
    #
    # view.draw_tile(row=2, col=0, color=0)
    # view.draw_tile(row=2, col=1, color=1)
    # view.draw_tile(row=2, col=2, color=0)
    # view.draw_tile(row=2, col=3, color=1)
    # view.draw_tile(row=2, col=4, color=0)
    # view.draw_tile(row=2, col=5, color=1)
    # view.draw_tile(row=2, col=6, color=0)
    # view.draw_tile(row=2, col=7, color=1)
    #
    # view.draw_tile(row=3, col=0, color=1)
    # view.draw_tile(row=3, col=1, color=0)
    # view.draw_tile(row=3, col=2, color=1)
    # view.draw_tile(row=3, col=3, color=0)
    # view.draw_tile(row=3, col=4, color=1)
    # view.draw_tile(row=3, col=5, color=0)
    # view.draw_tile(row=3, col=6, color=1)
    # view.draw_tile(row=3, col=7, color=0)
    #
    # view.draw_tile(row=4, col=0, color=0)
    # view.draw_tile(row=4, col=1, color=1)
    # view.draw_tile(row=4, col=2, color=0)
    # view.draw_tile(row=4, col=3, color=1)
    # view.draw_tile(row=4, col=4, color=0)
    # view.draw_tile(row=4, col=5, color=1)
    # view.draw_tile(row=4, col=6, color=0)
    # view.draw_tile(row=4, col=7, color=1)
    #
    # view.draw_tile(row=5, col=0, color=1)
    # view.draw_tile(row=5, col=1, color=0)
    # view.draw_tile(row=5, col=2, color=1)
    # view.draw_tile(row=5, col=3, color=0)
    # view.draw_tile(row=5, col=4, color=1)
    # view.draw_tile(row=5, col=5, color=0)
    # view.draw_tile(row=5, col=6, color=1)
    # view.draw_tile(row=5, col=7, color=0)
    #
    # view.draw_tile(row=6, col=0, color=0)
    # view.draw_tile(row=6, col=1, color=1)
    # view.draw_tile(row=6, col=2, color=0)
    # view.draw_tile(row=6, col=3, color=1)
    # view.draw_tile(row=6, col=4, color=0)
    # view.draw_tile(row=6, col=5, color=1)
    # view.draw_tile(row=6, col=6, color=0)
    # view.draw_tile(row=6, col=7, color=1)
    #
    # view.draw_tile(row=7, col=0, color=1)
    # view.draw_tile(row=7, col=1, color=0)
    # view.draw_tile(row=7, col=2, color=1)
    # view.draw_tile(row=7, col=3, color=0)
    # view.draw_tile(row=7, col=4, color=1)
    # view.draw_tile(row=7, col=5, color=0)
    # view.draw_tile(row=7, col=6, color=1)
    # view.draw_tile(row=7, col=7, color=0)

# main()
# Keeps the turtle window open
# turtle.done()

