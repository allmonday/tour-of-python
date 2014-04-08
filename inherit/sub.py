class Father(object):
    '''father class'''
    def __init__(self, name):
        '''init'''
        self.name = name

    def sayName(self):
        return self.name


class Child(Father):
    def __init__(self, name, age):
        Father.__init__(self, name)
        self.age = age

    def sayName(self):
        return self.name, self.age


if __name__ == "__main__":
    c = Child('xiaoming', 21)
    print "%s, %s" % c.sayName()
    f = Father('wang')
    print f.sayName()
    print 'is subclass(Child, Father):', issubclass(Child, Father)
    print 'is instance(c, Child):', isinstance(c, Child)
    print 'is instance(c, Father):', isinstance(c, Father)
