import numpy as np

d = np.loadtxt('input0', dtype='str')
l0, dx_len, dy_len = [], len(d[0]), len(d)

dic_x = {0: 1, dx_len-1: 0}
dic_y = {0: 3, dy_len-1: 2}

#    if x == 0:
#        l.pop(1)
#    elif x == dx_len-1:
#        l.pop(0)
#    if y == 0:
#        l.pop(3)
#    elif x == dy_len-1:
#        l.pop(2)

tup_l = [(1, 0), (-1, 0), (0,1), (0,-1)]

def smart(x,y):
    l = [(x+i, y+j) for i, j in tup_l]
    tup0 = (dic_x.get(x, None), dic_y.get(y, None))
    #print('yo',(dic_x.get(x, None), dic_y.get(y, None)))
    #print(l[i] for i in range(len(l)))
    return [l[i] for i in range(len(l)) if i not in tup0]

#    if any([i in (x, y) for i in (0, dx_len-1, dy_len-1)]):
#        if x == y:
#            l.append([(x + dic_c[x], y),
#                      (x, y + dic_c[y])
#                      (x + dic_c[x], y + dic_c[y])])
#
#            l.append([(x + dic_c[x], y),
#                      (x, y + dic_c[y])
#                      (x + dic_c[x], y + dic_c[y])])
#                      (x + dic_c[x], y + dic_c[y])])


xy_grid = [(x, y) for x in range(dx_len) for y in range(dy_len)]
for x, y in xy_grid:
    l1 = smart(x, y)
    print(x, y, l1, dx_len, dy_len)
    #print(d[l1[0][0],l1[0][1]])
    if all(d[x][y] < np.array([d[i][j] for i, j in l1])):
        l0.append((x, y, d[x][y]))


#for i in range(len(d)):
#    if i == 0:
#        for j in range(len(d[0])-2):
#            if all(d[i][j+1] < np.array([d[i+1][j+1], d[i][j], d[i][j+2]])):
#                l.append((i, j+1, d[i][j+1]))
#    elif i != len(d)-1:
#        for j in range(len(d[0])-2):
#            if all(d[i][j+1] < np.array([d[i+1][j+1], d[i-1][j+1],  d[i][j], d[i][j+2]])):
#                l.append((i, j+1, d[i][j+1]))
#    else:
#        for j in range(len(d[0])-2):
#            if all(d[i][j+1] < np.array([d[i-1][j+1], d[i][j], d[i][j+2]])):
#                l.append((i, j+1, d[i][j+1]))

print(l0)
            



