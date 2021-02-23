try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player


class Game:
    def __init__(self):
        self.player = Player(30, 350)
        frame = simplegui.create_frame("Game", 700 , 700)
        frame.set_draw_handler(self.draw)
        frame.start()

    def draw(self, canvas):
        self.player.draw(canvas)



if __name__ == "__main__":
    Game()