try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from movement import Movement
from vector import Vector
from enemy_movement import EnemyMovement
import os

class Enemy:
    def __init__(self, radius, speed, init_pos):
        self.image = simplegui._load_local_image("images/basic_enemy.png")
        self.speed = speed
        self.pos = Vector(init_pos[0],init_pos[1]) #sets the initial position of the enemy.
        self.in_collision = False
        self.movement = EnemyMovement(self.speed, self.pos, patrol_points=[Vector(210, 210), Vector(510, 210), Vector(510, 510), Vector(210, 510)])

        self.health = 100
        self.damage = 20

     #updates values regarding enemy position
    def update(self):
        self.movement.patrol() # patrols enemy between a set of points
        self.movement.update() # updates enemy position
        self.pos = self.movement.pos_vector

    #function to draw the enemy
    def draw(self, canvas):
        self.update()
        canvas.draw_image(
            self.image,
            (16,16),
            (32,32),
            self.pos.get_p(),
            (32,32)
        )

    def remove_health(self, amount):
        self.health -= amount

    