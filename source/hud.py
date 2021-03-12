try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player

#TODO move globally
WIDTH = 720
HEIGHT = 720

class Hud:
    def __init__(self, player):
        self.player = player

        self.hearts_img = simplegui._load_local_image("images/hearts.png")
        self.hearts_img_width = self.hearts_img.get_width()
        self.hearts_img_height = self.hearts_img.get_height()
        self.hearts_centre = [self.hearts_img_width/2, self.hearts_img_height/2]
        self.hearts_x = WIDTH/8
        self.hearts_y = HEIGHT/14

        #TODO use getters from player.py
        self.lives = 3
        
        self.score_x = WIDTH - 200
        self.score_y = HEIGHT - 663
        

    def draw(self, canvas):
        
        canvas.draw_image(self.hearts_img, self.hearts_centre, (self.hearts_img_width, self.hearts_img_height), (self.hearts_x, self.hearts_y), (self.hearts_img_width, self.hearts_img_height))
        canvas.draw_text('Score: ' + str(self.player.score), (self.score_x, self.score_y), 28, 'White', 'sans-serif')
        
        #checks if health has depleted
        if self.lives > self.player.lives:
            Hud.hit(self)
            self.lives -= 1

    #updates the image corresponding to health
    def hit(self):
        if self.hearts_img_width >= 45:
            self.hearts_img_width = self.hearts_img_width - 45
            self.hearts_centre = [self.hearts_img_width/2, self.hearts_img_height/2]
