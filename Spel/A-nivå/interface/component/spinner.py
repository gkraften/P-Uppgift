from interface.component import Component
from interface.component import Button
import interface.assets as assets

from sfml import sf

class Spinner(Component):
    """Spinner allowing you to choose a number."""

    def __init__(self, target, low, high, step):
        """Initialize a new Spinner. target is window to
        draw to, low is lower boundary, high is higher
        boundary and step is the step size."""

        super().__init__(target)

        self.character_size = 14

        self.up = Button(target, "▲")
        self.add_component(self.up)

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        for c in self.components:
            c.draw()