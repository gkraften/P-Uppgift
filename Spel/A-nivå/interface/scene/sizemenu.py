from interface.scene import Scene
from interface.scene.gamescene import GameScene
import interface.assets as assets
from interface.component.spinner import Spinner
from interface.component.button import Button

from sfml import sf

class SizeMenu(Scene):
    """Class representing a menu that lets player
    choose size of board."""

    TITLE_SCALE = 1/10
    SCALE = 1/15

    def __init__(self, target, single_player, color=None):
        """Instantiate SizeMenu. target is window to draw to,
        single_player is whether a single player game is to
        be played and color is the color the player wants to
        play as in case of single player."""

        super().__init__(target)

        if single_player and color is None:
            raise ValueError("Color must not be None if single_player is True.")

        self.next_scene = None

        self.single_player = single_player
        self.color = color

        font = sf.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.title = sf.Text()
        self.title.string = "Välj storlek på brädet"
        self.title.font = font

        self.size = Spinner(target, 4, 20, 2, 8)

        self.next = Button(target, "Fortsätt")
        self.next.set_listener(self._switch_to_game)

        self.add_component(self.size)
        self.add_component(self.next)

        self._setup_components()

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        self.target.draw(self.title)

        for c in self.components:
            c.draw()

    def event(self, events):
        super().event(events)

        for e in events:
            if type(e) == sf.ResizeEvent:
                size = self.target.size

                view = sf.View(sf.Rectangle((0, 0), (size.x, size.y)))
                self.target.view = view

                self._setup_components()

    def update(self, t):
        super().update(t)

        return self.next_scene

    def _setup_components(self):
        size = self.target.size

        self.title.character_size = size.y * self.TITLE_SCALE
        title_bounds = self.title.local_bounds
        self.title.position = (size.x / 2 - title_bounds.width / 2, 10)

        self.size.set_character_size(size.y * self.SCALE)
        bounds = self.size.get_bounds()
        self.size.set_position((size.x/2 - bounds[0]/2, size.y/2 - bounds[1]/2))

        self.next.set_character_size(size.y * self.SCALE)
        next_bounds = self.next.get_bounds()
        self.next.set_position((size.x/2 - next_bounds[0]/2, 3*size.y/4 - next_bounds[1]/2))

    def _switch_to_game(self):
        self.next_scene = GameScene(self.target, self.size.get_value(), self.single_player, self.color)