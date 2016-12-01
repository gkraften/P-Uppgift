from interface.component import Component
import interface.assets as assets
import reversi

from sfml import sf

class Piece(Component):
    """A piece that can be placed on the board."""

    def __init__(self, target, color):
        super().__init__(target)

        self.color = color

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
        if self.color == reversi.BLACK:
            self.target.draw(self.black)
        else:
            self.target.draw(self.white)

    def flip(self):
        """Flip the piece to change color."""

        self.color *= -1

    def set_position(self, pos):
        self.black.position = pos
        self.white.position = pos

    def set_size(self, size):
        self.size = size

        scale = size/self.texture_size.x

        self.black.ratio = (scale, scale)
        self.white.ratio = (scale, scale)