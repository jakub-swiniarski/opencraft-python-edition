from ursina import *
from blocks.Dirt import Dirt
from entities.Player import Player
from blocks.Stone import Stone

def main():
    app = Ursina()

    window.title="OpenCraft Python Edition"
    window.borderless = False
    window.fullscreen = True
    window.exit_button.visible = False
    #window.fps_counter.enabled = False

    player=Player()

    Sky(color=rgb(255,255,255))

    dirt=[]
    stone=[]

    for i in range(21):
        for j in range(21):
            newDirt=Dirt(i-10,0,j-10)
            dirt.append(newDirt)

    #for mouse sensitivity testing
    #test on the main monitor, jump before testing, wait for fps to stabilize
    newStone=Stone(10,1,0)
    stone.append(newStone)
    newStone=Stone(10,2,0)
    stone.append(newStone)

    app.run()

if __name__ == "__main__":
    main()