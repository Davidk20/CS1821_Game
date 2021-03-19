try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.movement import Movement
from source.vector import Vector
from source.enemy_movement import EnemyMovement
from source.collider import SpriteCollider
from source.stats import EnemyStats
from source.spritesheet import Spritesheet
from source.clock import Clock

#TODO clean initialiser
class Enemy (SpriteCollider, EnemyStats):
    def __init__(self, init_pos, target = None, patrol_points = None):
        self.sprite = Spritesheet("source/images/basic_enemy.png", 1, 1)
        self.pos = Vector(init_pos[0],init_pos[1]) #sets the initial position of the enemy.
        self.target = target
        self.patrol_points = patrol_points
        self.in_collision = False
        EnemyStats.__init__(self)
        self.movement = EnemyMovement(self.speed, self.pos, target = self.target, patrol_points = self.patrol_points)
        SpriteCollider.__init__(self, Vector(init_pos[0],init_pos[1]), self.movement)

    #updates values regarding enemy position
    def update(self):
        if Clock.transition(1):
            self.sprite.next_frame()
        self.movement.patrol() # patrols enemy between a set of points
        self.movement.update() # updates enemy position
        self.pos = self.movement.pos_vector

    #function to draw the enemy
    def draw(self, canvas):
        self.update()
        self.sprite.draw(canvas, self.pos)

    def set_patrol_points(self, points):
        if self.target != None:
            self.target = None
        self.movement.set_patrol_points(points)

    def set_target(self):
        if self.patrol_points != None:
            self.patrol_points = None
        self.movement.set_target()