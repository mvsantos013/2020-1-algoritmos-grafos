class Logger():
  def __init__(self, enabled=True):
    self.enabled = enabled

  def log(self, message):
    if(self.enabled):
      print(f'LOG (INFO): {message}')