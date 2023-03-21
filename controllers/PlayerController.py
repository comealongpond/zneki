import arcade

from controllers.GameObjectController import GameObjectController


class PlayerController(GameObjectController):
    def __init__(self, playerModel, GameWindow, Sprite):
        self.modelReference = playerModel
        self.gameWindowReference = GameWindow
        self.spriteReference = Sprite

    def on_update(self, dt):
        super().on_update(dt)

        return

    def on_keypress(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.modelReference.isMovingRight = True
        if symbol == arcade.key.A:
            self.modelReference.isMovingLeft = True
        if symbol == arcade.key.SPACE and self.gameWindowReference.physics_engine.is_on_ground(self.spriteReference):
            self.modelReference.isJumping = True
            impulse = (0, 1800)
            self.gameWindowReference.physics_engine.apply_impulse(self.spriteReference, impulse)
    
    def on_keyrelease(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.modelReference.isMovingRight = False
        if symbol == arcade.key.A:
            self.modelReference.isMovingLeft = False
        return 
    
    def get_debug_info(self):
        infoStr = f"Player x:{self.spriteReference.center_x:.3f}, y:{self.spriteReference.center_y:.3f}. "
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
