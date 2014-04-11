import gl, a

CONSTANT = 0


def fun1():
    gl.gl_1 = 'Hello'
    gl.gl_2 = 'World'


def modifyConstant():
    global CONSTANT
    print CONSTANT
    CONSTANT += 1
    return

if __name__ == "__main__":
    modifyConstant()
    print CONSTANT
    fun1()
    a.hello_world()
