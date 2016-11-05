class OccupiedCellException(Exception):
    '''Exception raised when a piece is placed on a cell that is already
    occupied.'''

    def __init__(self, message):
        super().__init__(message)

class NoFlipsException(Exception):
    '''Exception raised when a piece is placed in a way that no pieces
    are flipped.'''

    def __init__(self, message):
        super().__init__(message)

class WrongTurnException(Exception):
    '''Exception raised by Bot when it tries to play when it is not
    its turn.'''

    def __init__(self, message):
        super().__init__(message)