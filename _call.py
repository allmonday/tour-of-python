class Entity:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y


e = Entity(2, 3)
e(4, 5)
print e.x, e.y
