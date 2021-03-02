try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from movement import Movement

class EnemyMovement (Movement):
  def __init__(self, speed, pos_vector, patrol_points = None, target = None):
    super(speed, pos_vector)

    self.current_point = 0
    self.patrol_points = patrol_points
    self.target = target

  def move_towards_target(self, target):
    pass

  def patrol(self):
    pass