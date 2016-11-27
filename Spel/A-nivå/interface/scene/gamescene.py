from interface.scene import Scene
from interface.scene.mainmenu import MainMenu
import interface.assets as assets
from interface.component.button import Button

from sfml import sf

import reversi

class GameScene(Scene):
    """Class that handles a game of reversi."""

    def __init__(self, size, single_player, color=None):
        """Instantiate GameScene. size is size of board,
        single_player is whether it is a single player
        game and color is the color of the player if it
        is a single player game."""

        super().__init__(self.target)

        if single_player and color is None:
            raise ValueError("Color must not be None if single_player is True.")

        self.single_player = single_player
        if single_player:
            self.color = color

        board = reversi.Board(size)
        self.game = reversi.Reversi(board)

        if single_player:
            self.bot = reversi.bot.Bot(self.game, -color)

        self.table_texture = sf.Texture.from_file(assets.get_asset("/images/table.png"))
        self.table = sf.Sprite(self.table_texture)
        self.table.origin = (self.table.local_bounds.width/2, self.table.local_bounds.height/2)

        self.setup_components()

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        self.target.draw(self.table)

    def setup_components(self):
        size = self.target.size

        view = sf.View()
        view.size = size
        view.center = (0, 0)
        self.target.view = view

        table_size = self.table_texture.size
        table_ratio = table_size.x/table_size.y
        window_ratio = size.x/size.y

        if window_ratio >= table_ratio:
            self.table.ratio = size.x/table_size.x
        elif window_ratio < table_ratio:
            self.table.ratio = size.y/table_size.y

