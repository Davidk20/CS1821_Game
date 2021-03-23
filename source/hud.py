try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.player import Player

WIDTH = 720
HEIGHT = 720

class Hud:
    def __init__(self, player):
        """
        Simple inititaliser that loads hearts sprite and determines location of hud elements
        """
        self.player = player
        self.lives = 3

        self.hearts_img = simplegui._load_local_image("source/images/hearts.png")
        self.hearts_img_width = self.hearts_img.get_width()
        self.hearts_img_height = self.hearts_img.get_height()
        self.hearts_centre = [self.hearts_img_width/2, self.hearts_img_height/2]
        self.hearts_x = WIDTH/8
        self.hearts_y = HEIGHT/14

        self.score_x = WIDTH - 200
        self.score_y = HEIGHT - 663
        

    def draw(self, canvas):
        canvas.draw_image(self.hearts_img, self.hearts_centre, (self.hearts_img_width, self.hearts_img_height), (self.hearts_x, self.hearts_y), (self.hearts_img_width, self.hearts_img_height))
        canvas.draw_text('Score: ' + str(self.player.get_score()), (self.score_x, self.score_y), 28, 'White', 'sans-serif')
        
        if self.lower_health():
            self.hit()
        if self.up_health():
            self.heal()

    """
    Checks if the player has either gained or lost lives making the hud update automatically
    once the player object has lost or gained health
    """
    def lower_health(self):
        return self.lives > self.player.get_lives()

    def up_health(self):
        return self.lives < self.player.get_lives()

    """
    Updates the image corresponding to health either cropping it or enlarging it
    """
    def hit(self):
        if self.hearts_img_width >= 45:
            self.hearts_img_width -= 45
            self.hearts_centre = [self.hearts_img_width/2, self.hearts_img_height/2]
            self.lives -= 1

    def heal(self):
        if self.hearts_img_width < 135:
            self.hearts_img_width += 45
            self.hearts_centre = [self.hearts_img_width/2, self.hearts_img_height/2] 
            self.lives += 1