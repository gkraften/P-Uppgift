from interface.scene import Scene
from interface.scene.sizemenu import SizeMenu
import interface.assets as assets
from interface.component.button import Button

import sfml as sf

import reversi

class ColorMenu(Scene):
    """Class representing menu that lets the player
    choose the color to play as."""

    TITLE_SCALE = 1/10
    BUTTON_SCALE = 1/15

    def __init__(self, target):
        super().__init__(target)

        self.next_scene = None

        font = sf.graphics.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.title = sf.graphics.Text()
        self.title.string = "Vilken färg vill du spela som?"
        self.title.font = font

        self.button_white = Button(self.target, "Vit")
        self.button_black = Button(self.target, "Svart")

        self.add_component(self.button_white)
        self.add_component(self.button_black)

        self._setup_components()

    def draw(self):
        self.target.clear(sf.graphics.Color.BLACK)

        self.target.draw(self.title)

        for c in self.components:
            c.draw()

    def event(self, events):
        super().event(events)

        for e in events:
            if type(e) == sf.window.ResizeEvent:
                size = self.target.size

                view = sf.graphics.View(sf.graphics.Rectangle((0, 0), (size.x, size.y)))
                self.target.view = view

                self._setup_components()

    def update(self, t):
        super().update(t)

        return self.next_scene

    def _setup_components(self):
        size = self.target.size

        self.title.character_size = size.y * self.TITLE_SCALE
        title_bounds = self.title.local_bounds
        self.title.position = (size.x/2 - title_bounds.width/2, 10)

        self.button_black.set_character_size(size.y * self.BUTTON_SCALE)
        black_bounds = self.button_black.get_bounds()
        self.button_black.set_position((size.x/4 - black_bounds[0]/2, size.y/2 - black_bounds[1]/2))

        self.button_white.set_character_size(size.y * self.BUTTON_SCALE)
        white_bounds = self.button_white.get_bounds()
        self.button_white.set_position((3*size.x / 4 - white_bounds[0] / 2, size.y / 2 - white_bounds[1] / 2))

    def _switch_size_white(self):
        self.next_scene = SizeMenu(self.target, True, reversi.WHITE)

    def _switch_size_white(self):
        self.next_scene = SizeMenu(self.target, True, reversi.BLACK)
