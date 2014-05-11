def gen(l):
    for li in l:
        if type(li) == type('a'):
            yield 'string'
        elif type(li) == type(1):
            yield 'numeric'
        else:
            yield 'uh..'

mylist = ['a', 1, 'b' ,12]
for li in gen(mylist):
    print li
