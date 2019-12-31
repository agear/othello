from typing import List, Set


class Board:
    """TODO"""

    def __init__(self, dimensions: int=8):
        assert dimensions % 2 == 0
        self.dimensions = dimensions
        self.layout = []
        self.gameover = False
        self.white_points = 0
        self.black_points = 0

        # Set up the grid
        for row in range(self.dimensions):
            row = []
            self.layout.append(row)
        for row in self.layout:
            for col in range(self.dimensions):
                tile = Tile()
                row.append(tile)

        # Set starting tiles
        self.layout[self.dimensions // 2][self.dimensions // 2].place(0)
        self.layout[(self.dimensions // 2) - 1][(self.dimensions // 2) - 1].place(0)
        self.layout[(self.dimensions // 2) - 1][self.dimensions // 2].place(1)
        self.layout[(self.dimensions // 2)][(self.dimensions // 2) - 1].place(1)

    def update_points(self) -> None:
        """TODO"""
        self.white_points, self.black_points = 0, 0
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if self.layout[row][col].color == 0:
                    self.white_points += 1
                elif self.layout[row][col].color == 1:
                    self.black_points += 1

    def flip(self, row: int, col: int) -> None:
        """TODO"""
        assert 0 <= row < self.dimensions
        assert 0 <= col < self.dimensions
        self.layout[row][col].flip()

    def place(self, row: int, col: int, player: int) -> List[tuple]:
        """TODO"""
        if player is 0:
            enemy = 1
        elif player is 1:
            enemy = 0

        assert (row, col) in self.get_legal(player)

        self.layout[row][col].place(player)

        updated = self.updateLayout(row=row, col=col, player=player)

        if not bool(self.get_legal(0)) and not bool(self.get_legal(1)):
            self.gameover = True
        return updated

    def updateLayout(self, row: int, col: int, player: int) -> List[tuple]:
        """TODO"""
        """Returns the list of updated coordinate tuples"""
        if player is 0:
            enemy = 1
        elif player is 1:
            enemy = 0

        updated = []

        # North
        try:
            if self.layout[row - 1][col].color == enemy:
                if self.check_vertical(direction="north", row=row - 1, col=col, player=player):
                    while row > 0:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                row -= 1
                            except:
                                break
                        else:
                            row -= 1
        except:
            pass

        # South
        try:
            if self.layout[row + 1][col].color == enemy:
                if self.check_vertical(direction="south", row=row + 1, col=col, player=player):
                    while row < self.dimensions:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                row += 1
                            except:
                                break
                        else:
                            row += 1
        except:
            pass

        # East
        try:
            if self.layout[row][col + 1].color == enemy:
                if self.check_horizontal(direction="east", row=row, col=col + 1, player=player):
                    while col < self.dimensions:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                col += 1
                            except:
                                break
                        else:
                            col += 1
        except:
            pass

        # West
        try:
            if self.layout[row][col - 1].color == enemy:
                if self.check_horizontal(direction="west", row=row, col=col - 1, player=player):
                    while col > 0:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                col -= 1
                            except:
                                break
                        else:
                            col -= 1
        except:
            pass

        # Northwest
        try:
            if self.layout[row - 1][col - 1].color == enemy:
                if self.check_diagonal(direction="northwest", row=row - 1, col=col - 1, player=player):
                    while row > 0 and col > 0:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                col -= 1
                                row -= 1
                            except:
                                break
                        else:
                            col -= 1
                            row -= 1
        except:
            pass

        # Northeast
        try:
            if self.layout[row - 1][col + 1].color == enemy:
                if self.check_diagonal(direction="northeast", row=row - 1, col=col + 1, player=player):
                    while row > 0 and col < self.dimensions:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                col += 1
                                row -= 1
                            except:
                                break
                        else:
                            col += 1
                            row -= 1
        except:
            pass

        # Southwest
        try:
            if self.layout[row + 1][col - 1].color == enemy:
                if self.check_diagonal(direction="southwest", row=row + 1, col=col - 1, player=player):
                    while row < self.dimensions and col > 0:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                col -= 1
                                row += 1
                            except:
                                break
                        else:
                            col -= 1
                            row += 1
        except:
            pass

        # Southeast
        try:
            if self.layout[row + 1][col + 1].color == enemy:
                if self.check_diagonal(direction="southeast", row=row + 1, col=col + 1, player=player):
                    while row < self.dimensions and col < self.dimensions:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                col += 1
                                row += 1
                            except:
                                break
                        else:
                            col += 1
                            row += 1
        except:
            pass

        self.update_points()

        return updated

    def get_legal(self, player: int) -> Set[tuple]:
        """TODO"""
        if player is 0:
            enemy = 1
        elif player is 1:
            enemy = 0

        legal = set()
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if not self.layout[row][col].occupied:
                    # Vertical
                    try:
                        if self.layout[row - 1][col].color == enemy:
                            if self.check_vertical(direction="north", row=row - 1, col=col, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row + 1][col].color == enemy:
                            if self.check_vertical(direction="south", row=row + 1, col=col, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    # Horizontal
                    try:
                        if self.layout[row][col + 1].color == enemy:
                            if self.check_horizontal(direction="east", row=row, col=col + 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    if self.layout[row][col - 1].color == enemy:
                        if self.check_horizontal(direction="west", row=row, col=col - 1, player=player):
                            legal.add((row, col))

                    # Diagonal
                    try:
                        if self.layout[row - 1][col + 1].color == enemy:
                            if self.check_diagonal(direction="northeast", row=row - 1, col=col + 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row - 1][col - 1].color == enemy:
                            if self.check_diagonal(direction="northwest", row=row - 1, col=col - 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row + 1][col + 1].color == enemy:
                            if self.check_diagonal(direction="southeast", row=row + 1, col=col + 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row + 1][col - 1].color == enemy:
                            if self.check_diagonal(direction="southwest", row=row + 1, col=col - 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

        # print(legal)
        return legal

    def check_vertical(self, direction: str, row: int, col: int, player: int) -> bool:
        """TODO"""
        assert direction == "north" or direction == "south"

        if direction is "north":
            # print("checking north")
            for checkrow in range(row, 0, -1):
                if self.layout[checkrow][col].color == player:
                    # print("Returning true from north")
                    return True
                elif not self.layout[checkrow][col].occupied:
                    return False
            return False

        elif direction is "south":
            # print("checking south")
            for checkrow in range(row, self.dimensions, 1):
                if self.layout[checkrow][col].color == player:
                    # print("Returning true from south")
                    return True
                elif not self.layout[checkrow][col].occupied:
                    return False
            return False

    def check_diagonal(self, direction: str, row: int, col: int, player: int) -> bool:
        """TODO"""
        assert direction == "northeast" \
               or direction == "northwest" \
               or direction == "southeast" \
               or direction == "southwest"

        if direction is "northeast":
            while row > 0 and col < self.dimensions:
                # print("Checking {}, {}".format(row, col))
                if self.layout[row][col].color == player:
                    # print("{}, {} is occupied by player".format(row, col))
                    return True
                elif not self.layout[row][col].occupied:
                    return False
                else:
                    row -= 1
                    col += 1
            return False

        elif direction is "northwest":
            while row > 0 and col > 0:
                # print("Checking {}, {}".format(row, col))
                if self.layout[row][col].color == player:
                    # print("{}, {} is occupied by player".format(row, col))
                    return True
                elif not self.layout[row][col].occupied:
                    return False
                else:
                    row -= 1
                    col -= 1
            return False

        elif direction is "southeast":
            while row < self.dimensions and col < self.dimensions:
                # print("Checking {}, {}".format(row, col))
                if self.layout[row][col].color == player:
                    # print("{}, {} is occupied by player".format(row, col))
                    return True
                elif not self.layout[row][col].occupied:
                    return False
                else:
                    row += 1
                    col += 1
            return False

        elif direction is "southwest":
            while row < self.dimensions and col > 0:
                # print("Checking {}, {}".format(row, col))
                if self.layout[row][col].color == player:
                    # print("{}, {} is occupied by player".format(row, col))
                    return True
                elif not self.layout[row][col].occupied:
                    return False
                else:
                    row += 1
                    col -= 1
            return False

    def check_horizontal(self, direction: str, row: int, col: int, player: int) -> bool:
        assert direction == "east" or direction == "west"

        if direction is "east":
            # print("checking east")
            for checkCol in range(col, self.dimensions, 1):
                if self.layout[row][checkCol].color == player:
                    # print("Returning true from east")
                    return True
                elif not self.layout[row][checkCol].occupied:
                    return False
            return False

        elif direction is "west":
            # print("checking west")
            for checkCol in range(col, 0, -1):
                if self.layout[row][checkCol].color == player:
                    # print("Returning true from west")
                    return True
                elif not self.layout[row][checkCol].occupied:
                    return False
            return False

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
    """TODO"""

    def __init__(self):
        self.occupied = False
        self.color = None

    def place(self, player: int) -> None:
        """TODO"""
        if self.occupied:
            raise ValueError('Tile is already occupied!')
        self.color = player
        self.occupied = True

    def flip(self) -> None:
        """TODO"""
        if self.color is None:
            raise ValueError('Tile is empty!')
        elif self.color is 0:
            self.color = 1
        elif self.color is 1:
            self.color = 0

    def __str__(self) -> str:
        if not self.occupied:
            return "[_]"
        elif self.color is 0:
            return "[w]"
        elif self.color is 1:
            return "[b]"
