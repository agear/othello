class Board:

    def __init__(self, dimensions=8):
        assert dimensions % 2 == 0
        self.dimensions = dimensions
        self.layout = []
        for row in range(self.dimensions):
            row = []
            self.layout.append(row)
        for row in self.layout:
            for col in range(self.dimensions):
                tile = Tile()
                row.append(tile)
        #
        self.layout[self.dimensions//2][self.dimensions//2].place(0)
        self.layout[(self.dimensions // 2) -1][(self.dimensions // 2) -1].place(0)
        self.layout[(self.dimensions // 2) -1][self.dimensions // 2].place(1)
        self.layout[(self.dimensions // 2)][(self.dimensions // 2) - 1].place(1)

    def flip(self, row, col):
        assert 0 <= row < self.dimensions
        assert 0 <= col < self.dimensions
        self.layout[row][col].flip()

    def place(self, row, col, player):
        assert 0 <= row < self.dimensions
        assert 0 <= col < self.dimensions
        assert not self.layout[row][col].occupied

        self.layout[row][col].place(player)

    def isLegal(self, row, col, player):
        pass

    def __str__(self):
        strRep = ''
        edge = "|"
        for row in range(self.dimensions):
            strRep += edge
            for col in range(self.dimensions):
                strRep += self.layout[row][col].__str__()
            strRep += edge + "\n"

        return strRep

class Tile:

    def __init__(self):
        self.occupied = False
        self.color = None

    def place(self, player):
        if self.occupied:
            raise ValueError('Tile is already occupied!')
        self.color = player
        self.occupied = True

    def flip(self):
        if self.color is None:
            raise ValueError('Tile is empty!')
        elif self.color is 0:
            self.color = 1
        elif self.color is 1:
            self.color = 0

    def __str__(self):
        if not self.occupied:
            return "[_]"
        elif self.color is 0:
            return "[w]"
        elif self.color is 1:
            return "[b]"
