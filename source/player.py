try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from movement import Movement
import os


class Player:
    def __init__(self, init_pos):
        cwd = os.getcwd()
        cwd = cwd + "\images\player.png"
        cwd = cwd.replace(" ", "\ ")
        self.image = simplegui.load_image(cwd)
        self.pos = Vector(init_pos[0],init_pos[1])
        self.in_collision = False

        self.speed = 2
        self.lives = 3
        self.score = 0
        self.coins = 0
        self.inventory = []

        self.movement = Movement(self.speed, self.pos)

    #function to check and control player movement
    def check_input(self, keyboard):
        if keyboard.left == True:
            self.movement.move_horizontal(-1) #move left
        elif keyboard.right == True:
            self.movement.move_horizontal(1) #move right
        elif keyboard.up == True:
            self.movement.move_vertical(1) #move up
        elif keyboard.down == True:
            self.movement.move_vertical(-1) #move down

    #updates values regarding player position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector

    #function to draw the player
    def draw(self, canvas):
        self.update()
        canvas.draw_image(
            self.image,
             (16, 16),
             (32, 32),
             self.pos.get_p(), 
             (64,64)
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