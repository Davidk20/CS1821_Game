try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.movement import Movement
from source.vector import Vector

class EnemyMovement (Movement):
    def __init__(self, speed, pos_vector, patrol_points = None, target = None):
        super().__init__(speed, pos_vector)
        self.current_point = 0
        self.patrol_points = patrol_points # None by default
        self.target = target # None by default

    # Moves the enemy towards a particular target.
    def move_towards_target(self):
        delta_x = self.target.x - self.pos_vector.x # difference in x plane
        delta_y = self.target.y - self.pos_vector.y # difference in y plane

        if delta_x == 0 and delta_y == 0:
            return

        target_vector = Vector(delta_x, delta_y).normalize() # normalised vector from delta x & delta y
        self.vel_vector.add(target_vector)

    def patrol(self):
        if self.patrol_points == None:
            return # Escapes if their are no patrol points.
        else:
            # Checks if the player's current point is greater than the amount of patrol points
            if self.current_point + 1 > len(self.patrol_points):
                self.current_point = 0 # Resets current point back to 0
            
            self.target = self.patrol_points[self.current_point] # Sets the target to be the current patrol point 

            self.move_towards_target()

            # Checks if the current enemy position matches their current patrol position.
            if round(self.pos_vector.x) == self.patrol_points[self.current_point].x and round(self.pos_vector.y) == self.patrol_points[self.current_point].y:
                self.current_point += 1

    def set_target(self):
        self.target = self.patrol_points[self.current_point]

    def set_patrol_points(self, points):
        self.patrol_points = points