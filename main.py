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

#-------------------------------------

app = Ursina()

window.title="OpenCraft Python Edition"
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False
window.cog_button.visible = False

player=Player()

Sky(color=rgb(200,255,255))

def input(key):
        #MOUSE INPUT
        if key == 'left mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                Audio('assets/sfx/hitHurt.wav', range = 1, parent = "Player").volume = player.volume
                destroy(mouse.hovered_entity)

        if key == 'right mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                position=hit_info.entity.position + hit_info.normal
                if player.currentBlock=='1':
                    Audio('assets/sfx/laserShoot.wav', range = 1, parent = "Player").volume = player.volume
                    Dirt(position.x, position.y, position.z)

                elif player.currentBlock=='2':
                    Audio('assets/sfx/laserShoot.wav', range = 1, parent = "Player").volume = player.volume
                    Stone(position.x, position.y, position.z)

                elif player.currentBlock=='3':
                    Audio('assets/sfx/laserShoot.wav', range = 1, parent = "Player").volume = player.volume
                    Wood(position.x, position.y, position.z)

                elif player.currentBlock=='4':
                    Audio('assets/sfx/laserShoot.wav', range = 1, parent = "Player").volume = player.volume
                    Bricks(position.x, position.y, position.z)

                elif player.currentBlock=='5':
                    Audio('assets/sfx/laserShoot.wav', range = 1, parent = "Player").volume = player.volume
                    Gold(position.x, position.y, position.z)

                elif player.currentBlock=='6':
                    Audio('assets/sfx/laserShoot.wav', range = 1, parent = "Player").volume = player.volume
                    Glass(position.x, position.y, position.z)

                #before adding new blocks, add new numbers in player input (choosing a block)
                #add a menu for choosing blocks

for i in range(21):
    for j in range(21):
        Dirt(i-10,0,j-10)

DirectionalLight(parent=Entity(), y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()

#----------TODO----------
#render distance, change with cmd
#quality0 - switch to gold_old and disable matcap shader
#do not render blocks that are not visible
#level of detail
#stop player from moving when cmd is open
#------------------------