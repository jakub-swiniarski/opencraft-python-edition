from ursina import *

class Player(Entity):
    def __init__(self,x,y,z):
        super().__init__()
        self.model='cube'
        self.collider='box'
        #invisible, for now at least 
        self.color=Color(255,255,255,0)
        self.position=(x,y,z)
        self.rotation=(0,0,0)
        self.scale=(1,2,1)

        self.movementSpeed=100

        #mouse
        self.mouseSens=40
        mouse.visible=False
        mouse.locked=True
        
        #camera
        self.camera_pivot = Entity(parent=self, y=2)
        camera.parent = self.camera_pivot
        camera.rotation = (0,0,0)
        camera.fov = 90

    def update(self):
        #update camera position
        camera.x=self.position.x
        camera.y=self.position.y+1
        camera.z=self.position.z

        #mouse input
        self.rotation_y += mouse.velocity[0] * self.mouseSens
        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouseSens
        self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)

    def input(self,key):
        if key=='escape':
            quit()