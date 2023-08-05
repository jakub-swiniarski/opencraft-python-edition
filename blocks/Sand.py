from blocks.Block import Block
from ursina import raycast

class Sand(Block):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.texture='assets/blocks/sand.png'

    def update(self):
        pass
        #add gravity
