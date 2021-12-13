import numpy as np

# to get np.array of int
d = np.array([int(i) for i in str(np.loadtxt('input', dtype='str')).split(',')])
l, h, f0 = min(d), max(d), []
arr = np.cumsum(range(h-l+1))

for i in range(h-l):
    f1 = [arr[abs(j-i)] for j in d]
    f0.append(sum(f1))

print(min(f0))






