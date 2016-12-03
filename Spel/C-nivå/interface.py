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

def get_int(msg, error):
    success = False
    val = None
    while not success:
        try:
            val = int(input(msg))
            success = True
        except ValueError:
            print(error)

    return val

def get_row_col(size):
    '''Returns selected row and column. size is the
    size of the board.'''

    row = get_int("Välj RAD att placera pjäs på: ", "Raden måste vara en siffra")
    while not 1 <= row <= size:
        print("Raden måste ligga mellan 1 och %d" % size)
        row = get_int("Välj RAD att placera pjäs på: ", "Raden måste vara en siffra")

    col_input = input("Välj KOLUMN att placera pjäs på: ").upper()
    while len(col_input) != 1 or not (col_input in string.ascii_uppercase and string.ascii_uppercase.index(col_input) < size):
        print("Kolumnen måste vara en bokstav mellan A och %s" % string.ascii_uppercase[size])
        col_input = input("Välj KOLUMN att placera pjäs på: ").upper()

    col = string.ascii_uppercase.index(col_input)

    return (row-1, col)

def should_skip():
    '''Returns whether the user wants to skip its
    turn or not.'''

    skip = input("Vill du stå över din runda (enter för nej, vad som helst för ja)?")

    return len(skip) != 0

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
                print("○", end="")
            elif elem == reversi.BLACK:
                print("●", end="")
            else:
                print(" ", end="")
            print(" | ", end="")
        print()
        print_separator(width, offset)