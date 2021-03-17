try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
from source.player import Player
from source.keyboard import Keyboard
from source.enemy import Enemy
from source.level import Level
from source.hud import Hud
from source.projectile import Projectile
from source.wallcollider import WallCollider
from source.collider import Collider
from source.vector import Vector
import source.maps as maps

class Interaction:
    def __init__(self, player):
        self.player = player

class PlayerInteraction(Interaction):
    def __init__(self, player):
        Interaction.__init__(self, player)


class KeyboardInteraction(Interaction):
    def __init__(self, player, keyboard):
        Interaction.__init__(self, player)
        self.keyboard = keyboard

    #function to check and control player movement
    def check_input(self):
        if self.keyboard.left == True:
            self.player.movement.move_horizontal(-1) #move left
        if self.keyboard.right == True:
            self.player.movement.move_horizontal(1) #move right
        if self.keyboard.up == True:
            self.player.movement.move_vertical(1) #move up
        if self.keyboard.down == True:
            self.player.movement.move_vertical(-1) #move down
        if self.keyboard.space == True and self.player.can_shoot:
            self.player.can_shoot = False
            fire = Projectile(
                self.player.pos.get_p(),
                self.player.rotation,
                4,
                "blue"
                )
            self.player.bullets.append(fire)

class HudInteraction(Interaction):
    def __init__(self, player, hud):
        Interaction.__init__(self, player)
        self.hud = hud

class MapInteraction():
    def __init__(self, frame, init_level):
        #TODO put level order/array in here
        self.frame = frame
        self.current_level = init_level




'''
hud interaction
player interaction
keyboard interaction
map interaction
'''