import numpy as np

def parse(inp):
    a, b = [], []
    with open(inp) as file:
        for i, line in enumerate(file):
            line0 = line.rstrip().split()
            l = line0.index('|')
            a += line0[:l]
            b += line0[l+1:]
    return a, b

inp0 = 'input'
a0, b0 = parse(inp0)

print(sum([1 for i in b0 if len(i) in (2, 3, 4, 7)]))
