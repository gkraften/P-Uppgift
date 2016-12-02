from interface.component import Component
import interface.assets as assets
import reversi
import math

from sfml import sf

class Piece(Component):
    """A piece that can be placed on the board."""

    FLIP_TIME = 0.5

    def __init__(self, target, color):
        super().__init__(target)

        self.color = color

        self.time = sf.seconds(0)

        self.flipping = False

        self.black_tex = sf.Texture.from_file(assets.get_asset("/images/black.png"))
        self.black_tex.smooth = True
        self.white_tex = sf.Texture.from_file(assets.get_asset("/images/white.png"))
        self.white_tex.smooth = True

        self.texture_size = self.black_tex.size

        self.size = self.texture_size.x

        self.black = sf.Sprite(self.black_tex)
        self.black.origin = (self.texture_size.x/2, self.texture_size.y/2)
        self.white = sf.Sprite(self.white_tex)
        self.white.origin = (self.texture_size.x / 2, self.texture_size.y / 2)

    def draw(self):
        c = self.color
        if self.flipping and self.time.seconds < self.FLIP_TIME/2:
            c *= -1

        if c == reversi.BLACK:
            self.target.draw(self.black)
        else:
            self.target.draw(self.white)

    def update(self, t):
        if self.flipping:
            self.time += t

            if self.time.seconds < self.FLIP_TIME:
                ratio = self.max_scale/2 * math.sin(2*math.pi/self.FLIP_TIME * self.time.seconds + math.pi/2) + self.max_scale/2 # Apply a "smooth" animation
                self.set_scale(ratio)
            else:
                self.flipping = False
                self.set_scale(self.max_scale)

    def flip(self):
        """Flip the piece to change color."""

        self.max_scale = self.scale
        self.time = sf.seconds(0)
        self.color *= -1
        self.flipping = True

    def set_position(self, pos):
        self.black.position = pos
        self.white.position = pos

    def set_scale(self, scale):
        self.scale = scale
        self.black.ratio = (scale, scale)
        self.white.ratio = (scale, scale)