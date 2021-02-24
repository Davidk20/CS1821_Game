try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Keyboard:
  def __init__(self):
    self.left = False
    self.right = False
    self.up = False
    self. down = False

  def keyDown(self, key):
    if key == simplegui.KEY_MAP['a']:
      self.left = True
    elif key == simplegui.KEY_MAP['d']:
      self.right = True
    elif key == simplegui.KEY_MAP['w']:
      self.up = True
    elif key == simplegui.KEY_MAP['s']:
      self.down = True

  def keyUp(self, key):
    if key == simplegui.KEY_MAP['a']:
      self.left = False
    elif key == simplegui.KEY_MAP['d']:
      self.right = False
    elif key == simplegui.KEY_MAP['w']:
      self.up = False
    elif key == simplegui.KEY_MAP['s']:
      self.down = False
    
    