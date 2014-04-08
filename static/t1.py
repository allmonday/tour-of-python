class TestStaticMethod:
    @staticmethod
    def foo():
        print 'calling staic method foo()'


class TestClassMethod:
    @classmethod
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__

if __name__ == '__main__':
    print TestClassMethod.foo()
    t = TestClassMethod()
    print t.foo()
