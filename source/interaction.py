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
import random as rand


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

class MapInteraction:
    def __init__(self, frame, player):
        #TODO put level order/array in here
        self.frame = frame
        self.player = player
        self.level_array = [
            [maps.LEVEL_GRID_6, maps.LEVEL_GRID_2, maps.LEVEL_GRID_3],
            [maps.LEVEL_GRID_1, maps.LEVEL_GRID_CENTRE, maps.LEVEL_GRID_4],
            [maps.LEVEL_GRID_5, maps.LEVEL_GRID_6, maps.LEVEL_GRID_1]
        ]
        #TODO assign patrol points to each map
        self.map_patrol_points = {
            "00" : [],
            "01" : [],
            "02" : [],
            "10" : [],
            "11" : [Vector(210, 210), Vector(510, 210), Vector(510, 510), Vector(210, 510)],
            "12" : [],
            "20" : [],
            "21" : [],
            "22" : []
        }
        self.current_level = Level(self.level_array[1][1])
        self.level_setup()

    def level_setup(self):
        self.enemies = self.current_level.get_enemies()
        for enemy in self.enemies:
            if rand.randint(0,1) == 0:
                for i in self.level_array:
                    for j in i:
                        if j == self.current_level.get_level():
                            enemy.set_patrol_points(self.map_patrol_points[str(self.level_array.index(i))+str(i.index(j))])
            else:
                enemy.set_patrol_points([self.player.movement.get_pos()])
                enemy.set_target()

    def draw(self, canvas):
        self.current_level.draw(canvas)
        for enemy in self.enemies:
            enemy.draw(canvas)
