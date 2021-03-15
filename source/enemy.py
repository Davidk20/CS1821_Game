try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from source.movement import Movement
from source.vector import Vector
from source.enemy_movement import EnemyMovement
from source.collider import Collider
from source.stats import EnemyStats



#TODO clean initialiser
class Enemy (Collider, EnemyStats):
    def __init__(self, radius, init_pos, target = None, patrol_points = None):
        Collider.__init__(self, "circ", Vector(init_pos[0],init_pos[1]), 16, Vector(0, 0))
        EnemyStats.__init__(self)
        self.image = simplegui._load_local_image("source/images/basic_enemy.png")
        self.pos = Vector(init_pos[0],init_pos[1]) #sets the initial position of the enemy.
        self.target = target
        self.patrol_points = patrol_points
        self.in_collision = False
        self.movement = EnemyMovement(self.speed, self.pos, target = self.target, patrol_points = self.patrol_points)

     #updates values regarding enemy position
    def update(self):
        self.movement.patrol() # patrols enemy between a set of points
        self.movement.update() # updates enemy position
        self.pos = self.movement.pos_vector

    #function to draw the enemy
    def draw(self, canvas):
        self.update()
        canvas.draw_image(
            self.image,
            (16,16),
            (32,32),
            self.pos.get_p(),
            (32,32)
        )


    def remove_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        return self.score
    