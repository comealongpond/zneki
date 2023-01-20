import arcade
import time
from models.Player import Player

# Set constants for the screen size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Zneki"


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.sprites = arcade.SpriteList()
        
        self.sprites.append(Player())

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        
        self.sprites.draw()

       # arcade.finish_render()

    def update(self, dt):
        return

    sprites = None


if __name__ == "__main__":
    app = Game()
    arcade.run()
