import numpy as np

def cnt0(d):
    cnt = 0
    prv = d[0]
    cnt, prv = 0, d[0]
    z = 0
    for i in d[1:]:
        z += 1
        if i > prv:
            cnt += 1
#            print(d[z-1], d[z], i > prv, 'increased', cnt)
#        else:
#            print(d[z-1], d[z], i > prv, 'decreased', cnt)
        prv = i
    print(cnt)

d0 =np.loadtxt('input')
d1 =np.loadtxt('input0')
cnt0(d0)
print('-')
cnt0(d1)

o = np.loadtxt('input')
a = np.array([1,2,3,4,5])

k = [d0[i]>d0[i-1] for i in range(len(d0))[1:]]
print(sum(k))
print('-')
k = [d1[i]>d1[i-1] for i in range(len(d1))[1:]]
print(sum(k))

#d0[1:]-d0[:-1]

#print(a[1:])
#print(a[:-1])
#print(a[1:]>a[:-1])
print(a[1:]-a[:-1])
print(np.sum(np.diff(a)>0))
print(np.sum(np.diff(d0)>0))


