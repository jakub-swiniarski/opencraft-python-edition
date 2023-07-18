from ursina import *
from Dirt import Dirt
from Player import Player

def main():
    app = Ursina()

    window.title="Minecraft Python Edition"
    window.borderless = False
    window.fullscreen = False
    window.exit_button.visible = False
    #window.fps_counter.enabled = False

    player=Player()

    dirt=Dirt()

    app.run()

if __name__ == "__main__":
    main()