import numpy as np

def parse(inp):
    a, b = [], []
    with open(inp) as file:
        for i, line in enumerate(file):
            line0 = line.rstrip().split()
            l = line0.index('|')
#            a += line0[:l]
#            b += line0[l+1:]
            a.append(line0[:l])
            b.append(line0[l+1:])
    return a, b

inp0 = 'input1'
a0, b0 = parse(inp0)

num = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 
       5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
# 2, 3, 5 : 5
# 0, 6, 9 : 6
num0 = {2: 1, 3: 7, 4: 4, 7: 8}
alp = ['abcdefg']
l1 = [0, 2, 3, 5, 6, 9]

for i, j in zip(a0, b0):
    dic0 = {num0[len(k)] : k for k in i if len(k) in num0}
    l2 = [k for k in i if k not in dic0.values()]
    for k in a0[0]:
        if len(k) == 6:
            if set(dic0[4]) < set(k):
                dic0[9] = k
            elif set(dic0[1]) < set(k):
                dic0[0] = k
            else:
                dic0[6] = k
    for k in a0[0]:
        if len(k) == 5:
            if set(k) < set(dic0[6]):
                dic0[5] = k
            elif set(k) < set(dic0[9]):
                dic0[3] = k
            else: 
                dic0[2] = k
    print(dic0, len(dic0))
    print(b0[0])
    print([dic0[k] for k in b0[0]])
    exit('a')

print(sum([1 for i in b0 if len(i) in (2, 3, 4, 7)]))
