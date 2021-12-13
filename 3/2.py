import numpy as np

d = list(np.loadtxt('input', dtype='str'))
l0 = len(d[0])
p1 = []

for i in range(l0):
    if len(d)==1:
        p2 = d[0]
        break
    c = [j[i] for j in d]
    pick = '1' if c.count('1') >= c.count('0')  else '0'
    p1.append(pick)
    for j in reversed(range(len(c))):
        if c[j] != pick:
            d.pop(j)

d = list(np.loadtxt('input', dtype='str'))
l0 = len(d[0])
p2 = []

for i in range(l0):
    if len(d)==1:
        p2 = d[0]
        break
    c = [j[i] for j in d]
    pick = '0' if c.count('1') >= c.count('0') else '1'
    p2.append(pick)
    for j in reversed(range(len(c))):
        if c[j] != pick:
            d.pop(j)

print(''.join(p1), int(''.join(p1),2))
print(p2, int(''.join(p2),2))
print(int(''.join(p1),2)*int(''.join(p2),2))
