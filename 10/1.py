import numpy as np

d = np.loadtxt('input1', dtype='str')
brac = '()<>[]{}'
#brac_d = {brac[i] : brac[i+1] for i in range(len(brac))[::2]}
#brac_d.update({brac[i] : brac[i-1] for i in range(len(brac))[1::2]})
l_bra = {brac[i] : brac[i+1] for i in range(len(brac))[::2]}
r_bra = {brac[i] : brac[i-1] for i in range(len(brac))[1::2]}
#print(l_bra)
#print(brac_d)
#dic_b = {i[1]: i[0] for i in enumerate('()<>[]{}')}

#print(dic_b)

zopa = []
for i in d:
    i_mod = list(i)
    for j in range(int(len(i)/2)):
        for x, y in enumerate(i_mod[:-1-2*j]):
            if l_bra.get(y) == i_mod[x+1+2*j]:
                if i_mod[1+x:x+1+2*j].count('*') == len(i_mod[1+x:x+1+2*j]):
                    i_mod[x] = '*'
                    i_mod[x+1+2*j] = '*'
    for j in i_mod:
        if r_bra.get(j):
            zopa.append(j)
            break
#    print(i)
#    print(''.join(i_mod), zopa[-1], len(zopa))
#    print(' ')
#    exit('a')
#        print(i)
#        print(i_mod)
#        print(''.join(i_mod))
#        print(int(len(i)/2))
#        if k == 11:
#            exit('')
#    print(''.join(i_mod))
#    print(r_bra)
#    exit('-')

#    i_mod = ['*' if l_bra.get(i[x]) == i[x+1] else y for x, y in enumerate(i[:-1])]
#    i_mod += [i[-1]]
#    for j in reversed(range(len(i_mod[:-1]))):
#        if i_mod[j] == '*':
#            i_mod[j+1] = '*'
        
print(zopa)
#    print(i)
#    print(''.join(i_mod))
#    print(' ')
#    exit('a')
