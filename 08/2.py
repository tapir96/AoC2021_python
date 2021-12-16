import numpy as np

def parse(inp):
    a, b = [], []
    with open(inp) as file:
        for i, line in enumerate(file):
            line0 = [''.join(sorted(j)) for j in line.rstrip().split() if j != '|' ]
            a.append(line0[:10])
            b.append(line0[10:])
    return a, b


def calc(a0, b0, num0):
    final = []
    for i, j in zip(a0, b0):
        dic0 = {num0[len(k)] : k for k in i if len(k) in num0}

        for k in [z for z in i if len(z)==6]:
            if set(dic0['4']) < set(k):
                dic0['9'] = k
            elif set(dic0['1']) < set(k):
                dic0['0'] = k
            else:
                dic0['6'] = k
        for k in [z for z in i if len(z)==5]:
            if set(k) < set(dic0['6']):
                dic0['5'] = k
            elif set(k) < set(dic0['9']):
                dic0['3'] = k
            else: 
                dic0['2'] = k

        dic1 = dict((v,k) for k,v in dic0.items())
        final.append(''.join([dic1[k] for k in j]))

    print(sum([int(k) for k in final]))

inp0, num1, final = 'input', {2: '1', 3: '7', 4: '4', 7: '8'}, []
a1, b1 = parse(inp0)
calc(a1, b1, num1)
