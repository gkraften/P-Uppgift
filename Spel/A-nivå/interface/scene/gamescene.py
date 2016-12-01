from interface.scene import Scene
import interface.assets as assets
from interface.component.button import Button

from sfml import sf

import reversi
import reversi.bot

class GameScene(Scene):
    """Class that handles a game of reversi."""

    MSG_SCALE = 1/10
    SKIP_SCALE = 1/15

    def __init__(self, target, size, single_player, color=None):
        """Instantiate GameScene. size is size of board,
        single_player is whether it is a single player
        game and color is the color of the player if it
        is a single player game."""

        super().__init__(target)

        if single_player and color is None:
            raise ValueError("Color must not be None if single_player is True.")

        if single_player:
            self.translation = {color: "Du", -color: "Datorn"}
        else:
            self.translation = {reversi.WHITE: "Vit", reversi.BLACK: "Svart"}

        self.board_size = size

        self.single_player = single_player
        if single_player:
            self.color = color

        board = reversi.Board(size)
        self.game = reversi.Reversi(board)

        if single_player:
            self.bot = reversi.bot.Bot(self.game, -color)

        self.table_texture = sf.Texture.from_file(assets.get_asset("/images/table.png"))
        self.table_texture.smooth = True
        self.table = self._get_sprite(self.table_texture)

        self.board_centre = sf.Texture.from_file(assets.get_asset("/images/board_centre.png"))
        self.board_centre.smooth = True
        self.board_corner = sf.Texture.from_file(assets.get_asset("/images/board_corner.png")) # Top left corner
        self.board_corner.smooth = True
        self.board_edge = sf.Texture.from_file(assets.get_asset("/images/board_edge.png")) # Top edge

        font = sf.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.msg = sf.Text()
        self.msg.string = self.translation[self.game.get_turn()] + " ska spela"
        self.msg.font = font

        self.skip = Button(self.target, "Skippa tur")
        self.add_component(self.skip)

        self.board_tiles = []
        for row in range(size):
            r = []
            for col in range(size):
                sprite = None
                if row == col == 0: # Top left
                    sprite = self._get_sprite(self.board_corner)
                elif row == col == size-1: # Bottom right
                    sprite = self._get_sprite(self.board_corner)
                    sprite.rotate(180)
                elif row == 0 and col == size-1: # Top right
                    sprite = self._get_sprite(self.board_corner)
                    sprite.rotate(90)
                elif row == size-1 and col == 0: # Bottom left
                    sprite = self._get_sprite(self.board_corner)
                    sprite.rotate(-90)
                elif row == 0: # Top edge
                    sprite = self._get_sprite(self.board_edge)
                elif row == size-1: # Bottom edge
                    sprite = self._get_sprite(self.board_edge)
                    sprite.rotate(180)
                elif col == 0: # Left edge
                    sprite = self._get_sprite(self.board_edge)
                    sprite.rotate(-90)
                elif col == size-1: # Right edge
                    sprite = self._get_sprite(self.board_edge)
                    sprite.rotate(90)
                else: # Centre
                    sprite = self._get_sprite(self.board_centre)

                r.append(sprite)

            self.board_tiles.append(r)
        print(len(self.board_tiles))

        self._setup_components()

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        self.target.draw(self.table)

        self.target.draw(self.msg)

        self.skip.draw()

        for row in self.board_tiles:
            for tile in row:
                self.target.draw(tile)

    def event(self, e):
        super().event(e)

        for ev in e:
            if type(ev) == sf.ResizeEvent:
                self._setup_components()

    def _setup_components(self):
        size = self.target.size

        view = sf.View()
        view.size = size
        view.center = (0, 0)
        self.target.view = view

        tile_size = self.board_centre.size
        table_size = self.table_texture.size
        table_ratio = table_size.x/table_size.y
        window_ratio = size.x/size.y

        self.msg.character_size = size.y * self.MSG_SCALE
        self.msg.position = (-self.msg.local_bounds.width/2, -size.y/2 + 10)

        self.skip.set_character_size(size.y * self.SKIP_SCALE)
        skip_size = self.skip.get_bounds()
        self.skip.set_position((3*size.x/8 - skip_size[0]/2, skip_size[1]/2))

        if window_ratio >= table_ratio:
            r = size.x/table_size.x
            self.table.ratio = (r, r)
        elif window_ratio < table_ratio:
            r = size.y/table_size.y
            self.table.ratio = (r, r)

        ratio = size.y/(1.375*tile_size.y*self.board_size)
        scaled_tile_size = tile_size.x * ratio
        l_edge = (-self.board_size * scaled_tile_size + scaled_tile_size) / 2
        t_edge = (-self.board_size * scaled_tile_size + scaled_tile_size) / 2

        for row in range(self.board_size):
            for col in range(self.board_size):
                self.board_tiles[row][col].ratio = (ratio, ratio)
                self.board_tiles[row][col].position = (l_edge + col*scaled_tile_size, t_edge + row*scaled_tile_size)

    def _get_sprite(self, texture):
        """Initializes a sprite with texture texture
        and sets its origin to centre."""

        size = texture.size

        sprite = sf.Sprite(texture)
        sprite.origin = (size.x/2, size.y/2)

        return sprite

