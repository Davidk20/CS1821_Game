try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.vector import Vector
from source.collider import Collider
import math


class Projectile(Collider):
    def __init__(self, init_pos, player_direction, radius, color):
        super().__init__("circ", Vector(init_pos[0],init_pos[1]), radius)
        self.vectors = {
            0.0:Vector(0,-1),
            45.0:Vector(1,-1),
            90.0:Vector(1,0),
            135.0:Vector(1,1),
            180.0:Vector(0,1),
            225.0:Vector(-1,1),
            270.0:Vector(-1,0),
            315.0:Vector(-1,-1)
            }
        self.pos = Vector(init_pos[0], init_pos[1])
        #initial position - Type = Vector
        self.vel = self.get_vector(player_direction)
        #player_direction - Type = angle (rads)
        self.radius = radius
        #Projectile radius - Type = Int
        self.color = color
        #Projectile color - Type = string
        self.damage = 50

    #TODO link to movement class
    def out_of_bounds(self):
        current_pos = self.pos.get_p()
        if current_pos[0] > 700 or current_pos [0] < 0 or current_pos[1] > 700 or current_pos [1] < 0:
            return True
        else:
            return False

    def get_vector(self, direction):
        new_vector = self.vectors[math.degrees(direction)]
        return new_vector.multiply(10)

    def get_damage(self):
        return self.damage

    def draw(self, canvas):
        if self.out_of_bounds():
            return
        else:
            self.update()
            canvas.draw_circle(
                self.pos.get_p(),
                self.radius,
                1,
                self.color,
                self.color
            )

    def update(self):
        self.pos.add(self.vel)