import turtle

class View:

    def __init__(self, dimensions=8, square=50):
        self.dimensions = dimensions
        self.square = square
        self.circle = (square // 2)
        self.size = dimensions
        self.othello = turtle.Turtle()


    def draw_board(self):
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

def main():
    view = View()
    view.draw_board()

main()
# Keeps the turtle window open
turtle.done()

