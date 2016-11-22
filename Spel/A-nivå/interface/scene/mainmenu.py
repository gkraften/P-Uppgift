from interface.scene import Scene

import sfml as sf

class MainMenu(Scene):
    """Class representing the main menu."""

    TITLE_SCALE = 1/10

    def __init__(self, target):
        super().__init__(target)

        size = self.target.size

        font = sf.graphics.Font.from_file("/home/oscar/Skrivbord/P-Uppgift/Spel/A-nivå/assets/Amethyst.ttf")

        # Title
        self.title = sf.graphics.Text()
        self.title.string = "Reversi"
        self.title.font = font
        self.title.character_size = int(size.y * self.TITLE_SCALE)
        self.title.color = sf.graphics.Color.WHITE
        title_bounds = self.title.global_bounds
        self.title.position = (size.x/2 - title_bounds.width/2, 10)

    def draw(self):
        self.target.clear(sf.graphics.Color.BLACK)

        self.target.draw(self.title)

    def update(self, t):
        return None

    def event(self, events):
        for e in events:
            if type(e) == sf.window.ResizeEvent:
                # Window has been resized. Resize components.
                size = self.target.size

                view = sf.graphics.View(sf.graphics.Rectangle((0, 0), (size.x, size.y)))
                self.target.view = view

                self.title.character_size = int(size.y * self.TITLE_SCALE)
                title_bounds = self.title.global_bounds
                self.title.position = (size.x / 2 - title_bounds.width / 2, 10)
