from ursina import *
from blocks.Dirt import Dirt
from entities.Player import Player

def main():
    app = Ursina()

    window.title="OpenCraft"
    window.borderless = False
    window.fullscreen = False
    window.exit_button.visible = False
    #window.fps_counter.enabled = False

    mouse.visible=False
    mouse.locked=True

    camera.fov=90

    player=Player(0,1,0)

    dirt=[]
    for i in range(21):
        for j in range(21):
            newDirt=Dirt(i-10,0,j-10)
            dirt.append(newDirt)

    app.run()

if __name__ == "__main__":
    main()