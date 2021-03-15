try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from source.player import Player
from source.keyboard import Keyboard
from source.enemy import Enemy
from source.level import Level
from source.hud import Hud
from source.wallcollider import WallCollider
from source.collider import Collider
from source.vector import Vector
import source.maps as maps

class Interaction:
    def __init__(self):
        pass