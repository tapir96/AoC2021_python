import numpy as np

def parse(inp):
    a, b = [], []
    with open(inp) as file:
        for i, line in enumerate(file):
            line0 = line.rstrip().split()
            l = line0.index('|')
            a.append(line0[:l])
            b.append(line0[l+1:])
    return a, b

inp0 = 'input'
a0, b0 = parse(inp0)

       5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
num0 = {2: 1, 3: 7, 4: 4, 7: 8}
final = []

for i, j in zip(a0, b0):
    dic0 = {num0[len(k)] : k for k in i if len(k) in num0}
    l2 = [k for k in i if k not in dic0.values()]
    for k in i:
        if len(k) == 6:
            if set(dic0[4]) < set(k):
                dic0[9] = k
            elif set(dic0[1]) < set(k):
                dic0[0] = k
            else:
                dic0[6] = k
    for k in i:
        if len(k) == 5:
            if set(k) < set(dic0[6]):
                dic0[5] = k
            elif set(k) < set(dic0[9]):
                dic0[3] = k
            else: 
                dic0[2] = k
    print(dic0, len(dic0))
    print(j)
    print(dic0)
    dic1 = dict((''.join(sorted(v)),k) for k,v in dic0.items())
    print(' ')
    print(dic1)
    print([''.join(sorted(k)) for k in j])
    zowa = [str(k) for k in [dic1[''.join(sorted(k))] for k in j]]
    final.append(int(''.join(zowa)))
print(sum(final))

#print(sum([1 for i in b0 if len(i) in (2, 3, 4, 7)]))
