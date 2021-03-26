class Clock:
  time = 0 # initial clock time

  @classmethod # class method, called the same way regardless of instance
  def tick(cls):  
    cls.time += 1 # increments class's time

  @classmethod # class method, called the same way regardless of instance
  def transition(cls, frame_duration):
    # used to check if a sufficient amount of time has passed

    if cls.time % frame_duration == 0:
      return True
    else:
      return False