try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from movement import Movement
from projectile import Projectile
import os, math


class Player:
    def __init__(self, init_pos):
        self.image = simplegui._load_local_image("images/player.png")
        self.pos = Vector(init_pos[0],init_pos[1])
        self.in_collision = False
        self.rotation = 0

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
            self.rotation = -math.pi/2
            self.movement.move_horizontal(-1) #move left
        elif keyboard.right == True:
            self.rotation = math.pi/2
            self.movement.move_horizontal(1) #move right
        elif keyboard.up == True:
            self.rotation = 0
            self.movement.move_vertical(1) #move up
        elif keyboard.down == True:
            self.rotation = math.pi
            self.movement.move_vertical(-1) #move down
        elif keyboard.space == True:
            fire = Projectile(
                self.pos,
                self.rotation,
                2,
                "blue"
                )
            self.bullets.append(fire)

    #updates values regarding player position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector

    #function to draw the player
    def draw(self, canvas):
        self.update()
        for i in self.bullets:
            i.draw(canvas)

        canvas.draw_image(
            self.image,
             (16, 16),
             (32, 32),
             self.pos.get_p(), 
             (64,64),
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