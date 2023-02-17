import arcade

from controllers.Controller import Controller


class PlayerController(Controller):
    def __init__(self, playerModel):
        self.modelReference =  playerModel

    def on_update(self, dt):
        if self.isMovingRight:
            self.modelReference.position["x"] += 10
        if self.isMovingLeft:
            self.modelReference.position["x"] -= 10
        if self.isMovingDown:
            self.modelReference.position["y"] -= 10
        if self.isMovingUp:
            self.modelReference.position["y"] += 10

    def on_keypress(self, symbol, modifiers):
        if symbol == 100:
            self.isMovingRight = True
        if symbol == 97:
            self.isMovingLeft = True
        if symbol == 115:
            self.isMovingDown = True
        if symbol == 119:
            self.isMovingUp = True
    
    def on_keyrelease(self, symbol, modifiers):
        if symbol == 100:
            self.isMovingRight = False
        if symbol == 97:
            self.isMovingLeft = False
        if symbol == 115:
            self.isMovingDown = False
        if symbol == 119:
            self.isMovingUp = False

    isMovingRight = False
    isMovingLeft = False
    isMovingUp = False
    isMovingDown = False
