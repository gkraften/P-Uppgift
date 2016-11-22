from interface.component import Component
import interface.assets as assets

import sfml as sf

class Button(Component):
    """A button that can be rendered to the screen."""

    def __init__(self, text, pos=(0, 0)):
        """Initialize new button with text text at
        position pos."""

        font = sf.graphics.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.text = sf.graphics.Text()
        self.text.string = text
        self.text.font = font
        self.text.color = sf.graphics.Color.WHITE

        self.set_character_size(18)
        self.set_position(pos)

        self.listener = None

    def draw(self, target):
        #target.draw(self.rect)
        target.draw(self.text)

    def set_text(self, text):
        """Set text displayed on the button."""

        self.text.string = text

    def get_position(self):
        """Returns the buttons position."""

        return self.text.position

    def set_position(self, pos):
        """Sets the buttons position to pos."""

        self.text.position = pos

    def get_bounds(self):
        """Get width and height of the button."""

        bounds = self.text.global_bounds
        return (bounds.width, bounds.height)

    def set_listener(self, func):
        """Set function to execute when the button
        is clicked."""

        self.listener = func

    def set_character_size(self, size):
        """Set character size."""

        self.text.character_size = size

    def update(self, t):
        pass
