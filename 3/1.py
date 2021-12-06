import numpy as np

d = np.loadtxt('input0', dtype='str')
l = len(d[0])
print(len(d))
k = ''.join(d)
o = ['1' if k[i::l].count('1') > len(d)/2 else '0' for i in range(l)]
#a = [int(not i) for i in o]
a = ['0' if i == '1' else '1' for i in o]
print(o)
print(a)

#print(int(int(a,2)*int(o,2))
print(int(''.join(a),2)*int(''.join(o),2))


#print(''.join(d))
