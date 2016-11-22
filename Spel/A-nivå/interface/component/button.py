from interface.component import Component
import interface.assets as assets

import sfml as sf

class Button(Component):
    """A button that can be rendered to the screen."""

    _MARGIN = 10

    def __init__(self, text, pos=(0, 0)):
        """Initialize new button with text text at
        position pos."""

        font = sf.graphics.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.text = sf.graphics.Text()
        self.text.string = text
        self.text.font = font
        self.text.character_size = 18
        self.text.color = sf.graphics.Color.WHITE
        self.text.position = (pos[0], pos[1] + self._MARGIN)

        text_bounds = self.text.local_bounds
        self.rect = sf.graphics.RectangleShape((text_bounds.width + 2*self._MARGIN, text_bounds.height + 2*self._MARGIN))
        self.rect.fill_color = sf.graphics.Color.RED
        self.rect.position = pos

        self.listener = None

    def draw(self, target):
        target.draw(self.rect)
        target.draw(self.text)

    def set_text(self, text):
        """Set text displayed on the button."""

        self.text.string = text

    def get_position(self):
        """Returns the buttons position."""

        pos = self.rect.position
        return (pos.x - self._MARGIN, pos.y - self._MARGIN)

    def set_position(self, pos):
        """Sets the buttons position to pos."""

        self.text.position = (pos[0] + self._MARGIN, pos[1] + self._MARGIN)
        self.rect.position = pos

    def get_bounds(self):
        """Get width and height of the button."""

        return (self.text.global_bounds.width + self._MARGIN, self.text.global_bounds.height + self._MARGIN)

    def set_listener(self, func):
        """Set function to execute when the button
        is clicked."""

        self.listener = func

    def set_character_size(self, size):
        """Set character size."""

        self.text.character_size = size
