import arcade

from models.PlayerModel import PlayerModel
from controllers.PlayerController import PlayerController
from views.sprites.PlayerSprite import PlayerSprite
from views.Console import Console

from typing import Optional

import Constants as C


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(C.SCREEN_WIDTH, C.SCREEN_HEIGHT, C.SCREEN_TITLE)
        self.physics_engine = Optional[arcade.PymunkPhysicsEngine]

    def setup(self):
        playerModel = PlayerModel()
        self.models.append(playerModel)

         # Map name
        map_name = "assets/scenes/tile_basic_ground.json"

        # Load in TileMap
        tile_map = arcade.load_tilemap(map_name, C.SPRITE_SCALING_TILES)
        self.tile_map_list = tile_map.sprite_lists["tile_basic_ground"]

        self.sprites = arcade.SpriteList()

        playerSprite = PlayerSprite(playerModel)
        playerSprite.center_x = 5 * C.SPRITE_SIZE
        playerSprite.center_y = 6 * C.SPRITE_SIZE
        self.sprites.append(playerSprite)
        gravity = (0, -C.GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=C.DEFAULT_DAMPING,gravity=gravity)
        self.physics_engine.add_sprite(playerSprite,
                                       friction=C.PLAYER_FRICTION,
                                       mass=C.PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=C.PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=C.PLAYER_MAX_VERTICAL_SPEED)
        
        self.physics_engine.add_sprite_list(self.tile_map_list,
                                            friction=C.WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
        
        playerController = PlayerController(playerModel, self, playerSprite)
        self.controllers.append(playerController)

        self.console = Console(self, playerController)
        
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.console.on_draw_start()

        self.clear()
        #arcade.start_render()

        self.tile_map_list.draw()
        self.sprites.draw()

        self.console.on_draw_end()

    def update(self, dt):
        self.console.on_update_start()

        self.physics_engine.step()

        for controller in self.controllers:
            controller.on_update(dt)
        for sprite in self.sprites:
            sprite.on_update(dt)

        self.console.on_update_end()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.exit()
            return
        # if symbol == arcade.key.BACKSPACE:
        #     self.setup()
        #     return
        for controller in self.controllers:
            controller.on_keypress(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for controller in self.controllers:
            controller.on_keyrelease(symbol, modifiers)

    sprites = None
    controllers = []
    models = []
    