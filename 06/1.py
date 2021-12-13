import numpy as np

# to get np.array of int
d = np.array([int(i) for i in str(np.loadtxt('input', dtype='str')).split(',')])
days, l = 256, [sum(d==i) for i in range(9)]

for i in range(days):
    l.append(l.pop(0))
    l[6] += l[-1]

print(sum(l))

