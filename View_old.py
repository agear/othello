'''
    Alex Gear
    CS5001
    Homework 7
    December 2nd, 2018
'''

import turtle
# from tile import Tile
# from tile import Disk

SQUARE = 50
CIRCLE = (SQUARE // 2)
n = 8

class Board:
    def __init__(self):
        self.size = n
        self.grid = []
        self.r_bound = self.size * (SQUARE // 2)
        self.l_bound = self.size * -(SQUARE // 2)
        self.hor_center = self.l_bound + (SQUARE // 2)
        self.t_bound = self.size * (SQUARE // 2)
        self.b_bound = self.size * -(SQUARE // 2)
        self.ver_cent = self.t_bound - SQUARE
        for i in range(self.size):
            self.grid.append([])
            for j in range(self.size):
                tile = Disk(i, j, '')
                tile.x = i
                tile.y = j
                self.grid[i].append(tile)
        self.othello = turtle.Turtle()

    def __len__(self):
        return len(self.grid)

    def __str__(self):
        return self.grid

    def draw_board(self):
        ''' Function: draw_board
            Parameters: n, an int for # of squares
            Returns: nothing
            Does: Draws an nxn board with a green background
        '''

        turtle.setup(self.size * SQUARE + SQUARE, self.size * SQUARE + SQUARE)
        turtle.screensize(self.size * SQUARE, self.size * SQUARE)
        turtle.bgcolor('white')

        # Create the turtle to draw the board
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()
        # Line color is black, fill color is green
        self.othello.color("black", "forest green")

        # Move the turtle to the upper left corner
        corner = -n * SQUARE / 2
        self.othello.setposition(corner, corner)

        # Draw the green background
        self.othello.begin_fill()
        for i in range(4):
            self.othello.pendown()
            self.othello.forward(SQUARE * n)
            self.othello.left(90)
        self.othello.end_fill()

        # Draw the horizontal lines
        for i in range(n + 1):
            self.othello.setposition(corner, SQUARE * i + corner)
            self.othello.pendown()
            self.othello.forward(SQUARE * n)
            self.othello.penup()

        # Draw the vertical lines
        self.othello.left(90)
        for i in range(n + 1):
            self.othello.setposition(SQUARE * i + corner, corner)
            self.othello.pendown()
            self.othello.forward(SQUARE * n)
            self.othello.penup()

    def draw_tile(self, x, y, color):
        self.othello.penup()
        self.othello.goto(x, y)
        self.othello.pendown()
        self.othello.color("black", color)
        self.othello.begin_fill()
        self.othello.circle(CIRCLE)
        self.othello.end_fill()

    def in_boundary(self, x, y):
        '''
            Name: in_boundary
            input: x (an int), y (an int)
            returns: True if within the boundary, False otherwise
        '''
        if x < self.l_bound or x > self.r_bound:
            print("Out of bounds!")
            return False
        elif y < self.b_bound or y > self.t_bound:
            print("Out of bounds!")
            return False
        else:
            return True

    def update_b_legal(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                self.check_adjacent_black(i, j)
                print("Grid", i, j, "b_legal is:", self.grid[i][j].b_legal)

    def check_adjacent_black(self, col, row):
        if col - 1 >= 0  and row - 1 >= 0:
            if self.grid[col - 1][row - 1].color == "black":
                self.grid[col][row].b_legal = True
                return
        if col - 1 >= 0:
            if self.grid[col -1][row].color == "black":
                self.grid[col][row].b_legal = True
            return
        if col - 1 >= 0 and row + 1 <= 7:
            if self.grid[col - 1][row + 1].color == "black":
                self.grid[col][row].b_legal = True
                return
        if row - 1 >= 0:
            if self.grid[col][row - 1].color == "black":
                self.grid[col][row].b_legal = True
                return
        if row + 1 <= 7:
            if self.grid[col][row + 1].color == "black":
                self.grid[col][row].b_legal = True
                return
        if col + 1 <= 7 and row - 1 >= 0:
            if self.grid[col + 1][row - 1].color == "black":
                self.grid[col][row].b_legal = True
                return
        if col + 1 <= 7:
            if self.grid[col + 1][row].color == "black":
                self.grid[col][row].b_legal = True
                return
        if col + 1 <= 7 and row + 1 <= 7:
            if self.grid[col + 1][row + 1].color == "black":
                self.grid[col][row].b_legal = True
                return
        else:
            print("no adjacency")
            return False

    def update_w_legal(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                self.check_adjacent_white(i, j)
                print("Grid", i, j, "w_legal is:", self.grid[i][j].w_legal)

    def check_adjacent_white(self, col, row):
        if col - 1 >= 0  and row - 1 >= 0:
            if self.grid[col - 1][row - 1].color == "white":
                self.grid[col][row].w_legal = True
                return
        if col - 1 >= 0:
            if self.grid[col -1][row].color == "white":
                self.grid[col][row].w_legal = True
            return
        if col - 1 >= 0 and row + 1 <= 7:
            if self.grid[col - 1][row + 1].color == "white":
                self.grid[col][row].w_legal = True
                return
        if row - 1 >= 0:
            if self.grid[col][row - 1].color == "white":
                self.grid[col][row].w_legal = True
                return
        if row + 1 <= 7:
            if self.grid[col][row + 1].color == "white":
                self.grid[col][row].w_legal = True
                return
        if col + 1 <= 7 and row - 1 >= 0:
            if self.grid[col + 1][row - 1].color == "white":
                self.grid[col][row].w_legal = True
                return
        if col + 1 <= 7:
            if self.grid[col + 1][row].color == "white":
                self.grid[col][row].w_legal = True
                return
        if col + 1 <= 7 and row + 1 <= 7:
            if self.grid[col + 1][row + 1].color == "white":
                self.grid[col][row].w_legal = True
                return
        else:
            #print("no adjacency")
            return False
