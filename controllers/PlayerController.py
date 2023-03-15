import arcade

from controllers.GameObjectController import GameObjectController


class PlayerController(GameObjectController):
    def __init__(self, playerModel):
        self.modelReference = playerModel

    def on_update(self, dt):
        super().on_update(dt)
        if self.modelReference.position["y"] <= 300 and self.modelReference.isJumping:
            self.modelReference.isJumping = False

        if abs(self.modelReference.velocity["y"]) > 0:
            self.modelReference.moveState = "jump"
        elif self.modelReference.velocity["x"] == 0:
            self.modelReference.moveState = "idle"
        elif abs(self.modelReference.velocity["x"]) < (self.modelReference.speed / 2):
            self.modelReference.moveState = "walk"
        elif abs(self.modelReference.velocity["x"]) >= (self.modelReference.speed / 2):
            self.modelReference.moveState = "run"

        return

    def on_keypress(self, symbol, modifiers):
        if symbol == 100:
            self.modelReference.isMovingRight = True
        if symbol == 97:
            self.modelReference.isMovingLeft = True
        if symbol == 32 and not self.modelReference.isJumping:
            self.modelReference.velocity["y"] = 500
            self.modelReference.isJumping = True
    
    def on_keyrelease(self, symbol, modifiers):
        if symbol == 100:
            self.modelReference.isMovingRight = False
        if symbol == 97:
            self.modelReference.isMovingLeft = False
        return 
    
    def get_debug_info(self):
        infoStr = f"Player x:{self.modelReference.position['x']:.3f}, y:{self.modelReference.position['y']:.3f}, vx:{self.modelReference.velocity['x']:.3f} , vy:{self.modelReference.velocity['y']:.3f}. "
        if self.modelReference.isMovingLeft:
            infoStr += "isMovingLeft, "
        if self.modelReference.isMovingRight:
            infoStr += "isMovingRight, "
        if self.modelReference.isMovingUp:
            infoStr += "isMovingUp, "
        if self.modelReference.isMovingDown:
            infoStr += "isMovingDown, "  
        if self.modelReference.isJumping:
            infoStr += "isJumping, "

        return infoStr
