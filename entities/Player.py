from ursina import *

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model='cube'
        self.collider='box'
        #invisible, for now at least 
        self.color=Color(255,255,255,0)
        self.position=(0,1,-10)
        self.rotation=(0,0,0)
        self.scale=(1,2,1)

        self.movementSpeed=100

    def update(self):
        camera.x=self.position.x
        camera.y=self.position.y+1
        camera.z=self.position.z

    def input(self,key):
        pass