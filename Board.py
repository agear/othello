from typing import List, Set, Callable

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
        self.setup()



    def setup(self):
        """TODO"""
        for row in range(self.dimensions):
            row = []
            self.layout.append(row)
        for row in self.layout:
            for col in range(self.dimensions):
                tile = Tile()
                row.append(tile)
        self.set_start_tiles()

    def clear_tile(self, row: int, col: int) -> None:
        """TODO"""
        self.layout[row][col].color = None
        self.layout[row][col].occupied = False

    def clear_board(self) -> None:
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                self.clear_tile(row=row, col=col)


    def set_start_tiles(self):
        """TODO"""
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

        assert (row, col) in self.get_legal(player)

        self.layout[row][col].place(player)

        updated = self.updateLayout(row=row, col=col, player=player)

        self.gameover = self.is_gameover()
        return updated

    def raw_place(self, row: int, col: int, player: int) -> None:
        self.layout[row][col].place(player)

    def is_gameover(self) -> bool:
        return not bool(self.get_legal(player=0)) and not bool(self.get_legal(player=1))

    def get_opponent(self, player: int) -> int:
        assert player is 0 or player is 1
        if player is 0:
            return 1
        else:
            return 0


    def updateLayout(self, row: int, col: int, player: int) -> List[tuple]:
        """TODO"""
        """Returns the list of updated coordinate tuples"""

        opponent = self.get_opponent(player=player)

        updated = []

        increment = lambda x: x + 1
        decrement = lambda x: x - 1
        static = lambda x: x

        # North
        try:
            condition1 = self.check_direction(direction="north", row=row - 1, col=col, player=player)
            condition2 = row > 0
            condition3 = True

            update_row = decrement
            update_col = static

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # Northeast
        try:
            condition1 = self.check_direction(direction="northeast", row=row - 1, col=col + 1, player=player)
            condition2 = row > 0
            condition3 = col < self.dimensions

            update_row = decrement
            update_col = increment

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # East
        try:
            condition1 = self.check_direction(direction="east", row=row, col=col + 1, player=player)
            condition2 = col < self.dimensions
            condition3 = True

            update_row = static
            update_col = increment

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # Southeast
        try:
            condition1 = self.check_direction(direction="southeast", row=row + 1, col=col + 1, player=player)
            condition2 = row < self.dimensions
            condition3 = col < self.dimensions

            update_row = increment
            update_col = increment

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # South
        try:
            condition1 = self.check_direction(direction="south", row=row + 1, col=col, player=player)
            condition2 = row < self.dimensions
            condition3 = True

            update_row = increment
            update_col = static

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # Southwest
        try:
            condition1 = self.check_direction(direction="southwest", row=row + 1, col=col - 1, player=player)
            condition2 = row < self.dimensions
            condition3 = col > 0

            update_row = increment
            update_col = decrement

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # West
        try:
            condition1 = self.check_direction(direction="west", row=row, col=col - 1, player=player)
            condition2 = col > 0
            condition3 = True

            update_row = static
            update_col = decrement

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        # Northwest
        try:
            condition1 = self.check_direction(direction="northwest", row=row - 1, col=col - 1, player=player)
            condition2 = row > 0
            condition3 = col > 0

            update_row = decrement
            update_col = decrement

            updated = self.get_updates(row=row, col=col, opponent=opponent, condition1=condition1,
                                       condition2=condition2, condition3=condition3, update_row=update_row,
                                       update_col=update_col, updated=updated)
        except:
            pass

        self.update_points()

        return updated

    def get_updates(self, row: int, col: int, opponent: int, condition1: bool, condition2: bool, condition3: bool,
                    update_row: Callable[[int], int], update_col: Callable[[int],int],
                    updated: List[tuple]) -> List[tuple]:
        """TODO"""
        urow = row
        ucol = col
        if condition1:  # Check if the move is legal
            while condition2 and condition3: # Check that we haven't gone outside the boundary
                if self.layout[urow][ucol].color == opponent:
                    self.flip(row=urow, col=ucol)
                    updated.append((urow, ucol))
                    urow = update_row(urow)
                    ucol = update_col(ucol)
                elif not self.layout[urow][ucol].occupied:
                    break
                elif self.layout[urow][ucol] != opponent and (urow != row or ucol != col):
                    break
                else:
                    urow = update_row(urow)
                    ucol = update_col(ucol)

        return updated

    def helper(self, collection: tuple, row: int, col: int, player: int, opponent: int, legal: Set[tuple]) -> Set[tuple]:
        try:
            if self.layout[collection[1]][collection[2]].color == opponent:
                if self.check_direction(direction=collection[0], row=collection[1], col=collection[2], player=player):
                    legal.add((row, col))
            return legal
        except:
            return legal

    def get_legal(self, player: int) -> Set[tuple]:
        """TODO"""

        opponent = self.get_opponent(player=player)

        legal = set()
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if not self.layout[row][col].occupied:

                    northTuple = ("north", row-1, col)
                    northeastTuple = ("northeast", row-1, col+1)
                    eastTuple = ("east", row, col+1)
                    southeastTuple = ("southeast", row+1, col+1)
                    southTuple = ("south", row+1, col)
                    southwestTuple = ("southwest", row + 1, col - 1)
                    westTuple = ("west", row, col-1)
                    northwestTuple = ("northwest", row - 1, col - 1)

                    legal = self.helper(collection=northTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=northeastTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=eastTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=southeastTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=southTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=southwestTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=westTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)
                    legal = self.helper(collection=northwestTuple, row=row, col=col, player=player, opponent=opponent, legal=legal)


                    # # Diagonal
                    # try:
                    #     if self.layout[row - 1][col + 1].color == opponent:
                    #         if self.check_direction(direction="northeast", row=row - 1, col=col + 1, player=player):
                    #             legal.add((row, col))
                    # except:
                    #     pass
                    #
                    # try:
                    #     if self.layout[row - 1][col - 1].color == opponent:
                    #         if self.check_direction(direction="northwest", row=row - 1, col=col - 1, player=player):
                    #             legal.add((row, col))
                    # except:
                    #     pass
                    #
                    # try:
                    #     if self.layout[row + 1][col + 1].color == opponent:
                    #         if self.check_direction(direction="southeast", row=row + 1, col=col + 1, player=player):
                    #             legal.add((row, col))
                    # except:
                    #     pass
                    #
                    # try:
                    #     if self.layout[row + 1][col - 1].color == opponent:
                    #         if self.check_direction(direction="southwest", row=row + 1, col=col - 1, player=player):
                    #             legal.add((row, col))
                    # except:
                    #     pass

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
