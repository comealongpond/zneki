import arcade

from models.PlayerModel import PlayerModel
from controllers.PlayerController import PlayerController
from views.sprites.PlayerSprite import PlayerSprite
from views.Console import Console


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)

        playerModel = PlayerModel()
        self.models.append(playerModel)

        playerController = PlayerController(playerModel)
        self.controllers.append(playerController)

        self.sprites = arcade.SpriteList()
        self.sprites.append(PlayerSprite(playerModel))

        self.console = Console(self, playerController)
        
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.console.on_draw_start()

        arcade.start_render()

        for sprite in self.sprites:
            sprite.on_draw()

        self.console.on_draw_end()

    def update(self, dt):
        self.console.on_update_start()

        for controller in self.controllers:
            controller.on_update(dt)
        for sprite in self.sprites:
            sprite.on_update(dt)

        self.console.on_update_end()

    def on_key_press(self, symbol, modifiers):
        for controller in self.controllers:
            controller.on_keypress(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for controller in self.controllers:
            controller.on_keyrelease(symbol, modifiers)

    sprites = None
    controllers = []
    models = []
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    SCREEN_TITLE = "Zneki"