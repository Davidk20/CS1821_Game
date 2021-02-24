try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Movement:
  def __init__(self, speed):
    self.speed = speed

  def move_horizontal(self, direction):
    if direction < 0:
      #move left
      pass
    elif direction > 0:
      #move right
      pass

  def move_vertical(self, direction):
    if direction > 0:
      #move up
      pass
    elif direction < 0:
      #move down
      pass
