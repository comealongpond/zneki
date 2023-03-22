from views.sprites.Sprite import Sprite

class PlayerSprite(Sprite):

    def __init__(self, playerModel):
        self.initSpritesList()
        super().__init__(playerModel)
        self.spriteRotateDT = .1

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
        self.spritesList["run"] = [
            "assets/sprites/the_knight/Run_1.png",
            "assets/sprites/the_knight/Run_2.png",
            "assets/sprites/the_knight/Run_3.png",
            "assets/sprites/the_knight/Run_4.png",
            "assets/sprites/the_knight/Run_5.png",
            "assets/sprites/the_knight/Run_6.png",
            "assets/sprites/the_knight/Run_7.png",
            "assets/sprites/the_knight/Run_8.png",
            "assets/sprites/the_knight/Run_9.png",
            "assets/sprites/the_knight/Run_10.png"
        ]
        self.spritesList["jump"] = [
            "assets/sprites/the_knight/Jump_1.png",
            "assets/sprites/the_knight/Jump_2.png",
            "assets/sprites/the_knight/Jump_3.png",
            "assets/sprites/the_knight/Jump_4.png",
            "assets/sprites/the_knight/Jump_5.png",
            "assets/sprites/the_knight/Jump_6.png",
            "assets/sprites/the_knight/Jump_7.png",
            "assets/sprites/the_knight/Jump_8.png",
            "assets/sprites/the_knight/Jump_9.png",
            "assets/sprites/the_knight/Jump_10.png"
        ]
        