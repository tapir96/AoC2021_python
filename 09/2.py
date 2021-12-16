import numpy as np

d = np.loadtxt('input', dtype='str')
dx_len, dy_len = len(d[0]), len(d)

dic_x = {0: 3, dx_len-1: 2}
dic_y = {0: 1, dy_len-1: 0}
tup_l = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def smart(y, x):
    l1 = [(y+i, x+j) for i, j in tup_l]
    tup0 = (dic_y.get(y, None), dic_x.get(x, None))
    l2 = [l1[i] for i in range(len(l1)) if i not in tup0]
    return [(i, j, int(d[i][j])) for i, j in l2]


def get_bottom():
    l0 = []
    xy_grid = [(y, x) for x in range(dx_len) for y in range(dy_len)]
    for y, x in xy_grid:
        l2 = smart(y, x)
        if all(d[y][x] < np.array([d[i][j] for i, j, _ in l2])):
            l0.append((y, x, int(d[y][x])))

    return l0


def get_nines(t1, l_ext):
    l4 = []
    for i in t1:
        l4 += smart(i[0], i[1])
    l4 = [i for i in l4 if i[2] != 9]
    l4 = [i for i in l4 if i not in l_ext]
    l_ext += l4
    return list(set(l4)), list(set(l_ext))


def get_basin():
    l0, l1 = get_bottom(), []
    for t in l0:
        l2, l_ext = get_nines([t], [t])
        while l2:
            l2, l_ext = get_nines(l2, l_ext)
        l1.append(len(l_ext))
    l1_sort = sorted(l1)
    print(l1_sort[-1]*l1_sort[-2]*l1_sort[-3])


get_basin()
