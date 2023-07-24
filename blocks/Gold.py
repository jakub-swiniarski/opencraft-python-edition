from blocks.Block import Block
from ursina.shaders import *

class Gold(Block):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.texture='assets/blocks/gold.png'

        self.shader=matcap_shader