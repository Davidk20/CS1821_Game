try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Keyboard:
	def __init__(self):
		self.left = False
		self.right = False
		self.up = False
		self.down = False

	def keyDown(self, key):
		if key == simplegui.KEY_MAP['a'] or key == simplegui.KEY_MAP['left']:
			self.left = True
		elif key == simplegui.KEY_MAP['d'] or key == simplegui.KEY_MAP['right']:
			self.right = True
		elif key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['up']:
			self.up = True
		elif key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['down']:
			self.down = True

	def keyUp(self, key):
		if key == simplegui.KEY_MAP['a'] or key == simplegui.KEY_MAP['left']:
			self.left = False
		elif key == simplegui.KEY_MAP['d'] or key == simplegui.KEY_MAP['right']:
			self.right = False
		elif key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['up']:
			self.up = False
		elif key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['down']:
			self.down = False
		
    