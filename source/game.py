try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from keyboard import Keyboard
from enemy import Enemy


class Game:
    def __init__(self):
        self.player = Player([350,350])
        self.enemy = Enemy(30, 1, [50,50])
        self.kbd = Keyboard()
        self.interaction = Interaction(self.player, self.kbd)
        self.game_window_setup()


    #Setup of SimpleGUI window
    def game_window_setup(self):
        frame = simplegui.create_frame("Game", 700 , 700, 0)
        frame.set_canvas_background("#534a32")
        frame.set_keydown_handler(self.kbd.keyDown)
        frame.set_keyup_handler(self.kbd.keyUp)
        frame.set_draw_handler(self.draw)
        frame.start()

    #Function handling drawing of all shapes on screen
    def draw(self, canvas):
        self.player.draw(canvas)
        self.enemy.draw(canvas)
        self.interaction.update()


# Class to link player to keyboard for interactions with other shapes
class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard
    
    def update(self):
        self.player.check_input(self.keyboard)
        self.player.rotate() # Rotates the player every frame.

if __name__ == "__main__":
    Game()