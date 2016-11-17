from interface.scene import Scene

import sfml as sf

class MainMenu(Scene):
    """Class representing the main menu."""

    TITLE_SCALE = 1/10

    def __init__(self, target):
        super().__init__(target)

        size = self.target.size

        font = sf.graphics.Font.from_file("/home/oscar/Skrivbord/P-Uppgift/Spel/A-nivå/assets/Amethyst.ttf")

        self.title = sf.graphics.Text()
        self.title.string = "Reversi"
        self.title.font = font
        self.title.character_size = size.y * self.TITLE_SCALE
        self.title.color = sf.graphics.Color.BLACK
        title_bounds = self.title.global_bounds
        self.title.position = (size.x/2 - title_bounds.width/2, 10)

    def draw(self):
        self.target.clear(sf.graphics.Color.CYAN)

        self.target.draw(self.title)

    def update(self, t):
        return None

    def event(self, events):
        pass
