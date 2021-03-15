try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source import game

class Mouse:
    def __init__(self):
        self.pos = None

    def get_click_pos(self):
        temp = self.pos
        self.pos = None
        return temp

    def click_handler(self,position):
        if position != None:
            if position[0] != None:
                self.pos = position


class Button:
    def __init__(self, text, size, pos, frame):
        self.frame = frame
        self.sizes = {"large":[[400,100],64]}
        self.size = self.sizes[size]
        self.text = text
        self.pos = pos
        self.text_color = "white"
        self.button_color = "green"

    def get_centre(self):
        central = self.frame.get_canvas_textwidth(self.text, self.size[1], "sans-serif")
        central = (720 - central) / 2
        return central

    def get_area(self):
        return [
            [self.pos[0],self.pos[1]],
            [self.pos[0], self.pos[1]+self.size[0][1]],
            [self.pos[0]+self.size[0][0],self.pos[1]+self.size[0][1]],
            [self.pos[0]+self.size[0][0],self.pos[1]]
        ]

    def draw(self, canvas):
        canvas.draw_polygon([(self.pos[0],self.pos[1]),
                             (self.pos[0], self.pos[1]+self.size[0][1]), 
                             (self.pos[0]+self.size[0][0],self.pos[1]+self.size[0][1]),
                             (self.pos[0]+self.size[0][0],self.pos[1])
                             ],
                              5,
                              self.button_color, 
                              self.button_color)

        canvas.draw_text(self.text,
                         (self.get_centre(), 
                         self.pos[1]+(self.size[0][1]*0.75)), 
                         self.size[1], 
                         self.text_color, 
                         "sans-serif")

    def clicked(self, mouse_pos):
        button_area = self.get_area()
        if mouse_pos[0] > button_area[0][0] and mouse_pos[0] < button_area[3][0] and mouse_pos[1] > button_area[0][1] and mouse_pos[1] < button_area[2][1]:
            return self.text

class Menu:

    def __init__(self, frame, mode = "start"):
        self.frame = frame
        self.central = self.frame.get_canvas_textwidth('Python Game', 64, "sans-serif")
        self.central = (720 - self.central) / 2
        self.mouse = Mouse()
        if mode == "start":
            self.draw_start()
        elif mode == "died":
            self.draw_game_over()
        self.draw_window()

    def draw_start(self):
        self.mode_text = "Python Game"
        self.startButton = Button("Start Game", "large", [150,200], self.frame)
        self.lbButton = Button("Leaderboard", "large", [150,400], self.frame)
        self.quitButton = Button("Quit", "large", [150, 600], self.frame)
        self.buttons = [self.startButton, self.lbButton, self.quitButton]

    def draw_game_over(self):
        self.mode_text = "GAME OVER"
        self.restartButton = Button("Restart", "large", [150,200], self.frame)
        self.lbButton = Button("Leaderboard", "large", [150,400], self.frame)
        self.quitButton = Button("Quit", "large", [150, 600], self.frame)
        self.buttons = [self.restartButton, self.lbButton, self.quitButton]


    def draw_window(self):
        self.frame.set_draw_handler(self.draw)
        self.frame.set_mouseclick_handler(self.mouse.click_handler)
        self.frame.set_canvas_background("black")
        self.frame.start()


    def draw(self, canvas):
        self.update()
        canvas.draw_text(self.mode_text,
                         (self.central, 150), 
                        64, 
                        'White', 
                        "sans-serif")
        for button in self.buttons:
            button.draw(canvas)

    def update(self):
        mouse_pos = self.mouse.get_click_pos()
        if mouse_pos != None:
            for button in self.buttons:
                clicked = button.clicked(mouse_pos)
                if clicked == "Start Game" or clicked == "Restart":
                    game.Game(self.frame)
                if clicked == "Quit":
                    self.quit()

    def quit(self):
        if self.frame._keep_timers != None:
            simplegui.Timer._stop_all()
        self.frame.stop()
        self.frame._running = False


if __name__ == "__main__":
    frame = simplegui.create_frame("Game", 720 , 720, 0)
    menu = Menu(frame, "start")