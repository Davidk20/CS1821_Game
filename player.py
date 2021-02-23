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

        self.max_health = 100
        self.current_health = self.max_health
        self.speed = 1
        self.lives = 3
        self.score = 0
        self.coins = 0
        self.inventory = []



    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                self.radius ,
                self.border,
                self.color,
                self.color)