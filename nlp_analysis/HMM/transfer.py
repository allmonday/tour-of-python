import numpy as np

t1 = np.array([1,2,3])
t2 = np.matrix([[1,2,4],[0,4,1],[2,4,1]])
t3 = np.matrix([[0,1,2,3],[1,4,3,2],[1,5,0,9]])

out = np.dot(np.dot(t1,t2), t3)
print(out)

