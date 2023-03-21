from models.GameObjectModel import GameObjectModel

class PlayerModel(GameObjectModel):
    def __init__(self):
        super().__init__()
        
        self.position["x"] = 300
        self.position["y"] = 300

        self.acceleration = 1000
        self.deceleration = -1000
        self.speed = 8000

        self.isAffectedGravity = True


    def on_draw(self):
        super().on_draw()

    def on_update(self, dt):
        super().on_update(dt)

    def on_keypress(self, symbol, modifiers):
        super().on_keypress(symbol, modifiers)

    isJumping = False
        

    
