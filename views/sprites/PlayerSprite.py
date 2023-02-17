from views.sprites.Sprite import Sprite

class PlayerSprite(Sprite):

    def __init__(self, playerModel):
        super().__init__(playerModel)
        self.initSpritesList()

    def initSpritesList(self):
        self.spritesList["idle"] = [
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
        self.spritesList["walk"] = [
            "assets/sprites/the_knight/Walk_1.png",
            "assets/sprites/the_knight/Walk_2.png",
            "assets/sprites/the_knight/Walk_3.png",
            "assets/sprites/the_knight/Walk_4.png",
            "assets/sprites/the_knight/Walk_5.png",
            "assets/sprites/the_knight/Walk_6.png",
            "assets/sprites/the_knight/Walk_7.png",
            "assets/sprites/the_knight/Walk_8.png",
            "assets/sprites/the_knight/Walk_9.png",
            "assets/sprites/the_knight/Walk_10.png"
        ]
        