try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.vector import Vector
import math

class Movement:
    def __init__(self, speed, pos_vector):
        self.speed = speed
        self.pos_vector = pos_vector
        self.vel_vector = Vector()
        self.rotation = 0

    def move_horizontal(self, direction):
        """
        Direction: -1 = move left
        Direction: 1 = move right
        """
        if direction < 0:
          self.vel_vector.add(Vector(-self.speed, self.vel_vector.y)) #move left
        elif direction > 0:
          self.vel_vector.add(Vector(self.speed, self.vel_vector.y)) #move right

    def move_vertical(self, direction):
        """
        Direction: -1 = move down
        Direction: 1 = move up
        """
        if direction > 0:
          self.vel_vector.add(Vector(self.vel_vector.x, -self.speed)) #move down
        elif direction < 0:
          self.vel_vector.add(Vector(self.vel_vector.x, self.speed)) #move up

    def check_out_range(self, value):
        """
        A clamping function which will ensure that the speed of the player does not exceed the defined
        speed variable.
        """

        if value > self.speed:
            return self.speed
        elif value < -self.speed:
            return -self.speed
        else:
            return value

    def update(self):
        self.vel_vector = Vector(self.check_out_range(self.vel_vector.x), self.check_out_range(self.vel_vector.y))
        self.rotate()
        self.pos_vector.add(self.vel_vector)
        self.vel_vector.multiply(0.3) #Dampens movement when coming to stop

        
    def rotate(self):
        """
        Rotates the player based off their velocity vector.
        """
        if self.vel_vector.x > 0.1: # Moving right
            self.rotation = math.pi / 2

            if self.vel_vector.y > 0.1: # Moving down right
                self.rotation = (3/4) * math.pi
            elif self.vel_vector.y < -0.1: # Moving down left
                self.rotation = math.pi / 4
        elif self.vel_vector.x < -0.1: # Moving left
            self.rotation = (3/2) * math.pi

            if self.vel_vector.y > 0.1: # Moving down left
                self.rotation = (5/4) * math.pi
            elif self.vel_vector.y < -0.1: # Moving up left
                self.rotation = (7/4) * math.pi
        elif self.vel_vector.y > 0.1: # Moving down
            self.rotation = math.pi
        elif self.vel_vector.y < -0.1: # Moving up
            self.rotation = 0

    def get_pos(self):
        return self.pos_vector

    def get_rotation(self):
        return self.rotation

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

        if delta_x == 0 and delta_y == 0: # ensures there are no division by 0 errors when normalising
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