from interface.scene import Scene
import interface.assets as assets
from interface.component.button import Button
from interface.component.piece import Piece

from sfml import sf

import reversi
import reversi.bot
from reversi.highscore import Highscore

class GameScene(Scene):
    """Class that handles a game of reversi."""

    MSG_SCALE = 1/10
    SKIP_SCALE = 1/15

    HIGHSCORE_PATH = assets.get_asset("/../highscore.txt")

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

        Highscore.load(self.HIGHSCORE_PATH)
        self.highscore = False

        self.board_size = size

        self.single_player = single_player
        if single_player:
            self.color = color

        self.time = sf.seconds(0)

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

        self.shadow_texture = sf.Texture.from_file(assets.get_asset("/images/shadow.png"))
        self.shadow_texture.smooth = True
        self.shadow = self._get_sprite(self.shadow_texture)

        font = sf.Font.from_file(assets.get_asset("/fonts/GeosansLight.ttf"))
        self.msg = sf.Text()
        self.msg.string = self.translation[self.game.get_turn()] + " ska spela"
        self.msg.font = font

        self.skip = Button(self.target, "Skippa tur")
        self.skip.set_listener(self._skip_pressed)
        self.add_component(self.skip)

        self.pieces = []
        for row in range(size):
            r = []
            for col in range(size):
                if not board.is_empty(row, col):
                    piece = Piece(target, board.get_board_list()[row][col])
                    r.append(piece)
                    self.add_component(piece)
                else:
                    r.append(None)
            self.pieces.append(r)

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

        self._setup_components()

    def draw(self):
        self.target.clear(sf.Color.BLACK)

        self.target.draw(self.table)

        self.target.draw(self.msg)

        self.target.draw(self.shadow)

        for row in self.board_tiles:
            for tile in row:
                self.target.draw(tile)

        for c in self.components:
            c.draw()

    def event(self, e):
        super().event(e)

        for ev in e:
            if type(ev) == sf.ResizeEvent:
                self._setup_components()
            elif type(ev) == sf.MouseButtonEvent and ev.released: # Player tries to place piece
                if (not self.single_player or self.game.get_turn() == self.color) and self.game.winner() is None: # Check that you are allowed to play
                    mpos = self.target.map_pixel_to_coords(sf.Mouse.get_position(self.target))
                    for row in range(self.board_size):
                        for col in range(self.board_size):
                            bounds = self.board_tiles[row][col].global_bounds
                            if bounds.contains(mpos):
                                # Try to place piece
                                try:
                                    flipped = self.game.place(row, col)

                                    piece = Piece(self.target, -self.game.get_turn())
                                    piece.set_position(self._grid_position(row, col))
                                    self.pieces[row][col] = piece
                                    self.add_component(piece)

                                    for pos in flipped:
                                        self.pieces[pos[0]][pos[1]].flip()

                                    self.msg.string = self.translation[self.game.get_turn()] + " ska spela"

                                    self._setup_components()
                                except:
                                    pass
                                break

    def update(self, t):
        super().update(t)

        winner = self.game.winner()
        if winner:
            self.time += t
            if winner[0] == 0:
                self.msg.string = "Det blev oavgjort!"
            else:
                self.msg.string = self.translation[winner[0]] + " har vunnit med " + str(winner[1]) + " brickor!"
                if Highscore.get_highscore() < winner[1]:
                    Highscore.set_highscore(winner[1])
                    Highscore.save(self.HIGHSCORE_PATH)
                    self.highscore = True

            if self.highscore:
                if self.time.seconds >= 6:
                    from interface.scene.mainmenu import MainMenu
                    return MainMenu(self.target)
                elif self.time.seconds >= 3:
                    self.msg.string = "Nytt highscore dessutom!"
            elif self.time.seconds >= 3:
                from interface.scene.mainmenu import MainMenu
                return MainMenu(self.target)

            self._setup_components()
        elif self.single_player and self.game.get_turn() == -self.color:
            self.time += t
            if self.time.seconds >= 1:
                self.time = sf.seconds(0)

                flipped = self.bot.play()
                if flipped is None:
                    self.msg.string = "Datorn skippade sin runda"
                else:
                    self.msg.string = self.translation[self.game.get_turn()] + " ska spela"
                    for pos in flipped[:-1]:
                        self.pieces[pos[0]][pos[1]].flip()

                    new = flipped[-1]
                    piece = Piece(self.target, -self.color)
                    piece.set_position(self._grid_position(*new))
                    self.pieces[new[0]][new[1]] = piece
                    self.add_component(piece)
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

        ratio = 8*size.y/(9*self.shadow_texture.size.y)
        self.shadow.ratio = (ratio, ratio)

        if window_ratio >= table_ratio:
            r = size.x/table_size.x
            self.table.ratio = (r, r)
        elif window_ratio < table_ratio:
            r = size.y/table_size.y
            self.table.ratio = (r, r)

        ratio = size.y/(1.375*tile_size.y*self.board_size)

        for row in range(self.board_size):
            for col in range(self.board_size):
                self.board_tiles[row][col].ratio = (ratio, ratio)
                self.board_tiles[row][col].position = self._grid_position(row, col)

                if not self.pieces[row][col] is None:
                    self.pieces[row][col].set_position(self._grid_position(row, col))
                    self.pieces[row][col].set_scale(ratio)

    def _grid_position(self, row, col):
        """Row and col are positions in game grid. Returns
        position in world coordinates."""

        size = self.target.size
        tile_size = self.board_centre.size

        ratio = size.y / (1.375 * tile_size.y * self.board_size)
        scaled_tile_size = tile_size.x * ratio
        l_edge = (-self.board_size * scaled_tile_size + scaled_tile_size) / 2
        t_edge = (-self.board_size * scaled_tile_size + scaled_tile_size) / 2

        return (l_edge + col*scaled_tile_size, t_edge + row*scaled_tile_size)

    def _get_sprite(self, texture):
        """Initializes a sprite with texture texture
        and sets its origin to centre."""

        size = texture.size

        sprite = sf.Sprite(texture)
        sprite.origin = (size.x/2, size.y/2)

        return sprite

    def _skip_pressed(self):
        if not self.game.winner() is None or (self.single_player and self.game.get_turn() != self.color):
            return

        self.game.skip()
        self.msg.string = self.translation[self.game.get_turn()] + " ska spela"
