import numpy as np

d, b = np.loadtxt('input', dtype='str'), []
for i in d: b.extend(list(map(int, i[0].split(',') + i[2].split(','))))
x_p, x_m, y_p, y_m = max(b[0::2]), min(b[0::2]), max(b[1::2]), min(b[1::2])
tab = np.zeros((1+x_p-x_m)*(1+y_p-y_m))
print(x_p-x_m, y_p-y_m)

for i in range(int(len(b)/4)):
    vec, l = [b[j+i*4] for j in range(4)], []     # b[0], b[0], b[0], b[0]

    if not vec[2]-vec[0]:
        l = [(vec[0], j) for j in range(min(vec[1::2]), max(vec[1::2])+1)]
    elif not vec[3]-vec[1]:
        l = [(j, vec[1]) for j in range(min(vec[0::2]), max(vec[0::2])+1)]
    print(x_p, x_m, y_p, y_m, vec)
    for j in l:
        tab[j[0]-x_m + (j[1]-y_m)*(x_p-x_m)] += 1

print(sum(max(tab)==tab))

