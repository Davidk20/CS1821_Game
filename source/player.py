try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.clock import Clock
from source.vector import Vector
from source.movement import Movement
from source.projectile import Projectile
from source.collider import SpriteCollider
from source.stats import PlayerStats
from source.spritesheet import Spritesheet

class Player(SpriteCollider, PlayerStats):
    def __init__(self, init_pos):
        PlayerStats.__init__(self)
        self.pos = Vector(init_pos[0],init_pos[1])
        self.movement = Movement(self.speed, self.pos)
        SpriteCollider.__init__(self, Vector(init_pos[0],init_pos[1]), self.movement)
        self.sprite = Spritesheet("source/images/player_sheet.png", 4, 2)

    #updates values regarding player position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector

        if self.can_shoot == False and Clock.transition(self.time_between_shots):
            self.can_shoot = True

        if self.can_remove_life == False and Clock.transition(self.time_between_life_loss): # Time between player being able to lose life.
            self.can_remove_life = True


    #function to draw the player
    def draw(self, canvas):
        self.update()
        destroy = []
        for i in self.bullets:
            if i.alive == False:
                destroy.append(i)
            else:
                i.draw(canvas)
        for i in destroy:
            self.bullets.remove(i)

        self.sprite.draw(canvas, self.pos, self.movement.get_rotation())
        if Clock.transition(10):
            self.sprite.next_frame()
    