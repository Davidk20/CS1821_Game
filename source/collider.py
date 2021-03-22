from source.vector import Vector


class ColliderDimensionError(Exception):
    pass


class Collider:
    def __init__(self, shape, pos, a=None, b=None, c=None):
        self.shape = shape
        self.pos = pos
        # initialize circle collider
        if self.shape == "circ":
            if a == None:
                # if a circle collider is created without radius it will cause errors later
                # so best to throw error here to show cause of the problem
                raise ColliderDimensionError("A circle collider requires a radius parameter")
            self.radius = a
            if bool(b):
                self.vel = b
            else:
                self.vel = Vector(0, 0)
        # initialize rectangle collider
        if self.shape == "rect":
            if a == None or b == None:
                # if a rectangle collider is created without height and width it will cause errors later
                # so best to throw error here to show cause of the problem
                raise ColliderDimensionError("A rectangle collider requires height and width parameters")
            self.height = a
            self.width = b
            if bool(c):
                self.vel = c
            else:
                self.vel = Vector(0, 0)
        self.collisionList = []

    def hit(self, collider):
        # collisions with walls are handled by the wall, this allows .hit() to be called on colliders with wall colliders without writing the wall collision code in the regular collider as well
        if collider.shape == "wall":
            return collider.hit(self)
        if self.shape == "circ":
            if collider.shape == "rect":
                return collider.hit(self)
            # collision between two circles
            return collider.pos.copy().subtract(self.pos).length() <= collider.radius + self.radius
        if self.shape == "rect":
            if collider.shape == "circ":
                # collision between circle and rectangle, this works like collisions between two rectangles, so might need to be improved
                return (abs(collider.pos.x - self.pos.x) <= collider.radius + self.width / 2) and (
                abs(collider.pos.y - self.pos.y) <= collider.radius + self.height / 2)
            # collision between two rectangles
            return (abs(collider.pos.x - self.pos.x) <= collider.width / 2 + self.width / 2) and (
            abs(collider.pos.y - self.pos.y) <= collider.height / 2 + self.height / 2)

    # collision tracking, should help with sticky problem, but must still be partially handled outside collider class
    def add_collision(self, collider):
        self.collisionList.append(collider)

    def in_collision(self, collider):
        return collider in self.collisionList

    def remove_collision(self, collider):
        self.collisionList.remove(collider)

    # two types of bounce for use with physics moving objects
    def bounceZeroMass(self, collider):
        if collider.shape == "wall":
            self.vel.reflect(collider.normal)
        else:
            self.vel.reflect(self.pos.copy().subtract(collider.pos).normalize())

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

class SpriteCollider(Collider):
    
    def __init__(self, pos, movement):
        Collider.__init__(self, "circ", pos, 16, Vector(0, 0))
        self.movement = movement
    
    def bounceSprite(self, collider):
        if collider.shape == "wall":
            self.movement.vel_vector.add(collider.normal.copy().multiply(self.movement.speed))
        elif collider.shape == "circ":
            self.movement.vel_vector.add(self.pos.copy().subtract(collider.pos).normalize().multiply(self.movement.speed))
        elif collider.shape == "rect":
            normal = self.pos.copy().subtract(collider.pos).normalize()
            if abs(normal.x) > abs(normal.y):
                normal = Vector(normal.x, 0).normalize()
            else:
                normal = Vector(0, normal.y).normalize()
            self.movement.vel_vector.add(normal.multiply(self.movement.speed * 5))


class WallCollider:
    def __init__(self, pos, ori):
        self.pos = pos
        self.ori = ori
        self.shape = "wall"

        # use "v" to specify a vertical wall, and "h" to specify a horizontal wall
        if self.ori == "v":
            self.normal = Vector(1, 0)
        elif self.ori == "h":
            self.normal = Vector(0, 1)

    def hit(self, collider):
        # a vertical wall hits things passing from left to right and vice versa
        if self.ori == "v":
            if collider.shape == "circ":
                h = (
                (collider.pos.x - collider.radius <= self.pos.x) and (collider.pos.x + collider.radius >= self.pos.x))
            elif collider.shape == "rect":
                h = ((collider.pos.x - collider.width / 2 <= self.pos.x) and (
                collider.pos.x + collider.width / 2 >= self.pos.x))
        # a horizontal wall hits things passing from top to bottom and vice versa
        elif self.ori == "h":
            if collider.shape == "circ":
                h = (
                (collider.pos.y - collider.radius <= self.pos.y) and (collider.pos.y + collider.radius >= self.pos.y))
            elif collider.shape == "rect":
                h = ((collider.pos.y - collider.height / 2 <= self.pos.y) and (
                collider.pos.y + collider.height / 2 >= self.pos.y))
        return h