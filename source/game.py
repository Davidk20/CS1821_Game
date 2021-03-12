try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from keyboard import Keyboard
from enemy import Enemy
from level import Level
from hud import Hud
from wallcollider import WallCollider
from collider import Collider
from vector import Vector
import maps

class Game:
    def __init__(self):
        self.player = Player([350,350])
        self.hud = Hud(self.player)
        self.enemies = [Enemy(30, 1, [210, 210], patrol_points=[Vector(210, 210), Vector(510, 210), Vector(510, 510), Vector(210, 510)])]
        self.level_order = [maps.LEVEL_GRID_CENTRE, maps.LEVEL_GRID_1, maps.LEVEL_GRID_2]
        self.current_level = Level(self.level_order[0])
        self.kbd = Keyboard()
		#this list currently stores any colliders in the game that the player will collide with
        self.colliders = self.current_level.listWalls()
        #self.interaction = Interaction(self.player, self.kbd, [WallCollider(Vector(0,0), "v")])
        self.game_window_setup()
        


    #Setup of SimpleGUI window
    def game_window_setup(self):
        frame = simplegui.create_frame("Game", 720 , 720, 0)
        frame.set_canvas_background("#534a32")
        frame.set_keydown_handler(self.kbd.keyDown)
        frame.set_keyup_handler(self.kbd.keyUp)
        frame.set_draw_handler(self.draw)
        frame.start()

    #Function handling drawing of all shapes on screen
    def draw(self, canvas):
        self.current_level.draw(canvas)
        for i in self.colliders:
            if self.player.hit(i):
                self.player.bounceZeroMass(i)
        self.player.draw(canvas)

        for enemy in self.enemies:
            if self.player.hit(enemy):
                self.player.bounceZeroMass(i)
                self.player.remove_life(1)

            enemy.draw(canvas)
            
        for i in self.player.return_bullets():
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


# Class to link player to keyboard for interactions with other shapes (removed because it was not needed)
# class Interaction:
    # def __init__(self, player, keyboard, colliders):
        # self.player = player
        # self.keyboard = keyboard
        # self.colliders = colliders
    
    # def update(self):
        # self.player.check_input(self.keyboard)
        # self.player.rotate() # Rotates the player every frame.

if __name__ == "__main__":
    Game()