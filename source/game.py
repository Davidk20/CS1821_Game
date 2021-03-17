try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from main import Menu
from source.player import Player
from source.keyboard import Keyboard
from source.enemy import Enemy
from source.level import Level
from source.hud import Hud
from source.wallcollider import WallCollider
from source.collider import Collider
from source.vector import Vector
from source.clock import Clock
import source.maps as maps
from source.interaction import KeyboardInteraction

#TODO create interaction function to handle/create all interactions
#TODO organise variables such as canvas size globally across files

class Game:
    def __init__(self, frame):
        self.frame = frame
        self.player = Player([350,350])
        self.kbd = Keyboard()
        self.kbdInteraction = KeyboardInteraction(self.player, self.kbd)
        #TODO setup HUD interaction
        self.hud = Hud(self.player)
        #TODO enemies to be removed once level format restructured
        self.enemies = [Enemy(30, [210, 210], patrol_points=[Vector(210, 210), Vector(510, 210), Vector(510, 510), Vector(210, 510)])]
        #TODO move to level class?
        self.level_order = [maps.LEVEL_GRID_CENTRE, maps.LEVEL_GRID_1, maps.LEVEL_GRID_2]
        self.current_level = Level(self.level_order[0])
		#TODO move this into an interaction class
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

    def get_dimensions(self):
        return [720,720]

    def update(self):
        Clock.tick() # increment time in static clock class
        self.kbdInteraction.check_input()
        #TODO move to movement
        self.player.rotate()
        if not self.player.alive == True:
            Menu(self.frame, "died")
            return

        for i in self.colliders:
            if self.player.hit(i):
                self.player.bouncePlayer(i)

        for enemy in self.enemies:
            if self.player.hit(enemy):
                self.player.bouncePlayer(enemy)
                self.player.set_life(-1)
            
        for i in self.player.get_bullets():
            for enemy in self.enemies:
                if i.hit(enemy):
                    enemy.remove_health(i.get_damage())
            for wall in self.colliders:
                if i.hit(wall):
                    i.die()

    #Function handling drawing of all shapes on screen
    def draw(self, canvas):
        self.update()
        self.current_level.draw(canvas)
        self.player.draw(canvas)
        for enemy in self.enemies:
            enemy.draw(canvas)
        self.hud.draw(canvas)


if __name__ == "__main__":
    Game()