import numpy as np

d = np.loadtxt('input', dtype='str')
dic0 = {'up': -1, 'down': 1}
dic1 = {'horizonal': 0, 'depth': 0, 'aim': 0,}
for i in d:
    if i[0] == 'forward':
        dic1['horizonal'] += int(i[1])
        dic1['depth'] += dic1['aim']*int(i[1])
    else:
        dic1['aim'] += int(i[1])*dic0[i[0]]

print(dic1['horizonal'], dic1['depth'], dic1['horizonal']*dic1['depth'])


