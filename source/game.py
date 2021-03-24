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
from source.collider import Collider, WallCollider
from source.vector import Vector
from source.clock import Clock
from source.pickup import HealthPickup, BonusPickup
import source.maps as maps
from source.interaction import KeyboardInteraction, MapInteraction


#TODO create a flush() method to clean dead sprites at the end

class Game:
    def __init__(self, frame):
        self.frame = frame
        self.player = Player([350,350])
        self.kbd = Keyboard()
        self.kbdInteraction = KeyboardInteraction(self.player, self.kbd)
        self.map = MapInteraction(self.frame, self.player)
        self.enemies = self.map.current_level.get_enemies()
        self.hud = Hud(self.player)
        #this list currently stores any colliders in the game that the player will collide with
        self.colliders = self.map.current_level.listWalls()
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
        self.colliders = self.map.current_level.listWalls()
        self.enemies = self.map.current_level.get_enemies()
        Clock.tick() # increment time in static clock class
        self.kbdInteraction.check_input()
        if not self.player.alive == True:
            Menu(self.frame, "died", self.player.get_score())
            return

        for i in self.colliders:
            if self.player.hit(i):
                self.player.bounceSprite(i)

        for enemy in self.enemies:
            discard = []
            for collider in self.colliders:
                if enemy.hit(collider):
                    enemy.bounceSprite(collider)
            if self.player.hit(enemy):
                self.player.bounceSprite(enemy)
                self.player.set_life(-1)
            if enemy.alive == False:
                discard.append(enemy)
                self.player.set_score(enemy.get_score())

            for colliding_enemy in self.enemies:
                if (enemy != colliding_enemy):
                    if (colliding_enemy.hit(enemy)):
                        colliding_enemy.bounceSprite(enemy)
            for i in discard:
                self.enemies.remove(i)
            
        for i in self.player.get_bullets():
            for enemy in self.enemies:
                if i.hit(enemy):
                    enemy.set_health(- i.get_damage())
            for wall in self.colliders:
                if i.hit(wall):
                    i.die()

        for pickup in self.map.current_level.pickup_array:
            if pickup.hit(self.player):
                if type(pickup) is HealthPickup:
                    self.player.set_life(pickup.value)
                elif type(pickup) is BonusPickup:
                    self.player.set_score(pickup.value)
                self.map.pickup(pickup)

    #Function handling drawing of all shapes on screen
    def draw(self, canvas):
        self.update()
        self.map.draw(canvas)
        self.player.draw(canvas)
        for enemy in self.enemies:
            if enemy.alive == True:
                enemy.draw(canvas)
        self.hud.draw(canvas)


if __name__ == "__main__":
    Game()