try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.vector import Vector

class Movement:
    def __init__(self, speed, pos_vector):
        self.speed = speed
        self.pos_vector = pos_vector
        self.vel_vector = Vector()

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
        A clamping function which will ensure that the speed of the player does not exist the defined
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

        self.pos_vector.add(self.vel_vector)
        self.vel_vector.multiply(0.3) #Dampens movement when coming to stop

    def get_pos(self):
        return self.pos_vector