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
from source.collider import Collider
from source.vector import Vector
import source.maps as maps
import random as rand


class Interaction:
    '''
    Base Interaction Class
    '''
    def __init__(self, player):
        self.player = player


class KeyboardInteraction(Interaction):
    '''
    Class inherits from Interaction but is specialised for Keyboard object.
    Links keyboard inputs to player movement
    '''
    def __init__(self, player, keyboard):
        Interaction.__init__(self, player)
        self.keyboard = keyboard

    #function to check and control player movement
    def check_input(self):
        '''
        Method checks booleans from keyboard and triggers movement
        based on keypress
        '''
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
                self.player.movement.rotation,
                4,
                "blue"
                )
            self.player.bullets.append(fire)


class MapInteraction(Interaction):
    '''
    Class inherits from Interaction but is specialised for Map class
    '''
    def __init__(self, frame, player):
        Interaction.__init__(self, player)
        self.frame = frame
        self.level_array = [
            [maps.LEVEL_GRID_1, maps.LEVEL_GRID_2, maps.LEVEL_GRID_3],
            [maps.LEVEL_GRID_4, maps.LEVEL_GRID_CENTRE, maps.LEVEL_GRID_5],
            [maps.LEVEL_GRID_6, maps.LEVEL_GRID_7, maps.LEVEL_GRID_8]
        ]
        self.map_x = 1
        self.map_y = 1
        self.map_patrol_points = {
            "00" : [Vector(100, 350), Vector(300, 450), Vector(420, 250), Vector(610, 410), Vector(620, 270)],
            "01" : [Vector(310, 310), Vector(410, 310), Vector(410, 410), Vector(310, 410)],
            "02" : [Vector(110, 110), Vector(350, 110), Vector(350, 350), Vector(110, 350), Vector(110, 610), Vector(610, 610), Vector(610, 350), Vector(110,350)],
            "10" : [Vector(100, 100), Vector(620, 100), Vector(620, 620), Vector(100, 620), Vector(100, 350), Vector(620, 350), Vector(620, 100)],
            "11" : [Vector(210, 210), Vector(510, 210), Vector(510, 510), Vector(210, 510)],
            "12" : [Vector(100, 100), Vector(300, 350), Vector(600, 270), Vector(600, 450), Vector(100, 450), Vector(350, 350)],
            "20" : [Vector(350, 350), Vector(110, 350), Vector(350, 350), Vector(350, 610), Vector(350, 350), Vector(610, 350), Vector(350, 350), Vector(350, 110)],
            "21" : [Vector(110, 610), Vector(270, 350), Vector(110, 110), Vector(350, 200), Vector(610, 110), Vector(450, 350), Vector(610, 610), Vector(350, 110)],
            "22" : [Vector(350, 350), Vector(110, 110), Vector(350, 350), Vector(610, 110), Vector(350, 350), Vector(110, 610)]
        }
        self.current_level = Level(self.level_array[self.map_x][self.map_y])
        self.level_setup()

    def level_setup(self):
        '''
        Method configures objects and variables for current level.
        Configures enemy movement
        '''
        self.current_level = Level(self.level_array[self.map_x][self.map_y])
        self.enemies = self.current_level.get_enemies()
        for enemy in self.enemies:
            if rand.randint(0,1) == 0:
                for i in self.level_array:
                    for j in i:
                        if j == self.current_level.get_level():
                            enemy.set_patrol_points(self.map_patrol_points[str(self.level_array.index(i))+str(i.index(j))])
                            enemy.movement.speed = 3
            else:
                enemy.set_patrol_points([self.player.movement.get_pos()])
                enemy.set_target()


    def update(self):
        """
        The update function determines when the player has crossed one of the thresholds
        and then accrodingly changes level and player location
        """
        if self.player.pos.get_p()[0] < 0 and self.map_y > 0:
                self.map_y -= 1
                self.player.pos.add(Vector(715,0))
                self.level_setup()
                
        if self.player.pos.get_p()[1] < 0 and self.map_x > 0:
                self.map_x -= 1
                self.player.pos.add(Vector(0,715))
                self.level_setup()

        if self.player.pos.get_p()[0] > 720 and self.map_y < 2:
                self.map_y += 1
                self.player.pos.add(Vector(-715,0))
                self.level_setup()
                
        if self.player.pos.get_p()[1] > 720 and self.map_x < 2:
                self.map_x += 1
                self.player.pos.add(Vector(0,-715))
                self.level_setup()
                
    def draw(self, canvas):
        '''
        Method draws all wall, enemy and pickup objects onto canvas
        '''
        self.update()
        
        self.current_level.draw(canvas)

        for enemy in self.enemies:
            enemy.draw(canvas)
        for pickup in self.current_level.pickup_array:
            pickup.draw(canvas)

    def pickup(self, pickup):
        '''
        method removes pickup from list once it has been picked up.
        Removing it from draw queue and game.
        '''
        self.current_level.pickup_array.remove(pickup)
