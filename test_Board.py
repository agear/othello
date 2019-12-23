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
        b4.place(row=0, col=1, player=1)
        self.assertEqual('|[_][b][_][_]|\n|[_][b][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())
        # b4.place(row=0, col=1, player=1)
        # self.assertEqual('|[_][b][w][_]|\n|[_][w][b][_]|\n|[_][b][w][_]|\n|[_][_][_][_]|\n', b4.__str__())
        # self.assertRaises(AssertionError, b4.place, row=0, col=0, player=1)
        # self.assertRaises(AssertionError, b4.place, row=0, col=0, player=1)
        # self.assertRaises(AssertionError, b4.place, row=0, col=1, player=0)
        # self.assertRaises(AssertionError, b4.place, row=0, col=1, player=1)

    def test_getLegal(self):
        """TODO"""
        b = Board()
        legalwhite = set()
        legalwhite.add((4, 2))
        legalwhite.add((5, 3))
        legalwhite.add((2, 4))
        legalwhite.add((3, 5))
        self.assertEqual(legalwhite, b.getLegal(player=0))

        legalblack = set()
        legalblack.add((3, 2))
        legalblack.add((2, 3))
        legalblack.add((5, 4))
        legalblack.add((4, 5))
        self.assertEqual(legalblack, b.getLegal(player=1))

        b.layout[4][4].color = None
        b.layout[3][3].color = None
        b.layout[3][4].color = None
        b.layout[4][3].color = None

        b.layout[4][4].occupied = False
        b.layout[3][3].occupied = False
        b.layout[3][4].occupied = False
        b.layout[4][3].occupied = False

        empty = set()
        self.assertEqual(empty, b.getLegal(player=0))
        self.assertEqual(empty, b.getLegal(player=1))

# To Run tests from the editor/PyCharm
if __name__ == '__main__':
    unittest.main()
