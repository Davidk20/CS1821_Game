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
      self.pos_vector.add(Vector(-self.speed, 0)) 
    elif direction > 0:
      self.pos_vector.add(Vector(self.speed, 0)) 

  def move_vertical(self, direction):
    """
    Direction: -1 = move down
    Direction: 1 = move up
    """
    if direction > 0:
      self.pos_vector.add(Vector(0, -self.speed)) 
    elif direction < 0:
      self.pos_vector.add(Vector(0, self.speed))

  def check_input(self, keyboard):
    if keyboard.left == True:
      self.move_horizontal(-1)
    elif keyboard.right == True:
      self.move_horizontal(1)
    elif keyboard.up == True:
      self.move_vertical(1)
    elif keyboard.down == True:
      self.move_vertical(-1)
