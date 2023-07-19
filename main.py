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

    player=Player()

    dirt=[]
    for i in range(21):
        for j in range(21):
            newDirt=Dirt(i-10,0,j-10)
            dirt.append(newDirt)

    #for mouse sensitivity testing
    #newDirt=Dirt(6,1,0)
    #dirt.append(newDirt)
    #newDirt=Dirt(6,2,0)
    #dirt.append(newDirt)
    #USE STONE

    app.run()

if __name__ == "__main__":
    main()