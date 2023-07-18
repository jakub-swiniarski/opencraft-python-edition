from blocks.Block import Block

class Dirt(Block):
    def __init__(self):
        super().__init__()
        self.texture='assets/blocks/dirt.png'