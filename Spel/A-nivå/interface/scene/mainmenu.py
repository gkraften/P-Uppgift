from interface.scene import Scene
from interface.scene.colormenu import ColorMenu
import interface.assets as assets
from interface.component.button import Button

import sfml as sf

class MainMenu(Scene):
    """Class representing the main menu."""

    TITLE_SCALE = 1/10
    BUTTON_SCALE = 1/15

    def __init__(self, target):
        super().__init__(target)

        self.next_scene = None

        size = self.target.size

        font = sf.graphics.Font.from_file(assets.get_asset("/fonts/Amethyst.ttf"))

        # Title
        self.title = sf.graphics.Text()
        self.title.string = "Reversi"
        self.title.font = font
        self.title.character_size = int(size.y * self.TITLE_SCALE)
        self.title.color = sf.graphics.Color.WHITE
        title_bounds = self.title.global_bounds
        self.title.position = (size.x/2 - title_bounds.width/2, 10)

        # Menu items
        self.menuitems = []
        for item in [["Spela en spelare", self._switch_colormenu], ["Spela två spelare", None], ["Avsluta", target.close]]:
            button = Button(target, item[0])
            button.set_listener(item[1])
            self.menuitems.append(button)
        self._setup_buttons()

    def draw(self):
        self.target.clear(sf.graphics.Color.BLACK)

        self.target.draw(self.title)

        for item in self.menuitems:
            item.draw()

    def update(self, t):
        for button in self.menuitems:
            button.update(t)

        return self.next_scene

    def event(self, events):
        for button in self.menuitems:
            button.event(events)

        for e in events:
            if type(e) == sf.window.ResizeEvent:
                # Window has been resized. Resize components.
                size = self.target.size

                view = sf.graphics.View(sf.graphics.Rectangle((0, 0), (size.x, size.y)))
                self.target.view = view

                self.title.character_size = int(size.y * self.TITLE_SCALE)
                title_bounds = self.title.global_bounds
                self.title.position = (size.x / 2 - title_bounds.width / 2, 10)

                self._setup_buttons()

    def _setup_buttons(self):
        """Set the buttons positions and sizes."""

        for b in enumerate(self.menuitems):
            size = self.target.size

            button = b[1]

            button.set_character_size(size.y * self.BUTTON_SCALE)

            bounds = button.get_bounds()

            button.set_position((size.x / 2 - bounds[0] / 2, 2 * size.y / 6 + b[0] * size.y / 5))

    def _switch_colormenu(self):
        """Set scene to swtich to to ColorMenu."""

        self.next_scene = ColorMenu(self.target)
