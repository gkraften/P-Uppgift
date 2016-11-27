from interface.component import Component
from interface.component.button import Button
import interface.assets as assets

from sfml import sf

class Spinner(Component):
    """Spinner allowing you to choose a number."""

    MARGIN = 5

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
        self.more.set_listener(self.increment)
        self.less = Button(target, "Mindre")
        self.less.set_listener(self.decrement)

        font = sf.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.display = sf.Text()
        self.display.font = font
        self.display.string = str(self.value)

        self.set_character_size(14)
        self.set_position((0, 0))

    def draw(self):
        self.target.draw(self.display)
        self.less.draw()
        self.more.draw()

    def update(self, t):
        self.more.update(t)
        self.less.update(t)

    def event(self, events):
        self.more.event(events)
        self.less.event(events)

    def set_character_size(self, size):
        self.display.character_size = size
        self.more.set_character_size(size)
        self.less.set_character_size(size)

    def get_position(self):
        return self.pos

    def set_position(self, pos):
        self.pos = pos

        disp_bounds = self.display.local_bounds
        less_bounds = self.less.get_bounds()
        more_bounds = self.more.get_bounds()

        self.display.position = (pos[0] + (less_bounds[0] + self.MARGIN + more_bounds[0])/2 - disp_bounds.width/2, pos[1])
        self.less.set_position((pos[0], pos[1] + disp_bounds.height + self.MARGIN))
        self.more.set_position((pos[0] + less_bounds[0] + self.MARGIN, pos[1] + disp_bounds.height + self.MARGIN))

    def get_bounds(self):
        disp_bounds = self.display.local_bounds
        less_bounds = self.less.get_bounds()
        more_bounds = self.more.get_bounds()

        return (less_bounds[0] + self.MARGIN + more_bounds[0], disp_bounds.height + self.MARGIN + less_bounds[1])

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

        self.display.string = str(val)
        self.set_position(self.pos)

    def increment(self):
        val = self.value + self.step
        if val > self.high:
            val = self.high

        self.set_value(val)

    def decrement(self):
        val = self.value - self.step
        if val < self.low:
            val = self.low

        self.set_value(val)
