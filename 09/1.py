import numpy as np

d = np.loadtxt('input0', dtype='str')
l0, dx_len, dy_len = [], len(d[0]), len(d)

dic_x = {0: 3, dx_len-1: 2}
dic_y = {0: 1, dy_len-1: 0}
tup_l = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def smart(x, y):
    l1 = [(y+i, x+j) for i, j in tup_l]
    tup0 = (dic_y.get(y, None), dic_x.get(x, None))
    return [l1[i] for i in range(len(l1)) if i not in tup0]


xy_grid = [(y, x) for x in range(dx_len) for y in range(dy_len)]
for y, x in xy_grid:
    l2 = smart(x, y)
    if all(d[y][x] < np.array([d[i][j] for i, j in l2])):
        l0.append((x, y, int(d[y][x])))

print(len(l0))
print(sum([i[2] + 1 for i in l0]))
