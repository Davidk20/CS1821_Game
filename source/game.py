try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from menu import Menu
from source.player import Player
from source.keyboard import Keyboard
from source.enemy import Enemy
from source.level import Level
from source.hud import Hud
from source.wallcollider import WallCollider
from source.collider import Collider
from source.vector import Vector
import source.maps as maps

#TODO create interaction function to handle/create all interactions
#TODO organise variables such as canvas size globally across files

class Game:
    def __init__(self, frame):
        self.frame = frame
        self.player = Player([350,350])
        self.hud = Hud(self.player)
        #enemies to be removed once level format restructured
        self.enemies = [Enemy(30, [210, 210], patrol_points=[Vector(210, 210), Vector(510, 210), Vector(510, 510), Vector(210, 510)])]
        self.level_order = [maps.LEVEL_GRID_CENTRE, maps.LEVEL_GRID_1, maps.LEVEL_GRID_2]
        self.current_level = Level(self.level_order[0])
        #kbd moved to interaction class
        self.kbd = Keyboard()
		#this list currently stores any colliders in the game that the player will collide with
        self.colliders = self.current_level.listWalls()
        self.game_window_setup()
        
    #Setup of SimpleGUI window
    def game_window_setup(self):
        self.frame.set_canvas_background("#534a32")
        self.frame.set_keydown_handler(self.kbd.keyDown)
        self.frame.set_keyup_handler(self.kbd.keyUp)
        self.frame.set_draw_handler(self.draw)
        self.frame.start()

    #Function handling drawing of all shapes on screen
    #Needs to be moved into interaction
    def draw(self, canvas):
        if not self.player.alive == True:
            Menu(self.frame, "died")
            return

        self.current_level.draw(canvas)
        for i in self.colliders:
            if self.player.hit(i):
                self.player.bounceZeroMass(i)
        self.player.draw(canvas)

        for enemy in self.enemies:
            if self.player.hit(enemy):
                self.player.bounceZeroMass(i)
                self.player.set_life(-1)

            enemy.draw(canvas)
            
        for i in self.player.get_bullets():
            for enemy in self.enemies:
                if i.hit(enemy):
                    enemy.remove_health(i.get_damage())
            for wall in self.colliders:
                if i.hit(wall):
                    print("hit")

        #self.interaction.update() #this is not necessary, just use lines below instead
        self.player.check_input(self.kbd)
        self.player.rotate()
        self.hud.draw(canvas)


if __name__ == "__main__":
    Game()