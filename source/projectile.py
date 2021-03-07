try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
import math

class Projectile:
    def __init__(self, init_pos, player_direction, radius, color):
        self.pos = Vector(init_pos[0], init_pos[1])
        #initial position - Type = Vector
        self.vel = self.get_vector(player_direction)
        #player_direction - Type = angle (rads)
        self.radius = radius
        #Projectile radius - Type = Int
        self.color = color
        #Projectile color - Type = string

    def out_of_bounds(self):
        current_pos = self.pos.get_p()
        if current_pos[0] > 700 or current_pos [0] < 0 or current_pos[1] > 700 or current_pos [1] < 0:
            return True
        else:
            return False

    def get_vector(self, direction):
        coords = self.pos.get_p()
        x = 10 * math.cos(math.degrees(direction)) #+ int(coords[0])
        y = 10 * math.sin(math.degrees(direction)) #+ int(coords[1])
        return Vector(x, y)


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