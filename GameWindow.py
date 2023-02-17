import arcade

from models.Player import Player
from controllers.PlayerController import PlayerController


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)

        self.sprites = arcade.SpriteList()
        self.sprites.append(Player())

        self.controllers.append(PlayerController())

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        for sprite in self.sprites:
            sprite.on_draw()

    def update(self, dt):
        for sprite in self.sprites:
            sprite.on_update(dt)
        for controller in self.controllers:
            controller.on_update(dt)

    def on_key_press(self, symbol, modifiers):
        for sprite in self.sprites:
            sprite.on_keypress(symbol, modifiers)
        for controller in self.controllers:
            controller.on_keypress(symbol, modifiers)

    sprites = None
    controllers = []
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    SCREEN_TITLE = "Zneki"