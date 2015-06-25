def gen():
    r = 1
    while True:
        n = yield r
        if not n:
            return
        print n, r
        r = n + r

g = gen()
print g.next()
x = 1
while x < 5:
    r = g.send(x)
    # print r
    x += 1

g.close()
