import arcade

class Sprite(arcade.Sprite):
    def __init__(self):
        super(Sprite, self).__init__()

    def on_draw(self):
        arcade.start_render()
        
        img = self.spritesList[self.moveState][self.currentSpriteIndex]
        draw_sprite = arcade.Sprite(img, 1)
        draw_sprite.center_x = self.position["x"]
        draw_sprite.center_y = self.position["y"]
        draw_sprite.draw()

       # arcade.finish_render()

    def on_update(self, dt):
        if (self.timeSinceLastSpriteChange + dt >= self.spriteRotateDT):
            self.spriteSwap()
            self.timeSinceLastSpriteChange = 0
        else:
            self.timeSinceLastSpriteChange += dt

    def spriteSwap(self):
        if (self.currentSpriteIndex + 1 >= len(self.spritesList[self.moveState])-1):
            self.currentSpriteIndex = 1
        else:
            self.currentSpriteIndex += 1

    #GameWindowReference = None
    position = {
        "x": 0,
        "y": 0
    }
    timeSinceLastSpriteChange = 0
    currentSpriteIndex = 1
    moveState = "idle"
    spriteRotateDT = .15
    spritesList = {
        "idle": [],
        "walk": []
    }