import pickle


#class MyClass(object):
#    def __init__(self):
#        self.foo = 'hi'


MyClass = pickle.load(open("MyClass.pickle", 'r'))
print type(MyClass)
#pickle.dump(MyClass, open('MyClass.pickle', 'w'))
#A = MyClass
#mya = A()
#print mya.foo

#myc = pickle.load(open('myc.pickle', 'r'))
#print myc.foo
