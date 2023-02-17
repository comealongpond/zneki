from models.Model import Model

class PlayerModel(Model):
    def __init__(self):
        super(PlayerModel, self).__init__()
        
        self.position["x"] = 600
        self.position["y"] = 500

    def on_draw(self):
        super().on_draw()

    def on_update(self, dt):
        super().on_update(dt)

    def on_keypress(self, symbol, modifiers):
        super().on_keypress(symbol, modifiers)
        

    
