from ursina import *
from Dirt import Dirt

app = Ursina()

window.title="Minecraft Python Edition"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
#window.fps_counter.enabled = False

dirt=Dirt()

app.run()