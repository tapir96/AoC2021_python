import numpy as np

# to get np.array of int
d = np.array([int(i) for i in str(np.loadtxt('input', dtype='str')).split(',')])
days = 256

l = [sum(d==i) for i in range(9)]
for i in range(days):
    temp = l.pop(0)
    l.append(temp)
    l[6] += temp

print(sum(l))

