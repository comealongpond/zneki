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
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        super().__init__(self.screen_width, self.screen_height, C.SCREEN_TITLE)
        self.physics_engine = Optional[arcade.PymunkPhysicsEngine]

    def setup(self):
        playerModel = PlayerModel()
        self.models.append(playerModel)

         # Map name
        map_name = "assets/scenes/levels/3.json"


        gravity = (0, -C.GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=C.PLAYER_DAMPING,gravity=gravity)
        
        self.sprites = arcade.SpriteList()

        self.playerSprite = PlayerSprite(playerModel)
        self.playerSprite.scale = C.SPRITE_SCALING_PLAYER
        self.playerSprite.center_x = 400
        self.playerSprite.center_y = 250
        self.sprites.append(self.playerSprite)
        self.add_player_sprite_to_physics_engine()
        
        tile_map = arcade.load_tilemap(map_name, C.SPRITE_SCALING_TILES)
        self.tile_map_list = tile_map.sprite_lists["level_3_tiles"]
        self.physics_engine.add_sprite_list(self.tile_map_list,
                                            friction=C.WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

        object_map = arcade.load_tilemap(map_name, C.SPRITE_SCALING_TILES)
        self.object_map_list = object_map.sprite_lists["level_3_objects"]
        self.physics_engine.add_sprite_list(self.object_map_list,
                                            friction=C.WALL_FRICTION,
                                            collision_type="object",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
        
        self.physics_engine.add_collision_handler("player", "object", self.dead)
        
        self.playerController = PlayerController(playerModel, self, self.playerSprite)
        self.controllers.append(self.playerController)

        self.camera_sprites = arcade.Camera(self.screen_width, self.screen_height)

        self.console = Console(self, self.playerController)
        

    def on_draw(self):
        self.console.on_draw_start()

        #self.clear()
        arcade.start_render()
        
        self.camera_sprites.use()

        arcade.draw_lrwh_rectangle_textured(0, 0, self.screen_width * C.BACKGROUND_SCALE, self.screen_height * C.BACKGROUND_SCALE, arcade.load_texture("assets/scenes/BG.png"))

        self.tile_map_list.draw()
        self.object_map_list.draw()
        self.object_map_list.draw_hit_boxes()

        self.sprites.draw()
        self.sprites.draw_hit_boxes()

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
        self.playerSprite.center_y = 250
        self.add_player_sprite_to_physics_engine()
        self.scroll_to_player()

    def dead(self, sprite_a, sprite_b, arbiter, space, data):
        self.game_over()
        return False

    sprites = None
    controllers = []
    models = []
    