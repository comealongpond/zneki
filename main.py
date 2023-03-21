import arcade

from views.GameWindow import GameWindow

def main():
    app = GameWindow()
    app.setup()
    arcade.run()

if __name__ == "__main__":
    main()

