import arcade

from typing import Optional
from pyglet.math import Vec2

from models.PlayerModel import PlayerModel
from controllers.PlayerController import PlayerController
from views.sprites.PlayerSprite import PlayerSprite
from views.Console import Console

import Constants as C


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(C.SCREEN_WIDTH, C.SCREEN_HEIGHT, C.SCREEN_TITLE)
        self.physics_engine = Optional[arcade.PymunkPhysicsEngine]

    def setup(self):
        playerModel = PlayerModel()
        self.models.append(playerModel)

         # Map name
        map_name = "assets/scenes/levels/2.json"

        # Load in TileMap
        tile_map = arcade.load_tilemap(map_name, C.SPRITE_SCALING_TILES)
        self.tile_map_list = tile_map.sprite_lists["level_2"]

        gravity = (0, -C.GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=C.PLAYER_DAMPING,gravity=gravity)

        self.sprites = arcade.SpriteList()

        self.playerSprite = PlayerSprite(playerModel)
        self.playerSprite.scale = C.SPRITE_SCALING_PLAYER
        self.playerSprite.center_x = 400
        self.playerSprite.center_y = 500
        self.sprites.append(self.playerSprite)
        self.add_player_sprite_to_physics_engine()
        
        self.physics_engine.add_sprite_list(self.tile_map_list,
                                            friction=C.WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
        
        self.playerController = PlayerController(playerModel, self, self.playerSprite)
        self.controllers.append(self.playerController)

        self.camera_sprites = arcade.Camera(C.SCREEN_WIDTH, C.SCREEN_HEIGHT)

        self.console = Console(self, self.playerController)
        

    def on_draw(self):
        self.console.on_draw_start()

        #self.clear()
        arcade.start_render()

        self.camera_sprites.use()

        arcade.draw_lrwh_rectangle_textured(0, 0, C.SCREEN_WIDTH * C.BACKGROUND_SCALE, C.SCREEN_HEIGHT * C.BACKGROUND_SCALE, arcade.load_texture("assets/scenes/BG.png"))

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

        if self.playerSprite.center_y < 0:
            return self.game_over()

        self.scroll_to_player()

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

    def scroll_to_player(self):
        position = Vec2(max(self.playerSprite.center_x - self.width / 2, 0),
                        max(self.playerSprite.center_y - self.height / 2, 0))

        self.camera_sprites.move_to(position, C.CAMERA_SPEED)

    def add_player_sprite_to_physics_engine(self):
        self.physics_engine.add_sprite(self.playerSprite,
                                       friction=C.PLAYER_FRICTION,
                                       mass=C.PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=C.PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=C.PLAYER_MAX_VERTICAL_SPEED)

    def game_over(self):
        print("Game Over")
        self.physics_engine.remove_sprite(self.playerSprite)
        self.playerSprite.center_x = 400
        self.playerSprite.center_y = 500
        self.add_player_sprite_to_physics_engine()
        self.scroll_to_player()

    sprites = None
    controllers = []
    models = []
    