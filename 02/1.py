import numpy as np

d = np.loadtxt('input', dtype='str')
dic = {'forward': 0, 'up': 0, 'down': 0}
for i in d:
    dic[i[0]] += int(i[1])

print(dic['forward']*(dic['down']-dic['up']))


