import reversi
import string
import math

def print_separator(width, offset):
    '''Print a line separating two rows in the board.'''

    print(" "*offset, end="")
    print("—"*width)

def digits(d):
    '''Returns the number of digits in d.'''

    return int(math.log10(d)) + 1

def get_row_col():
    '''Returns selected row and column or (None, None)
    if the user wants to skip its turn.'''

    row_input = input("Välj RAD att placera pjäs på (tryck endast enter för att stå över): ")
    if row_input == "":
        return (None, None)

    col_input = input("Välj KOLUMN att placera pjäs på (tryck endast enter för att stå över): ")
    if col_input == "":
        return (None, None)

    row = int(row_input) - 1
    col = string.ascii_uppercase.index(col_input.upper())

    return (row, col)

def display_board(b):
    '''Print the board b. The width must be max 26.'''

    board = b.get_board_list()

    if len(board) > 26:
        raise ValueError("Size of board must not exceed 26.")

    n_digits = digits(len(board))
    offset = n_digits + 2

    print(" "*(offset+1), end="")

    width = 0
    for i in range(len(board)):
        print(string.ascii_uppercase[i % 26], end="   ")
        width += 4
    width -= 1
    print()

    print_separator(width, offset)

    for index,row in enumerate(board):
        print(index+1, end=" "*(n_digits - digits(index+1)) + " | ")
        for elem in row:
            if elem == reversi.WHITE:
                print("v", end="")
            elif elem == reversi.BLACK:
                print("s", end="")
            else:
                print(" ", end="")
            print(" | ", end="")
        print()
        print_separator(width, offset)