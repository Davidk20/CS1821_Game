try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.vector import Vector
from source.movement import Movement
from source.projectile import Projectile
from source.collider import Collider
import os, math

class Player(Collider):
    def __init__(self, init_pos):
        super().__init__("circ", Vector(init_pos[0],init_pos[1]), 16, Vector(0, 0))
        self.image = simplegui._load_local_image("source/images/player.png")
        self.pos = Vector(init_pos[0],init_pos[1])
        self.rotation = 0

        #TODO move to interaction class handling time between actions
        self.time = 0
        self.can_shoot = True
        self.can_remove_life = True

        self.alive = True
        self.speed = 2
        self.lives = 3
        self.score = 0
        self.bullets = []

        #TODO move into instance of interaction
        self.movement = Movement(self.speed, self.pos)

    #TODO move to interaction
    #function to check and control player movement
    def check_input(self, keyboard):
        if keyboard.left == True:
            self.movement.move_horizontal(-1) #move left
        if keyboard.right == True:
            self.movement.move_horizontal(1) #move right
        if keyboard.up == True:
            self.movement.move_vertical(1) #move up
        if keyboard.down == True:
            self.movement.move_vertical(-1) #move down
        if keyboard.space == True and self.can_shoot:
            self.last_shot_time = self.time
            self.can_shoot = False
            fire = Projectile(
                self.pos.get_p(),
                self.rotation,
                4,
                "blue"
                )
            self.bullets.append(fire)

    #TODO move into movement class
    def rotate(self):
        """
        Rotates the player based off their velocity vector.
        """
        vel_vector = self.movement.vel_vector

        if vel_vector.x > 0.1: # Moving right
            self.rotation = math.pi / 2

            if vel_vector.y > 0.1: # Moving down right
                self.rotation = (3/4) * math.pi
            elif vel_vector.y < -0.1: # Moving down left
                self.rotation = math.pi / 4
        elif vel_vector.x < -0.1: # Moving left
            self.rotation = (3/2) * math.pi

            if vel_vector.y > 0.1: # Moving down left
                self.rotation = (5/4) * math.pi
            elif vel_vector.y < -0.1: # Moving up left
                self.rotation = (7/4) * math.pi
        elif vel_vector.y > 0.1: # Moving down
            self.rotation = math.pi
        elif vel_vector.y < -0.1: # Moving up
            self.rotation = 0

    #TODO move to interaction class
    #updates values regarding player position
    def update(self):
        self.movement.update()
        self.pos = self.movement.pos_vector

        self.time += 1

        if self.can_shoot == False and self.time - self.last_shot_time >= 20:
            self.can_shoot = True

        if self.can_remove_life == False and self.time - self.last_time_remove_life >= 40: # Time between player being able to lose life.
            self.can_remove_life = True

    #TODO simplify and move to interaction class
    #function to draw the player
    def draw(self, canvas):
        self.update()
        destroy = []
        for i in self.bullets:
            if i.out_of_bounds():
                destroy.append(i)
            else:
                i.draw(canvas)
        for i in destroy:
            self.bullets.remove(i)

        canvas.draw_image(
            self.image,
             (16, 16),
             (32, 32),
             self.pos.get_p(), 
             (32,32),
             self.rotation
        )
	
    #TODO move into collider, or create PlayerCollider
    # Overrides the function from the Collider class.
    def bounceZeroMass(self, collider):
        if collider.shape == "wall":
            self.movement.vel_vector.add(collider.normal.copy().multiply(self.speed))
        elif collider.shape == "circ":
            self.movement.vel_vector.add(self.pos.copy().subtract(collider.pos).normalize().multiply(self.speed))
        elif collider.shape == "rect":
            normal = self.pos.copy().subtract(collider.pos).normalize()
            if abs(normal.x) > abs(normal.y):
                normal = Vector(normal.x, 0).normalize()
            else:
                normal = Vector(0, normal.y).normalize()
            self.movement.vel_vector.add(normal.multiply(self.speed))

    def die(self):
        self.alive = False

    #add/remove functions for all values
    def set_life(self,value):
        if value > 0:
            self.lives += 0
        else:
            if self.can_remove_life: # only removes life if a sufficient amount of time has passed.
                self.last_time_remove_life = self.time
                self.can_remove_life = False
                self.lives += value
            if self.lives <= 0:
                self.die()

    def get_lives(self):
        return self.lives

    def set_speed(self, value):
        self.speed += value

    def set_score(self, value):
        self.score += value

    def get_score(self):
        return self.score

    def get_bullets(self):
        return self.bullets