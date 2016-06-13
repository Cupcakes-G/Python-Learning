
class A(object):
  def __init__(self):
    self.b = 1
    self.c = 2
  def do_nothing(self):
    pass

a = A()
d = a.__dict__     # object to dictionary conversion
print d




