try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector

class Player:
    def __init__(self, radius, centre):
        self.radius = radius
        self.game_centre = centre
        self.pos = Vector(centre,centre)
        self.border = 1
        self.color = "white"
        self.in_collision = False


    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                self.radius ,
                self.border,
                self.color,
                self.color)