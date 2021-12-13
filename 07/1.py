import numpy as np

# to get np.array of int
d = np.array([int(i) for i in str(np.loadtxt('input', dtype='str')).split(',')])
l, h, f0 = min(d), max(d),[]

for i in range(h-l):
    f1= []
    for j in d:
        f1.append(abs(j-i))
    f0.append(sum(f1))


print(min(f0))






