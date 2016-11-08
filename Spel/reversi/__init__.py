import itertools
import reversi.exceptions
import random


WHITE = 1
BLACK = -1
EMPTY = 0


class Board:
    '''A class representing the board and what's placed on it.'''

    def __init__(self, size):
        '''Initialize a new board of dimensions size*size. It will be initialized
        with two black and two white pieces placed on diagonals in the center.
        size must be a multiple of 2 and greater than 2.'''

        if size % 2 != 0:
            raise ValueError("size must be a multiple of 2.")

        if size <= 2:
            raise ValueError("size must be greater than 2.")

        self.size = size

        self.board = []
        for r in range(size):
            row = []
            for c in range(size):
                row.append(0)
            self.board.append(row)


        # Put initial pieces on the board
        self.board[size//2 - 1][size//2 - 1] = WHITE
        self.board[size//2][size//2] = WHITE
        self.board[size//2 - 1][size//2] = BLACK
        self.board[size//2][size//2 - 1] = BLACK

        self.n_pieces = {WHITE: 2, BLACK: 2, "total": 4}

    def get_board_list(self):
        '''Returns the underlying 2-dimensional list
        that represents the board. The returned list
        should not be modified.'''

        return self.board

    def is_empty(self, row, col):
        '''Returns whether the cell at row row and column col is empty or not'''

        return self.board[row][col] == EMPTY

    def is_full(self):
        '''Returns whether the board has been filled or not.'''

        return self.size**2 - self.n_pieces["total"] == 0

    def flips(self, type, row, col):
        '''Returns a list containing the positions of all pieces that would
        be flipped if a piece of color type were to be placed at row row
        and column col. If none are flipped or if the cell is occupied an
        empty list is returned.'''

        if not self.is_empty(row, col):
            return []

        # Directions is a list of all possible directions to move in the grid
        directions = list(itertools.product([-1, 0, 1], repeat=2))
        del directions[directions.index((0, 0))]

        # Move in all directions and follow pieces of opposite color until
        # an empty cell, the boarder of the board or a piece of color type
        # is encountered
        flipped = []
        for direction in directions:
            candidates = []
            pos = (row + direction[0], col + direction[1])
            while 0 <= pos[0] <= self.size-1 and 0 <= pos[1] <= self.size-1 and self.board[pos[0]][pos[1]] == -type:
                candidates.append(pos)
                pos = (pos[0] + direction[0], pos[1] + direction[1])

            if 0 <= pos[0] <= self.size-1 and 0 <= pos[1] <= self.size-1:
                flipped += candidates

        return flipped

    def nflips(self, type, row, col):
        '''Returns how many pieces would be flipped if a piece of color type
        were to be placed at row row and column col. Returns zero if no pieces would
        be flipped or if the cell at row row and column col is already occupied.'''

        return len(self.flips(type, row, col))

    def place(self, type, row, col):
        '''Places a piece of color type at row row and column col. If the cell
        is occupied or if no pieces are flipped or if the cell lies outside of the board
        an exception will be raised. Returns a list with the positions of all
        pieces that were flipped.'''

        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError("row and col must lie between 0 and %d" % self.size)

        if not self.is_empty(row, col):
            raise reversi.exceptions.OccupiedCellException("Cell at row %d and column %d is occupied" % (row, col))

        flipped = self.flips(type, row, col)
        if len(flipped) == 0:
            raise reversi.exceptions.NoFlipsException("Piece placed at row %d and column %d does not flip any pieces" % (row, col))

        self.board[row][col] = type
        for flip in flipped:
            self.board[flip[0]][flip[1]] = type
        self.n_pieces["total"] += 1
        self.n_pieces[type] += 1

        return flipped

    def get_n_white(self):
        '''Returns the number of white pieces on the board.'''

        return self.n_pieces[WHITE]

    def get_n_black(self):
        '''Returns the number of black pieces on the board.'''

        return self.n_pieces[BLACK]



class Reversi:
    '''A class representing a game of reversi.'''

    def __init__(self, board):
        '''Initializes a game using board board of type Board. The color that
        starts is randomized.'''

        self.board = board
        self.turn = random.choice([reversi.WHITE, reversi.BLACK])

        self.skipped = {reversi.WHITE: False, reversi.BLACK: False}

    def set_turn(self, type):
        '''Sets whose turn it is.'''

        self.turn = type

    def get_turn(self):
        '''Returns whose turn it is.'''

        return self.turn

    def place(self, row, col):
        '''Places a piece of same type as whose turn it currently is at row row
        and column col. Raises the same exceptions as Board.place. Returns a
        list with the positions of all pieces that were flipped.'''

        flipped = self.board.place(self.turn, row, col)
        self.skipped[self.turn] = False
        self.turn *= -1

        return flipped

    def skip(self):
        '''Lets the color whose turn it currently is to skip its turn.'''

        self.skipped[self.turn] = True
        self.turn *= -1

    def winner(self):
        '''If both players have skipped their turn or if the board is full a list
        containing the color that has won and by how many pieces is returned. If
        there is a draw a list containing a 0 is returned. If no one has won yet,
        None is returned.'''

        if self.board.is_full() or (self.skipped[BLACK] and self.skipped[WHITE]): #There is a winner
            n_black = self.board.get_n_black()
            n_white = self.board.get_n_white()

            if n_black == n_white: # A draw
                return [0]
            else:
                winner = BLACK if n_black > n_white else WHITE
                return [winner, abs(n_black - n_white)]
        else:
            return None