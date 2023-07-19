from ursina import *

class Block(Entity):
    def __init__(self,x,y,z):
        super().__init__()
        self.model='cube'
        self.collider='box'
        self.texture='assets/blocks/missing.png'
        self.position=(x,y,z)
        self.rotation=(0,0,0)
        self.scale=(1,1,1)