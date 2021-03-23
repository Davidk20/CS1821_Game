from source.spritesheet import Spritesheet
from source.collider import PickupCollider
from source.stats import PickupStats
from source.vector import Vector

class HealthPickup(PickupCollider, PickupStats):
    def __init__(self, pos):
        PickupCollider.__init__(self, pos)
        PickupStats.__init__(self)
        self.pos = pos
        self.sprite = Spritesheet("source/images/heart_pickup.png", 1, 1)


    def draw(self, canvas):
        self.sprite.draw(canvas, self.pos)

class BonusPickup(PickupCollider, PickupStats):
    def __init__(self, pos, bonusMul):
        PickupCollider.__init__(self, pos)
        PickupStats.__init__(self, bonusMul)
        self.pos = pos
        self.sprite = Spritesheet("source/images/crystal.png", 1, 1)

    def draw(self, canvas):
        self.sprite.draw(canvas, self.pos)