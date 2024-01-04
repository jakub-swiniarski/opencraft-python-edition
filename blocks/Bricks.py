from blocks.Block import Block

class Bricks(Block):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.texture='assets/img/blocks/bricks.png'
