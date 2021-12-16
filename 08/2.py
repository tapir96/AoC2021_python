"""Solution to exercise 08 AoC."""


def parse(inp):
    """Parse the input file."""
    a, b = [], []
    with open(inp) as file:
        for i, l in enumerate(file):
            l0 = [''.join(sorted(j)) for j in l.rstrip().split() if j != '|']
            a.append(l0[:10])
            b.append(l0[10:])
    return a, b


def calc(a0, b0):
    """Parse the input file."""
    num0, final = {2: '1', 3: '7', 4: '4', 7: '8'}, []
    for i, j in zip(a0, b0):
        dic0 = {num0[len(k)]: k for k in i if len(k) in num0}

        for k in [z for z in i if len(z) == 6]:
            if set(dic0['4']) < set(k):
                dic0['9'] = k
            elif set(dic0['1']) < set(k):
                dic0['0'] = k
            else:
                dic0['6'] = k
        for k in [z for z in i if len(z) == 5]:
            if set(k) < set(dic0['6']):
                dic0['5'] = k
            elif set(k) < set(dic0['9']):
                dic0['3'] = k
            else:
                dic0['2'] = k

        dic1 = dict((v, k) for k, v in dic0.items())
        final.append(''.join([dic1[k] for k in j]))

    print(sum([int(k) for k in final]))


a1, b1 = parse('input')
calc(a1, b1)
