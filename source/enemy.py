try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.movement import Movement, EnemyMovement
from source.vector import Vector
from source.collider import SpriteCollider
from source.stats import EnemyStats
from source.spritesheet import Spritesheet
from source.clock import Clock

class Enemy (SpriteCollider, EnemyStats):
    def __init__(self, init_pos, target = None, patrol_points = None):
        self.sprite = Spritesheet("source/images/enemy_sheet.png", 4, 2)
        self.pos = Vector(init_pos[0],init_pos[1]) #sets the initial position of the enemy.
        self.target = target # sets initial enemy target, if there is one.
        self.patrol_points = patrol_points # sets initial patrol points, if there are some.
        self.in_collision = False # initial collision state.
        EnemyStats.__init__(self)
        self.movement = EnemyMovement(self.speed, self.pos, target = self.target, patrol_points = self.patrol_points)
        SpriteCollider.__init__(self, Vector(init_pos[0],init_pos[1]), self.movement)

    #updates values regarding enemy position
    def update(self):
        if Clock.transition(10):
            self.sprite.next_frame()
        self.movement.patrol() # patrols enemy between a set of points
        self.movement.update() # updates enemy position
        self.pos = self.movement.pos_vector

    #function to draw the enemy
    def draw(self, canvas):
        self.update()
        self.sprite.draw(canvas, self.pos, self.movement.get_rotation())

    def set_patrol_points(self, points):
        if self.target != None:
            self.target = None
        self.movement.set_patrol_points(points)

    def set_target(self):
        if self.patrol_points != None:
            self.patrol_points = None
        self.movement.set_target()