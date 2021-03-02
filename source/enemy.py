try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from movement import Movement

class Enemy:
  def __init__(self, radius, speed, init_pos):
    self.radius = radius
    self.speed = speed
    self.pos = init_pos #sets the initial position of the enemy.
    self.in_collision = False
    self.movement = Movement(self.speed, self.pos)

    self.health = 100
    self.damage = 20

     #updates values regarding enemy position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector

    #function to draw the enemy
    def draw(self, canvas):
        self.update()
        canvas.draw_circle(self.pos.get_p(),
                self.radius ,
                self.border,
                self.color,
                self.color)

    def remove_health(self, amount):
      self.health -= amount

    