from vector import Vector


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
            if collider.shape == circ:
                h = (
                (collider.pos.x - collider.radius <= self.pos.x) and (collider.pos.x + collider.radius >= self.pos.x))
            elif collider.shape == rect:
                h = ((collider.pos.x - collider.width / 2 <= self.pos.x) and (
                collider.pos.x + collider.width / 2 >= self.pos.x))
        # a horizontal wall hits things passing from top to bottom and vice versa
        elif self.ori == "h":
            if collider.shape == circ:
                h = (
                (collider.pos.y - collider.radius <= self.pos.y) and (collider.pos.y + collider.radius >= self.pos.y))
            elif collider.shape == rect:
                h = ((collider.pos.y - collider.height / 2 <= self.pos.y) and (
                collider.pos.y + collider.height / 2 >= self.pos.y))
        return h
