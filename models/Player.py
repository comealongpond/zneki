import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()
        
        img = self.spritesList["idle"][self.currentSpriteIndex]
        player_sprite = arcade.Sprite(img, 1)
        player_sprite.center_x = 900
        player_sprite.center_y = 500
        player_sprite.draw()

       # arcade.finish_render()

    def update(self, dt):
        if (self.timeSinceLastSpriteChange + dt >= self.spriteRotateDT):
            self.spriteSwap()
            self.timeSinceLastSpriteChange = 0
        else:
            self.timeSinceLastSpriteChange += dt

    def spriteSwap(self):
        if (self.currentSpriteIndex + 1 >= len(self.spritesList["idle"])-1):
            self.currentSpriteIndex = 1
        else:
            self.currentSpriteIndex += 1

    #GameWindowReference = None
    timeSinceLastSpriteChange = 0
    currentSpriteIndex = 1
    spriteRotateDT = .15
    spritesList = {
        "idle": [
            "assets/sprites/the_knight/Idle_1.png",
            "assets/sprites/the_knight/Idle_2.png",
            "assets/sprites/the_knight/Idle_3.png",
            "assets/sprites/the_knight/Idle_4.png",
            "assets/sprites/the_knight/Idle_5.png",
            "assets/sprites/the_knight/Idle_6.png",
            "assets/sprites/the_knight/Idle_7.png",
            "assets/sprites/the_knight/Idle_8.png",
            "assets/sprites/the_knight/Idle_9.png",
            "assets/sprites/the_knight/Idle_10.png"
        ]
    }