from controllers.Controller import Controller
from models.Player import Player

class PlayerController(Controller):
    def __init__(self):
        print("Hel")

    def on_keypress(self, symbol, modifiers):
        print("PlayerController.on_keypress")
