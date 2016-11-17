from interface.scene import Scene

import sfml as sf

class MainMenu(Scene):
    """Class representing the main menu."""

    def draw(self):
        self.target.clear(sf.graphics.Color.CYAN)

    def update(self, t):
        return None