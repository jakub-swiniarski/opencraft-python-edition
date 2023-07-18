from ursina import *

class Block(Entity):
    def __init__(self):
        super().__init__()
        self.model='cube'
        self.texture='assets/missing.png'
        self.position=(0,0,0)
        self.rotation=(0,0,0)
        self.scale=(1,1,1)