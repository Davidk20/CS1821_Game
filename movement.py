try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector

class Movement:
  def __init__(self, speed, pos_vector):
    self.speed = speed
    self.pos_vector = pos_vector

  def move_horizontal(self, direction):
    """
    Direction: -1 = move left
    Direction: 1 = move right
    """
    if direction < 0:
      self.pos_vector.add(Vector(-speed, 0)) 
      pass
    elif direction > 0:
      self.pos_vector.add(Vector(speed, 0)) 
      pass

  def move_vertical(self, direction):
    """
    Direction: -1 = move down
    Direction: 1 = move up
    """
    if direction > 0:
      self.pos_vector.add(Vector(0, speed)) 
      pass
    elif direction < 0:
      self.pos_vector.add(Vector(0, -speed))
      pass
