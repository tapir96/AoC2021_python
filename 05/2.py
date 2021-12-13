import numpy as np

d, b = np.loadtxt('input', dtype='str'), []
for i in d: b.extend(list(map(int, i[0].split(',') + i[2].split(','))))
x_p, x_m, y_p, y_m = max(b[0::2]), min(b[0::2]), max(b[1::2]), min(b[1::2])
tab, d_x = np.zeros((1+x_p-x_m)*(1+y_p-y_m)), x_p-x_m

for i in range(int(len(b)/4)):
    vec, l = [b[j+i*4] for j in range(4)], []
    a = [vec[2]-vec[0], vec[3]-vec[1]]
    c = [0 if j == 0 else int(j/abs(j)) for j in a]
    for j in range(max(abs(np.array(a)))+1):
        l.append((vec[0]+j*c[0], vec[1]+j*c[1]))
    for j in l:
        tab[j[0]-x_m + (j[1]-y_m)*d_x] += 1

print(sum(np.array(tab)>=2))

