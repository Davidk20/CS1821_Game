try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from keyboard import Keyboard

class Game:
    def __init__(self):
        self.player = Player(30, 350)
        self.kbd = Keyboard()
        self.interaction = Interaction(self.player, self.kbd)

        frame = simplegui.create_frame("Game", 700 , 700)
        frame.set_canvas_background("#534a32")
        frame.set_keydown_handler(self.kbd.keyDown)
        frame.set_keyup_handler(self.kbd.keyUp)
        frame.set_draw_handler(self.draw)
        frame.start()

    def draw(self, canvas):
        self.player.draw(canvas)
        self.interaction.update()

class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard
    
    def update(self):
        self.player.check_input(self.keyboard)

if __name__ == "__main__":
    Game()