try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from movement import Movement
from vector import Vector

class EnemyMovement (Movement):
    def __init__(self, speed, pos_vector, patrol_points = None, target = None):
        super(speed, pos_vector)
        self.current_point = 0
        self.patrol_points = patrol_points # None by default
        self.target = target # None by default

    # Moves the enemy towards a particular target.
    def move_towards_target(self, target):
        delta_x = target.x - self.pos_vector.x
        delta_y = target.y - self.pos_vector.y 

        target_vector = Vector(delta_x, delta_y).normalize()
        self.vel_vector.add(target_vector)

    def patrol(self):
        pass