class A(object):
    @classmethod
    def cm(cls):
        print 'caller of cm(cls):',cls.__name__
    @staticmethod
    def sm():
        print 'called static method'

class B(A):
    pass




