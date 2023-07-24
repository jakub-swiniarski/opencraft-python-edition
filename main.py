from ursina import *
from blocks.Dirt import Dirt
from entities.Player import Player
from blocks.Stone import Stone
from blocks.Wood import Wood

app = Ursina()

window.title="OpenCraft Python Edition"
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
#window.fps_counter.enabled = False

player=Player()

Sky(color=rgb(200,255,255))

dirt=[]
stone=[]
wood=[]

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
                    newDirt=Dirt(position.x, position.y, position.z)
                    dirt.append(newDirt)

                if player.currentBlock=='2':
                    newStone=Stone(position.x, position.y, position.z)
                    stone.append(newStone)

                if player.currentBlock=='3':
                    newWood=Wood(position.x, position.y, position.z)
                    wood.append(newWood)

for i in range(21):
    for j in range(21):
        newDirt=Dirt(i-10,0,j-10)
        dirt.append(newDirt)

DirectionalLight(parent=Entity(), y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()