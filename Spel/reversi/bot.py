from reversi.exceptions import WrongTurnException

class Bot:
    '''A class representing a reversi-playing bot. Can be used to play
    one-player games.'''


    def __init__(self, game, type):
        '''Initializes the bot with the game game of type Reversi. type is the
        color that the bot plays as.'''

        self.game = game
        self.type = type


    def play(self):
        '''Makes a move. Raises an exception if it is not the bot's turn.
        Returns a list of all pieces that were flipped and None if it skipped its
        turn.'''

        if self.type != self.game.get_turn():
            raise WrongTurnException("It is not currently the bots turn")

