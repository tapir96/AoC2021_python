import numpy as np

d, b = np.loadtxt('input0', dtype='str'), []
for i in d: b.extend(list(map(int, [i[0][0], i[0][2], i[2][0], i[2][2]])))
x_p, x_m, y_p, y_m = max(b[0::2]), min(b[0::2]), max(b[1::2]), min(b[1::2])
tab = np.zeros((1+x_p-x_m)*(1+y_p-y_m))

for i in range(int(len(b)/4)):
    vec, l = [b[j+i*4] for j in range(4)], []     # b[0], b[0], b[0], b[0]
    if not vec[2]-vec[0]:
        l = [(vec[0], j) for j in range(min(vec[1::2]), max(vec[1::2])+1)]
    elif not vec[3]-vec[1]:
        l = [(j, vec[1]) for j in range(min(vec[0::2]), max(vec[0::2])+1)]
    for j in l:
        print(j)
        tab[j[0] + j[1]*(x_p-x_m)] += 1

    #la = range(vec[2]
    

    #l = [(f, k) for f                                   # generate a set of x y values..
# idx: x + y*(x_p-x_m)
#print(x_p, x_m, y_p, y_m, tab)
print(b)
print(tab)
print(sum(max(tab)==tab))






#print(max(b[0::2]))
#print(max(b[1::2]))
#print(b[0::2])
#print(b[1::2])

