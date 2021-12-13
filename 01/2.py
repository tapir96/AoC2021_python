import numpy as np

d1, w = np.loadtxt('input'), 3
a = [sum(d1[i:i+w]) for i in range(len(d1[:-w+1]))]
print(np.sum(np.diff(a)>0))


