import arcade

from models.PlayerModel import PlayerModel
from controllers.PlayerController import PlayerController
from views.sprites.PlayerSprite import PlayerSprite


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)

        playerModel = PlayerModel()
        self.models.append(playerModel)

        self.controllers.append(PlayerController(playerModel))

        self.sprites = arcade.SpriteList()
        self.sprites.append(PlayerSprite(playerModel))

        

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        for sprite in self.sprites:
            sprite.on_draw()

    def update(self, dt):
        for controller in self.controllers:
            controller.on_update(dt)
        for sprite in self.sprites:
            sprite.on_update(dt)

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