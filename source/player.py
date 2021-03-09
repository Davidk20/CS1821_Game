try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from movement import Movement
from projectile import Projectile
from collider import Collider
import os, math


class Player(Collider):
    def __init__(self, init_pos):
        super().__init__("circ", Vector(init_pos[0],init_pos[1]), 16, Vector(0, 0))
        self.image = simplegui._load_local_image("images/player.png")
        self.pos = Vector(init_pos[0],init_pos[1])
        self.in_collision = False
        self.rotation = 0
        self.time = 0
        
        self.shoot = True
        self.speed = 2
        self.lives = 3
        self.score = 0
        self.coins = 0
        self.inventory = []
        self.bullets = []

        self.movement = Movement(self.speed, self.pos)

    #function to check and control player movement
    def check_input(self, keyboard):
        if keyboard.left == True:
            self.movement.move_horizontal(-1) #move left
        if keyboard.right == True:
            self.movement.move_horizontal(1) #move right
        if keyboard.up == True:
            self.movement.move_vertical(1) #move up
        if keyboard.down == True:
            self.movement.move_vertical(-1) #move down
        if keyboard.space == True and self.shoot:
            self.last_shot_time = self.time
            self.shoot = False
            fire = Projectile(
                self.pos.get_p(),
                self.rotation,
                4,
                "blue"
                )
            self.bullets.append(fire)

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

    #updates values regarding player position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector
        self.time += 1
        if self.shoot == False and self.time - self.last_shot_time >= 20:
            self.shoot = True

    #function to draw the player
    def draw(self, canvas):
        self.update()
        destroy = []
        for i in self.bullets:
            if i.out_of_bounds():
                destroy.append(i)
            else:
                i.draw(canvas)
        for i in destroy:
            self.bullets.remove(i)

        canvas.draw_image(
            self.image,
             (16, 16),
             (32, 32),
             self.pos.get_p(), 
             (32,32),
             self.rotation
        )


    #add/remove functions for all values
    def remove_life(self,value):
        self.lives -= value

    def add_life(self, value):
        self.lives += value

    def remove_speed(self, value):
        self.speed -= value
    
    def add_speed(self, value):
        self.speed += value

    def remove_score(self, value):
        self.score -= value
    
    def add_score(self, value):
        self.score += value

    def remove_coins(self, value):
        self.coins -= value

    def add_coins(self, value):
        self.coins += value

    def remove_inventory(self, value):
        self.inventory.remove(value)

    def add_inventory(self, value):
        self.inventory.append(value)