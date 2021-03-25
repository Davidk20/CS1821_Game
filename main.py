try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source import game

class Mouse:
    '''
    Class to handle the mouse interacting with the 
    Main menu
    '''
    def __init__(self):
        self.pos = None

    def get_click_pos(self):
        '''
        returns click position
        '''
        temp = self.pos
        self.pos = None
        return temp

    def click_handler(self,position):
        '''
        stores click position when triggered by frame
        '''
        if position != None:
            if position[0] != None:
                self.pos = position

class Button:
    '''
    class to draw a button on the main menu screen
    '''
    def __init__(self, text, size, pos, frame):
        self.frame = frame
        self.sizes = {"large":[[400,100],64]}
        self.size = self.sizes[size]
        self.text = text
        self.pos = pos
        self.text_color = "white"
        self.button_color = "green"

    def get_centre(self):
        '''
        returns the position needed to correctly centre text on screen
        '''
        central = self.frame.get_canvas_textwidth(self.text, self.size[1], "sans-serif")
        central = (720 - central) / 2
        return central

    def get_area(self):
        '''
        returns the list of coords for the shape of the button
        '''
        return [
            [self.pos[0],self.pos[1]],
            [self.pos[0], self.pos[1]+self.size[0][1]],
            [self.pos[0]+self.size[0][0],self.pos[1]+self.size[0][1]],
            [self.pos[0]+self.size[0][0],self.pos[1]]
        ]


    def draw(self, canvas):
        '''
        Method draws the button and text on the frame
        '''
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
        '''
        Method checks whether button has been clicked and returns the text of the button
        '''
        button_area = self.get_area()
        if mouse_pos[0] > button_area[0][0] and mouse_pos[0] < button_area[3][0] and mouse_pos[1] > button_area[0][1] and mouse_pos[1] < button_area[2][1]:
            return self.text

class Menu:
    def __init__(self, frame, mode = "start", score = 0):
        self.frame = frame
        self.score = score
        self.mouse = Mouse()
        if mode == "start":
            self.draw_start()
        elif mode == "died":
            self.draw_game_over()
        self.draw_window()


    def get_central(self, text):
        '''
        returns the position needed to correctly centre text on screen
        '''
        central = self.frame.get_canvas_textwidth(text, 64, "sans-serif")
        return (720 - central) / 2


    def draw_start(self):
        '''
        method to draw the start menu screen
        '''
        self.mode_text = "Python Game"
        self.score_text = " "
        self.startButton = Button("Start Game", "large", [150,200], self.frame)
        self.quitButton = Button("Quit", "large", [150, 400], self.frame)
        self.buttons = [self.startButton, self.quitButton]


    def draw_game_over(self): 
        '''
        method to draw the game over screen
        '''
        self.mode_text = "GAME OVER"
        self.score_text = "You scored " + str(self.score) + " points!"
        self.restartButton = Button("Restart", "large", [150,250], self.frame)
        self.quitButton = Button("Quit", "large", [150, 400], self.frame)
        self.buttons = [self.restartButton, self.quitButton]


    def draw_window(self):
        '''
        method to configure handlers start the frame
        '''
        self.frame.set_draw_handler(self.draw)
        self.frame.set_mouseclick_handler(self.mouse.click_handler)
        self.frame.set_canvas_background("black")
        self.frame.start()


    def draw(self, canvas):
        '''
        method to draw the objects on the canvas
        '''
        self.update()
        canvas.draw_text(self.mode_text,
                         (self.get_central(self.mode_text), 150), 
                        64, 
                        'White', 
                        "sans-serif")
        canvas.draw_text(self.score_text,
                         (self.get_central(self.score_text), 220), 
                        64, 
                        'White', 
                        "sans-serif")
        for button in self.buttons:
            button.draw(canvas)

    def update(self):
        '''
        method to update the objects and check for a click
        '''
        mouse_pos = self.mouse.get_click_pos()
        if mouse_pos != None:
            for button in self.buttons:
                clicked = button.clicked(mouse_pos)
                if clicked == "Start Game" or clicked == "Restart":
                    game.Game(self.frame)
                if clicked == "Quit":
                    self.quit()

    def quit(self):
        '''
        method to quit the program
        '''
        if self.frame._keep_timers != None:
            simplegui.Timer._stop_all()
        self.frame.stop()
        self.frame._running = False


if __name__ == "__main__":
    frame = simplegui.create_frame("Game", 720 , 720, 0)
    menu = Menu(frame, "start")
