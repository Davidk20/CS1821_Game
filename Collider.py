from vector.py import Vector


class ColliderDimensionError(Exception):
    pass


class Collider:
    def __init__(self, shape, pos, a=None, b=None, c=None):
        self.shape = shape
        self.pos = pos
        # initialize circle collider
        if self.shape == circ:
            if a == None:
                # if a circle collider is created without radius it will cause errors later
                # so best to throw error here to show cause of the problem
                raise ColliderDimensionError("A circle collider requires a radius parameter")
            self.radius = a
            if b != None:
                self.vel = b
            else:
                self.vel = Vector(0, 0)
        # initialize rectangle collider
        if self.shape == rect:
            if a == None or b == None:
                # if a rectangle collider is created without height and width it will cause errors later
                # so best to throw error here to show cause of the problem
                raise ColliderDimensionError("A rectangle collider requires height and width parameters")
            self.height = a
            self.width = b
            if c != None:
                self.vel = c
            else:
                self.vel = Vector(0, 0)
        self.collisionList = []

    def hit(self, collider):
        if self.shape == circ:
            if collider.shape == rect:
                return collider.hit(self)
            # collision between two circles
            return collider.pos.copy().subtract(self.pos).length() <= collider.radius + self.radius
        if self.shape == rect:
            if collider.shape == circ:
                # collision between circle and rectangle, this works like collisions between two rectangles, so might need to be improved
                return (collider.pos.x - self.pos.x <= collider.radius + self.width / 2) and (
                collider.pos.y - self.pos.y <= collider.radius + self.height / 2)
            # collision between two rectangles
            return (collider.pos.x - self.pos.x <= collider.width / 2 + self.width / 2) and (
            collider.pos.y - self.pos.y <= collider.height / 2 + self.height / 2)

    # collision tracking, should help with sticky problem, but must still be partially handled outside collider class
    def add_collision(self, collider):
        self.collisionList.append(collider)

    def in_collision(self, collider):
        return collider in self.collisionList

    def remove_collision(self, collider):
        self.collisionList.remove(collider)

    # two types of bounce for use with physics moving objects
    def bounceZeroMass(self, normal):
        self.vel.reflect(normal)

    def bounceMomentum(self, collider):
        connect = self.pos.copy().subtract(collider.pos)

        normal = connect.copy().normalize()
        v1_par = self.vel.get_proj(normal)
        v1_perp = self.vel.copy().subtract(v1_par)
        v2_par = collider.getVel().get_proj(normal)
        v2_perp = collider.getVel().copy().subtract(v2_par)

        self.vel = v2_par + v1_perp
        collider.setVel(v1_par + v2_perp)

    def getVel(self):
        return self.vel

    def setVel(self, vel):
        self.vel = vel