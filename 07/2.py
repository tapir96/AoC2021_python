import numpy as np

# to get np.array of int
d = np.array([int(i) for i in str(np.loadtxt('input', dtype='str')).split(',')])
f0, arr = [], np.cumsum(range(max(d)-min(d)+1))

for i in range(len(arr)):
    f1 = [arr[abs(j-i)] for j in d]
    f0.append(sum(f1))

print(min(f0))






