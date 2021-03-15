class Clock:
  time = 0

  @classmethod
  def tick(cls):
    cls.time += 1

  @classmethod
  def transition(cls, frame_duration):
    if cls.time % frame_duration == 0:
      return True
    else:
      return False