from interface.component import Component
import interface.assets as assets

from sfml import sf

class Button(Component):
    """A button that can be rendered to the screen."""

    def __init__(self, target, text, pos=(0, 0)):
        """Initialize new button with text text at
        position pos."""

        super().__init__(target)

        font = sf.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.text = sf.Text()
        self.text.string = text
        self.text.font = font
        self.text.color = sf.Color.WHITE

        self.set_character_size(18)
        self.set_position(pos)

        self.listener = None

    def draw(self):
        #target.draw(self.rect)
        self.target.draw(self.text)

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

    def _hovering(self):
        """Returns whether the mouse is above the button."""

        mpos = self.target.map_pixel_to_coords(sf.Mouse.get_position(self.target))

        pos = self.get_position()
        bounds = self.get_bounds()

        rect = sf.Rectangle(pos, bounds)

        return rect.contains(mpos)

    def event(self, e):
        for ev in e:
            if type(ev) == sf.MouseButtonEvent:
                if ev.pressed and self._hovering():
                    self.text.color = sf.Color(127, 0, 0)
                if ev.released and self._hovering() and not self.listener is None:
                    self.listener()
            elif type(ev) == sf.MouseMoveEvent and not sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
                if self._hovering():
                    self.text.color = sf.Color.RED
                else:
                    self.text.color = sf.Color.WHITE
