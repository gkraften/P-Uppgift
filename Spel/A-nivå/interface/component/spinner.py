from interface.component import Component
from interface.component.button import Button
import interface.assets as assets

from sfml import sf

class Spinner(Component):
    """Spinner allowing you to choose a number."""

    def __init__(self, target, low, high, step, init=None):
        """Initialize a new Spinner. target is window to
        draw to, low is lower boundary, high is higher
        boundary, step is the step size and init is
        the initial value."""

        super().__init__(target)

        self.low = low
        self.high = high
        self.step = step
        if init is None:
            self.value = low
        else:
            self.value = init

        self.more = Button(target, "Större")
        self.less = Button(target, "Mindre")

        font = sf.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.display = sf.Text()
        self.display.font = font
        self.display.string = str(self.value)

        self.set_character_size(14)

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        self.target.draw(self.display)
        self.less.draw()
        self.more.draw()

    def set_character_size(self, size):
        self.display.character_size = size
        self.more.set_character_size(size)
        self.less.set_character_size(size)

    def set_position(self, pos):
        disp_bounds = self.display.local_bounds
        less_bounds = self.less.get_bounds()

        self.display.position = pos
        self.less.set_position((pos[0], pos[1] + disp_bounds.height + 5))
        self.more.set_position((pos[0] + less_bounds[0] + 5, pos[1] + disp_bounds.height + 5))
