from models.GameObjectModel import GameObjectModel

import Constants as C

class PlayerModel(GameObjectModel):
    def __init__(self):
        super().__init__()
        self.speed = C.PLAYER_MOVE_FORCE


    def on_draw(self):
        super().on_draw()

    def on_update(self, dt):
        super().on_update(dt)

    def on_keypress(self, symbol, modifiers):
        super().on_keypress(symbol, modifiers)

        

    
