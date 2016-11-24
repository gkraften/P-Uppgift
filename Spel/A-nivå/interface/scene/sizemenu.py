from interface.scene import Scene
import interface.assets as assets
from interface.component.button import Button

import sfml as sf

class SizeMenu(Scene):
    """Class representing a menu that lets player
    choose size of board."""

    TITLE_SCALE = 1 / 10

    def __init__(self, target, single_player, color=None):
        """Instantiate SizeMenu. target is window to draw to,
        single_player is whether a single player game is to
        be played and color is the color the player wants to
        play as in case of single player."""

        super().__inti__(target)

        if single_player and color is None:
            raise ValueError("Color must not be None if single_player is True.")

        self.single_player = single_player
        self.color = color

        font = sf.graphics.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.title = sf.graphics.Text()
        self.title.string = "Välj storlek på brädet"

    def draw(self):
        self.target.clear(sf.graphics.Color.BLACK)

        self.target.draw(self.title)

    def event(self, events):
        super().event(events)

        for e in events:
            if type(e) == sf.window.ResizeEvent:
                size = self.target.size

                view = sf.graphics.View(sf.graphics.Rectangle((0, 0), (size.x, size.y)))
                self.target.view = view

                self._setup_components()

    def _setup_components(self):
        size = self.target.size

        self.title.character_size = size.y * self.TITLE_SCALE
        title_bounds = self.title.local_bounds
        self.title.position = (size.x / 2 - title_bounds.width / 2, 10)