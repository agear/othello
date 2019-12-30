import unittest
from Board import Board
from Board import Tile

class TestBoard(unittest.TestCase):
    """TODO"""
    def test_Tile(self):
        """TODO"""
        tile = Tile()
        self.assertEqual(tile.occupied, False)
        self.assertEqual(tile.color, None)
        self.assertRaises(ValueError, tile.flip)
        self.assertEqual("[_]", tile.__str__())
        tile.place(0)
        self.assertEqual(tile.color, 0)
        self.assertRaises(ValueError, tile.place, 1)
        self.assertEqual(tile.occupied, True)
        self.assertEqual(tile.color, 0)
        tile.flip()
        self.assertEqual(tile.occupied, True)
        self.assertEqual(tile.color, 1)
        self.assertEqual("[b]", tile.__str__())
        tile.flip()
        self.assertEqual(tile.occupied, True)
        self.assertEqual(tile.color, 0)
        self.assertEqual("[w]", tile.__str__())

    def test_BoardStr(self):
        """TODO"""
        b2 = Board(dimensions=2)
        self.assertEqual('|[w][b]|\n|[b][w]|\n', b2.__str__())
        # Board dimensions must be divisible by 2
        self.assertRaises(AssertionError, Board, dimensions=3 )
        b4 = Board(dimensions=4)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())
        b8 = Board(dimensions=8)
        self.assertEqual('|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_]' \
                         '[_][w][b][_][_][_]|\n|[_][_][_][b][w][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n' \
                         '|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n', b8.__str__())


    def test_flip(self):
        """TODO"""
        b2 = Board(2)
        self.assertRaises(AssertionError, b2.flip, row=-1, col=-1)
        self.assertRaises(AssertionError, b2.flip, row=4, col=4)
        self.assertRaises(AssertionError, b2.flip, row=-1, col=1)
        self.assertRaises(AssertionError, b2.flip, row=4, col=1)
        self.assertRaises(AssertionError, b2.flip, row=1, col=-1)
        self.assertRaises(AssertionError, b2.flip, row=1, col=4)
        b2.flip(row=0, col=0)
        b2.flip(row=0, col=1)
        b2.flip(row=1, col=0)
        b2.flip(row=1, col=1)
        self.assertEqual('|[b][w]|\n|[w][b]|\n', b2.__str__())

    def test_place(self):
        """TODO"""
        b2 = Board(2)
        self.assertRaises(AssertionError, b2.place, row=-1, col=-1, player=0)
        self.assertRaises(AssertionError, b2.place, row=4, col=4, player=0)
        self.assertRaises(AssertionError, b2.place, row=-1, col=1, player=0)
        self.assertRaises(AssertionError, b2.place, row=4, col=1, player=1)
        self.assertRaises(AssertionError, b2.place, row=1, col=-1, player=1)
        self.assertRaises(AssertionError, b2.place, row=1, col=4, player=1)

        # Test each white opening move
        b4 = Board(4)
        b4.place(row=0, col=2, player=0)
        self.assertEqual('|[_][_][w][_]|\n|[_][w][w][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        b4 = Board(4)
        b4.place(row=2, col=0, player=0)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[w][w][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        b4 = Board(4)
        b4.place(row=1, col=3, player=0)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][w][w]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        b4 = Board(4)
        b4.place(row=3, col=1, player=0)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][w][w][_]|\n|[_][w][_][_]|\n', b4.__str__())

        # Test each black opening move
        b4 = Board(4)
        b4.place(row=1, col=0, player=1)
        self.assertEqual('|[_][_][_][_]|\n|[b][b][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        b4 = Board(4)
        b4.place(row=0, col=1, player=1)
        self.assertEqual('|[_][b][_][_]|\n|[_][b][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        b4 = Board(4)
        b4.place(row=3, col=2, player=1)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][b][b][_]|\n|[_][_][b][_]|\n', b4.__str__())

        b4 = Board(4)
        b4.place(row=2, col=3, player=1)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][b][b][b]|\n|[_][_][_][_]|\n', b4.__str__())

        # Set up an empty board
        b8 = Board()

        b8.layout[4][4].color = None
        b8.layout[3][3].color = None
        b8.layout[3][4].color = None
        b8.layout[4][3].color = None

        b8.layout[4][4].occupied = False
        b8.layout[3][3].occupied = False
        b8.layout[3][4].occupied = False
        b8.layout[4][3].occupied = False
        self.assertEqual('|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n', b8.__str__())


        b8.layout[0][0].color = 0
        b8.layout[0][0].occupied = True

        b8.layout[1][1].color = 1
        b8.layout[1][1].occupied = True

        b8.layout[2][2].color = 1
        b8.layout[2][2].occupied = True

        b8.layout[4][4].color = 1
        b8.layout[4][4].occupied = True

        b8.layout[5][5].color = 0
        b8.layout[5][5].occupied = True

        b8.layout[6][6].color = 1
        b8.layout[6][6].occupied = True

        b8.layout[7][7].color = 1
        b8.layout[7][7].occupied = True

        self.assertEqual('|[w][_][_][_][_][_][_][_]|\n|[_][b][_][_][_][_][_][_]|\n|[_][_][b][_][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][_][b][_][_][_]|\n|[_][_][_][_][_][w][_][_]|\n|[_][_][_][_][_][_][b][_]|\n|[_][_][_][_][_][_][_][b]|\n', b8.__str__())

        b8.layout[0][3].color = 0
        b8.layout[0][3].occupied = True

        b8.layout[1][3].color = 1
        b8.layout[1][3].occupied = True

        b8.layout[2][3].color = 1
        b8.layout[2][3].occupied = True

        b8.layout[4][3].color = 1
        b8.layout[4][3].occupied = True

        b8.layout[5][3].color = 0
        b8.layout[5][3].occupied = True

        b8.layout[6][3].color = 1
        b8.layout[6][3].occupied = True

        b8.layout[7][3].color = 1
        b8.layout[7][3].occupied = True

        self.assertEqual('|[w][_][_][w][_][_][_][_]|\n|[_][b][_][b][_][_][_][_]|\n|[_][_][b][b][_][_][_][_]|\n|[_][_][_][_][_][_][_][_]|\n|[_][_][_][b][b][_][_][_]|\n|[_][_][_][w][_][w][_][_]|\n|[_][_][_][b][_][_][b][_]|\n|[_][_][_][b][_][_][_][b]|\n', b8.__str__())

        b8.layout[3][0].color = 0
        b8.layout[3][0].occupied = True

        b8.layout[3][1].color = 1
        b8.layout[3][1].occupied = True

        b8.layout[3][2].color = 1
        b8.layout[3][2].occupied = True

        b8.layout[3][4].color = 1
        b8.layout[3][4].occupied = True

        b8.layout[3][5].color = 0
        b8.layout[3][5].occupied = True

        b8.layout[3][6].color = 1
        b8.layout[3][6].occupied = True

        b8.layout[3][7].color = 1
        b8.layout[3][7].occupied = True

        print("\n", b8)
        self.assertEqual('|[w][_][_][w][_][_][_][_]|\n|[_][b][_][b][_][_][_][_]|\n|[_][_][b][b][_][_][_][_]|\n|[w][b][b][_][b][w][b][b]|\n|[_][_][_][b][b][_][_][_]|\n|[_][_][_][w][_][w][_][_]|\n|[_][_][_][b][_][_][b][_]|\n|[_][_][_][b][_][_][_][b]|\n', b8.__str__())

        b8.place(row=3, col=3, player=0)
        print("\n", b8)
        # self.assertEqual('|[w][_][_][w][_][_][_][_]|\n|[_][w][_][w][_][_][_][_]|\n|[_][_][w][w][_][_][_][_]|\n|[w][w][w][w][w][w][b][b]|\n|[_][_][_][w][w][_][_][_]|\n|[_][_][_][w][_][w][_][_]|\n|[_][_][_][b][_][_][b][_]|\n|[_][_][_][b][_][_][_][b]|\n', b8.__str__())

        # self.assertRaises(AssertionError, b4.place, row=0, col=0, player=1)
        # self.assertRaises(AssertionError, b4.place, row=0, col=0, player=1)
        # self.assertRaises(AssertionError, b4.place, row=0, col=1, player=0)
        # self.assertRaises(AssertionError, b4.place, row=1, col=1, player=1)

    def test_getLegal(self):
        """TODO"""
        # Test correct legal opening moves for white
        b = Board()
        legalwhite = set()
        legalwhite.add((4, 2))
        legalwhite.add((5, 3))
        legalwhite.add((2, 4))
        legalwhite.add((3, 5))
        self.assertEqual(legalwhite, b.get_legal(player=0))

        # Test correct legal opening moves for black
        legalblack = set()
        legalblack.add((3, 2))
        legalblack.add((2, 3))
        legalblack.add((5, 4))
        legalblack.add((4, 5))
        self.assertEqual(legalblack, b.get_legal(player=1))

        # Test that an empty board has no legal moves
        b.layout[4][4].color = None
        b.layout[3][3].color = None
        b.layout[3][4].color = None
        b.layout[4][3].color = None

        b.layout[4][4].occupied = False
        b.layout[3][3].occupied = False
        b.layout[3][4].occupied = False
        b.layout[4][3].occupied = False

        empty = set()
        self.assertEqual(empty, b.get_legal(player=0))
        self.assertEqual(empty, b.get_legal(player=1))

        # Test diagonals

        # Test Northwest
        b4 = Board(4)

        b4.layout[2][2].flip()
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][b][b][_]|\n|[_][_][_][_]|\n', b4.__str__())

        legalwhite = set()
        legalwhite.add((1, 3))
        legalwhite.add((3, 1))
        legalwhite.add((3, 3))
        self.assertEqual(legalwhite, b4.get_legal(player=0))
        b4.place(row=3, col=3, player=0)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][b][w][_]|\n|[_][_][_][w]|\n', b4.__str__())


        # Test Northeast
        b4 = Board(4)

        b4.layout[2][1].flip()
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][w][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        legalblack = set()
        legalblack.add((1, 0))
        legalblack.add((3, 0))
        legalblack.add((3, 2))
        self.assertEqual(legalblack, b4.get_legal(player=1))
        b4.place(row=3, col=0, player=1)
        self.assertEqual('|[_][_][_][_]|\n|[_][w][b][_]|\n|[_][b][w][_]|\n|[b][_][_][_]|\n', b4.__str__())


        # Test Southwest
        b4 = Board(4)

        b4.layout[1][2].flip()
        self.assertEqual('|[_][_][_][_]|\n|[_][w][w][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        legalblack = set()
        legalblack.add((0, 1))
        legalblack.add((0, 3))
        legalblack.add((2, 3))
        self.assertEqual(legalblack, b4.get_legal(player=1))
        b4.place(row=0, col=3, player=1)
        self.assertEqual('|[_][_][_][b]|\n|[_][w][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())


        # Test Southeast
        b4 = Board(4)

        b4.layout[1][1].flip()
        self.assertEqual('|[_][_][_][_]|\n|[_][b][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())

        legalwhite = set()
        legalwhite.add((0, 0))
        legalwhite.add((0, 2))
        legalwhite.add((2, 0))
        self.assertEqual(legalwhite, b4.get_legal(player=0))
        b4.place(row=0,col=0,player=0)
        self.assertEqual('|[w][_][_][_]|\n|[_][w][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())



# To Run tests from the editor/PyCharm
if __name__ == '__main__':
    unittest.main()
