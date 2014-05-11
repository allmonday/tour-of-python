import random
fl = open('expensive.txt','r').readlines()
sel_factor = int(len(fl)/ 10)
s100 = random.sample(fl, sel_factor)
open('expensive_test.txt','w').write(''.join(s100))

