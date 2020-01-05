from typing import List, Set

DIRECTIONS = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]

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
        # if player is 0:
        #     enemy = 1
        # elif player is 1:
        #     enemy = 0

        assert (row, col) in self.get_legal(player)

        self.layout[row][col].place(player)

        updated = self.updateLayout(row=row, col=col, player=player)

        if not bool(self.get_legal(player=0)) and not bool(self.get_legal(player=1)):
            self.gameover = True
        return updated

    def direction(self, f1, f2, row, col, f3, enemy, f4):
        updated = []
        try:
            if f1:
                if f2:
                    while f3:
                        if self.layout[row][col].color == enemy:
                            try:
                                self.flip(row=row, col=col)
                                updated.append((row, col))
                                f4
                            except:
                                break
                        else:
                            f4
        except:
            pass

        return updated

    def updateLayout(self, row: int, col: int, player: int) -> List[tuple]:
        """TODO"""
        """Returns the list of updated coordinate tuples"""
        if player is 0:
            enemy = 1
        elif player is 1:
            enemy = 0

        updated = []

        increment = lambda x: x + 1
        decrement = lambda x: x - 1
        static = lambda x: x

        # North
        try:
            condition1 = self.layout[row - 1][col].color == enemy
            condition2 = self.check_direction(direction="north", row=row - 1, col=col, player=player)
            condition3 = row > 0
            condition4 = True

            update_row = decrement
            update_col = static

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # # North
        # try:
        #     if self.layout[row - 1][col].color == enemy:
        #         if self.check_direction(direction="north", row=row - 1, col=col, player=player):
        #             while row > 0:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         row -= 1
        #                     except:
        #                         # To break out of while loop ???
        #                         row = -1
        #                         break
        #                 else:
        #                     row -= 1
        # except:
        #     pass

        # South
        try:
            condition1 = self.layout[row + 1][col].color == enemy
            condition2 = self.check_direction(direction="south", row=row + 1, col=col, player=player)
            condition3 = row < self.dimensions
            condition4 = True

            update_row = increment
            update_col = static

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # South
        # try:
        #     if self.layout[row + 1][col].color == enemy:
        #         if self.check_direction(direction="south", row=row + 1, col=col, player=player):
        #             while row < self.dimensions:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         row += 1
        #                     except:
        #                         row = self.dimensions + 1
        #                         break
        #                 else:
        #                     row += 1
        # except:
        #     pass

        # East
        try:
            condition1 = self.layout[row][col + 1].color == enemy
            condition2 = self.check_direction(direction="east", row=row, col=col + 1, player=player)
            condition3 = col < self.dimensions
            condition4 = True

            update_row = static
            update_col = increment

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # East
        # try:
        #     if self.layout[row][col + 1].color == enemy:
        #         if self.check_direction(direction="east", row=row, col=col + 1, player=player):
        #             while col < self.dimensions:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         col += 1
        #                     except:
        #                         col = self.dimensions + 1
        #                         break
        #                 else:
        #                     col += 1
        # except:
        #     pass

        # West
        try:
            condition1 = self.layout[row][col - 1].color == enemy
            condition2 = self.check_direction(direction="west", row=row, col=col - 1, player=player)
            condition3 = col > 0
            condition4 = True

            update_row = static
            update_col = decrement

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # # West
        # try:
        #     if self.layout[row][col - 1].color == enemy:
        #         if self.check_direction(direction="west", row=row, col=col - 1, player=player):
        #             while col > 0:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         col -= 1
        #                     except:
        #                         col = -1
        #                         break
        #                 else:
        #                     col -= 1
        # except:
        #     pass

        # Northwest
        try:
            condition1 = self.layout[row - 1][col - 1].color == enemy
            condition2 = self.check_direction(direction="northwest", row=row - 1, col=col - 1, player=player)
            condition3 = row > 0
            condition4 = col > 0

            update_row = decrement
            update_col = decrement

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # Northwest
        # try:
        #     if self.layout[row - 1][col - 1].color == enemy:
        #         if self.check_direction(direction="northwest", row=row - 1, col=col - 1, player=player):
        #             while row > 0 and col > 0:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         col -= 1
        #                         row -= 1
        #                     except:
        #                         col = -1
        #                         row = -1
        #                         break
        #                 else:
        #                     col -= 1
        #                     row -= 1
        # except:
        #     pass

        # Northeast
        try:
            condition1 = self.layout[row - 1][col + 1].color == enemy
            condition2 = self.check_direction(direction="northeast", row=row - 1, col=col + 1, player=player)
            condition3 = row > 0
            condition4 = col < self.dimensions

            update_row = decrement
            update_col = increment

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # # Northeast
        # try:
        #     if self.layout[row - 1][col + 1].color == enemy:
        #         if self.check_direction(direction="northeast", row=row - 1, col=col + 1, player=player):
        #             while row > 0 and col < self.dimensions:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         col += 1
        #                         row -= 1
        #                     except:
        #                         col = self.dimensions + 1
        #                         row = -1
        #                         break
        #                 else:
        #                     col += 1
        #                     row -= 1
        # except:
        #     pass

        # Southwest
        try:
            condition1 = self.layout[row + 1][col - 1].color == enemy
            condition2 = self.check_direction(direction="southwest", row=row + 1, col=col - 1, player=player)
            condition3 = row < self.dimensions
            condition4 = col > 0

            update_row = increment
            update_col = decrement

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        # Southwest
        # try:
        #     if self.layout[row + 1][col - 1].color == enemy:
        #         if self.check_direction(direction="southwest", row=row + 1, col=col - 1, player=player):
        #             while row < self.dimensions and col > 0:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         col -= 1
        #                         row += 1
        #                     except:
        #                         col = -1
        #                         row = self.dimensions + 1
        #                         break
        #                 else:
        #                     col -= 1
        #                     row += 1
        # except:
        #     pass

        # Southeast
        # try:
        #     if self.layout[row + 1][col + 1].color == enemy:
        #         if self.check_direction(direction="southeast", row=row + 1, col=col + 1, player=player):
        #             while row < self.dimensions and col < self.dimensions:
        #                 if self.layout[row][col].color == enemy:
        #                     try:
        #                         self.flip(row=row, col=col)
        #                         updated.append((row, col))
        #                         col += 1
        #                         row += 1
        #                     except:
        #                         col = self.dimensions + 1
        #                         row = self.dimensions + 1
        #                         break
        #                 else:
        #                     col += 1
        #                     row += 1
        # except:
        #     pass

        # Southeast
        try:
            condition1 = self.layout[row + 1][col + 1].color == enemy
            condition2 = self.check_direction(direction="southeast", row=row + 1, col=col + 1, player=player)
            condition3 = row < self.dimensions
            condition4 = col < self.dimensions

            update_row = increment
            update_col = increment

            updated = self.abstract(row=row, col=col, enemy=enemy, condition1=condition1, condition2=condition2, condition3=condition3, condition4=condition4, update_row=update_row, update_col=update_col, updated=updated)
        except:
            pass

        self.update_points()

        return updated

    def abstract(self, row, col, enemy, condition1, condition2, condition3, condition4, update_row, update_col, updated):
        if condition1:
            if condition2:
                while condition3 and condition4:
                    if self.layout[row][col].color == enemy:
                        try:
                            self.flip(row=row, col=col)
                            updated.append((row, col))
                            row = update_row(row)
                            col = update_col(col)
                        except:
                            break
                    else:
                        row = update_row(row)
                        col = update_col(col)

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
                            if self.check_direction(direction="north", row=row - 1, col=col, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row + 1][col].color == enemy:
                            if self.check_direction(direction="south", row=row + 1, col=col, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    # Horizontal
                    try:
                        if self.layout[row][col + 1].color == enemy:
                            if self.check_direction(direction="east", row=row, col=col + 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    if self.layout[row][col - 1].color == enemy:
                        if self.check_direction(direction="west", row=row, col=col - 1, player=player):
                            legal.add((row, col))

                    # Diagonal
                    try:
                        if self.layout[row - 1][col + 1].color == enemy:
                            if self.check_direction(direction="northeast", row=row - 1, col=col + 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row - 1][col - 1].color == enemy:
                            if self.check_direction(direction="northwest", row=row - 1, col=col - 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row + 1][col + 1].color == enemy:
                            if self.check_direction(direction="southeast", row=row + 1, col=col + 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

                    try:
                        if self.layout[row + 1][col - 1].color == enemy:
                            if self.check_direction(direction="southwest", row=row + 1, col=col - 1, player=player):
                                legal.add((row, col))
                    except:
                        pass

        # print(legal)
        return legal

    def check_direction(self, direction: str, row: int, col: int, player: int) -> bool:
        """TODO"""

        assert direction in DIRECTIONS

        increment = lambda x: x + 1
        decrement = lambda x: x - 1
        static = lambda x: x

        if direction is "north":
            condition1 = row > 0
            condition2 = True
            update_row = decrement
            update_col = static

        elif direction is "northeast":
            condition1 = row > 0
            condition2 = col < self.dimensions
            update_row = decrement
            update_col = increment

        elif direction is "east":
            condition1 = col < self.dimensions
            condition2 = True
            update_row = static
            update_col = increment

        elif direction is "southeast":
            condition1 = row < self.dimensions
            condition2 = col < self.dimensions
            update_row = increment
            update_col = increment

        elif direction is "south":
            condition1 = row < self.dimensions
            condition2 = True
            update_row = increment
            update_col = static

        elif direction is "southwest":
            condition1 = row < self.dimensions
            condition2 = col > 0
            update_row = increment
            update_col = decrement

        elif direction is "west":
            condition1 = col > 0
            condition2 = True
            update_row = static
            update_col = decrement

        elif direction is "northwest":
            condition1 = row > 0
            condition2 = col > 0
            update_row = decrement
            update_col = decrement

        while condition1 and condition2:
            if self.layout[row][col].color == player:
                return True
            elif not self.layout[row][col].occupied:
                return False
            else:
                row = update_row(row)
                col = update_col(col)
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
