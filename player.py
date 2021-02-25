try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from movement import Movement

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
        self.speed = 2
        self.lives = 3
        self.score = 0
        self.coins = 0
        self.inventory = []

        self.movement = Movement(self.speed, self.pos)

    
    def check_input(self, keyboard):
        if keyboard.left == True:
            self.movement.move_horizontal(-1)
        elif keyboard.right == True:
            self.movement.move_horizontal(1)
        elif keyboard.up == True:
            self.movement.move_vertical(1)
        elif keyboard.down == True:
            self.movement.move_vertical(-1)

    def update(self):
        self.pos = self.movement.pos_vector

    def draw(self, canvas):
        self.update()
        canvas.draw_circle(self.pos.get_p(),
                self.radius ,
                self.border,
                self.color,
                self.color)
