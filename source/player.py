try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.clock import Clock
from source.vector import Vector
from source.movement import Movement
from source.projectile import Projectile
from source.collider import PlayerCollider
from source.stats import PlayerStats
from source.spritesheet import Spritesheet
import os, math

class Player(PlayerCollider, PlayerStats):
    def __init__(self, init_pos, speedMul = 2):
        PlayerStats.__init__(self, speedMul)
        self.pos = Vector(init_pos[0],init_pos[1])
        self.movement = Movement(self.speed, self.pos)
        PlayerCollider.__init__(self, Vector(init_pos[0],init_pos[1]), self.movement)
        self.sprite = Spritesheet("source/images/player.png", 1, 1)
        #TODO move to movement
        self.rotation = 0


    #TODO move into movement class
    def rotate(self):
        """
        Rotates the player based off their velocity vector.
        """
        vel_vector = self.movement.vel_vector

        if vel_vector.x > 0.1: # Moving right
            self.rotation = math.pi / 2

            if vel_vector.y > 0.1: # Moving down right
                self.rotation = (3/4) * math.pi
            elif vel_vector.y < -0.1: # Moving down left
                self.rotation = math.pi / 4
        elif vel_vector.x < -0.1: # Moving left
            self.rotation = (3/2) * math.pi

            if vel_vector.y > 0.1: # Moving down left
                self.rotation = (5/4) * math.pi
            elif vel_vector.y < -0.1: # Moving up left
                self.rotation = (7/4) * math.pi
        elif vel_vector.y > 0.1: # Moving down
            self.rotation = math.pi
        elif vel_vector.y < -0.1: # Moving up
            self.rotation = 0

    #TODO move to interaction class
    #updates values regarding player position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector

        if self.can_shoot == False and Clock.transition(self.time_between_shots):
            self.can_shoot = True

        if self.can_remove_life == False and Clock.transition(self.time_between_life_loss): # Time between player being able to lose life.
            self.can_remove_life = True

    #TODO simplify and move to interaction class
    #function to draw the player
    def draw(self, canvas):
        self.update()
        destroy = []
        for i in self.bullets:
            if i.alive == False:
                destroy.append(i)
            else:
                i.draw(canvas)
        for i in destroy:
            self.bullets.remove(i)


        self.sprite.draw(canvas, self.pos, self.rotation)
        if Clock.transition(1):
            self.sprite.next_frame()
    