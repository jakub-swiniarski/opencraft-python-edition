from ursina import *

#entities
from entities.Player import Player

#blocks
from blocks.Dirt import Dirt
from blocks.Stone import Stone
from blocks.Wood import Wood
from blocks.Bricks import Bricks
from blocks.Gold import Gold
from blocks.Glass import Glass

app = Ursina()

window.title="OpenCraft Python Edition"
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
#window.fps_counter.enabled = False

player=Player()

Sky(color=rgb(200,255,255))

blocks=[]   

def input(key):
        #MOUSE INPUT
        if key == 'left mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                destroy(mouse.hovered_entity)

        if key == 'right mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                position=hit_info.entity.position + hit_info.normal
                if player.currentBlock=='1':
                    newBlock=Dirt(position.x, position.y, position.z)

                elif player.currentBlock=='2':
                    newBlock=Stone(position.x, position.y, position.z)

                elif player.currentBlock=='3':
                    newBlock=Wood(position.x, position.y, position.z)

                elif player.currentBlock=='4':
                    newBlock=Bricks(position.x, position.y, position.z)

                elif player.currentBlock=='5':
                    newBlock=Gold(position.x, position.y, position.z)

                elif player.currentBlock=='6':
                    newBlock=Glass(position.x, position.y, position.z)

                blocks.append(newBlock)
                #before adding new blocks, add new numbers in player input (choosing a block)

for i in range(21):
    for j in range(21):
        newBlock=Dirt(i-10,0,j-10)
        blocks.append(newBlock)

DirectionalLight(parent=Entity(), y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()