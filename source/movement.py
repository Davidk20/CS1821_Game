try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector

class Movement:
  def __init__(self, speed, pos_vector):
    self.speed = speed
    self.pos_vector = pos_vector
    self.vel_vector = Vector()

    self.patrol_points = patrol_points

  def move_horizontal(self, direction):
    """
    Direction: -1 = move left
    Direction: 1 = move right
    """
    if direction < 0:
      self.vel_vector.add(Vector(-self.speed, self.vel_vector.y)) #move left
    elif direction > 0:
      self.vel_vector.add(Vector(self.speed, self.vel_vector.y)) #move right

  def move_vertical(self, direction):
    """
    Direction: -1 = move down
    Direction: 1 = move up
    """
    if direction > 0:
      self.vel_vector.add(Vector(self.vel_vector.x, -self.speed)) #move down
    elif direction < 0:
      self.vel_vector.add(Vector(self.vel_vector.x, self.speed)) #move up

  def update(self):
    self.pos_vector.add(self.vel_vector)
    self.vel_vector.multiply(0.3) #Dampens movement when coming to stop
