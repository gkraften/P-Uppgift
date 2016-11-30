from interface.scene import Scene
import interface.assets as assets
from interface.component.button import Button

from sfml import sf

import reversi
import reversi.bot

class GameScene(Scene):
    """Class that handles a game of reversi."""

    def __init__(self, target, size, single_player, color=None):
        """Instantiate GameScene. size is size of board,
        single_player is whether it is a single player
        game and color is the color of the player if it
        is a single player game."""

        super().__init__(target)

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
        self.table_texture.smooth = True
        self.table = sf.Sprite(self.table_texture)
        self.table.origin = (self.table.local_bounds.width/2, self.table.local_bounds.height/2)

        self._setup_components()

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        self.target.draw(self.table)

    def event(self, e):
        super().event(e)

        for ev in e:
            if type(ev) == sf.ResizeEvent:
                self._setup_components()

    def _setup_components(self):
        size = self.target.size

        view = sf.View()
        view.size = size
        view.center = (0, 0)
        self.target.view = view

        table_size = self.table_texture.size
        table_ratio = table_size.x/table_size.y
        window_ratio = size.x/size.y

        if window_ratio >= table_ratio:
            print("Första")
            r = size.x/table_size.x
            self.table.ratio = (r, r)
        elif window_ratio < table_ratio:
            print("Andra")
            r = size.y/table_size.y
            self.table.ratio = (r, r)

