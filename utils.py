class Stopwatch():
  def __init__(self):
    from time import time, gmtime, strftime
    self.time = time
    self.gmtime = gmtime
    self.strftime = strftime
  
  def start(self, steps_nb):
    self.started_ = True
    self.start_ = self.time()
    self.steps_nb_ = steps_nb

  def stop(self):
    self.started_ = False
  
  def estimate(self, step):
    if self.started_:
      self.elapsed_ = self.time() - self.start_
      self.estimated_ = (self.elapsed_ * self.steps_nb_) / step
      self.remaining_ = self.estimated_ - self.elapsed_
      self.progression_ = (step * 100) / self.steps_nb_
  
  def time_str(self, seconds):
    return self.strftime("%H:%M:%S", self.gmtime(seconds))

  def info(self, step=None, update=True):
    if update:
      if step != None:
        self.estimate(step=step)
      else:
        print("ERROR: Missing current step number")
    
    print(f"Elapsed: {self.time_str(self.elapsed_)} | Remaining: {self.time_str(self.remaining_)} \t [{self.progression_:.2f}%]")
    