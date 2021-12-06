import numpy as np

d = np.loadtxt('input0', dtype='str')
l0, l1, k = len(d[0]), len(d), ''.join(d)
o = ['1' if k[i::l0].count('1') > l1/2 else '0' for i in range(l0)]

print(int(''.join([str(int(i)^1) for i in o]),2)*int(''.join(o),2))


