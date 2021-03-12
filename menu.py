try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import source

class Menu:

    def __init__(self):
        self.draw_window()


    def draw_window(self):
        self.frame = simplegui.create_frame("Game", 720 , 720, 0)
        self.frame.set_draw_handler(self.draw)
        self.frame.start()

    def button_handler(self):
        print("yeet")

    def draw(self, canvas):
        canvas.draw_text('Python Game', ((self.frame.get_canvas_textwidth("Python Game", 64)), 200), 64, 'White', "sans-serif")
        button1 = self.frame.add_button('Label 1', self.button_handler)

if __name__ == "__main__":
    menu = Menu()
