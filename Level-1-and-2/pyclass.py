

class Person(object):

    def __init__(self, n , a):
        self.name = n
        self.age = a

    def is_adult(self):
        if (self.age >= 18):
                a = True
        else:
                a = False

        return a

#main
a = Person("anv", 18)
m = Person("manju", 12)

print a.is_adult()
print m.is_adult()

s = " hi there"
