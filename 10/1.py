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

for i in d:
    i_mod = ['*' if l_bra.get(i[x]) == i[x+1] else y for x, y in enumerate(i[:-1])]
    i_mod += [i[-1]]
    for j in reversed(range(len(i_mod[:-1]))):
        if i_mod[j] == '*':
            i_mod[j+1] = '*'
        
    print(i)
    print(''.join(i_mod))
    exit('a')
    #i_mod = [[x if x [in range(len(i))[::2]]

#for i, j in enumerate(d):
#    a = [dic_b[k] for k in j]
#    print(a)
#    print(j)
#    j_mod = [y if a[x+1]-a[x] != 1 else '*' for x, y in enumerate(j[:-1])]
#    zappa = []
#    for x, y in enumerate(j[:-1]):
#        print('a', a[x+1]-a[x])
#        #if a[x+1]-a[x] 
#    print(''.join(j_mod))
#    #j_mod = [k if 
#    #j_mod = [k for k in j[:-1] if a[i+1]-a[i] != 0 else '*']
#    exit('a')
    #j_mod = [k for k in j[:-1] if a[i+1]-a[i] != 0 else '*']

    
#    a = [dic_b[j] for j in i]
#    odd, eve = [], []
#    for k, j in enumerate(a):
#        if j%2 == 1:
#            odd.append(j)
#        else:
#            eve.append(j)
#        if j%2 == 1:
#            odd_c = odd.count(j)
#            eve_c = eve.count(j-1)
#            print(i[:len(odd+eve)], len(odd+eve))
#            print(set(odd), i[k], odd_c, eve_c)
#            print(' ')
#            if odd_c > eve_c:
#                print('nani2!')
#                exit('zoya')

#        for k in set(odd):
#            odd_c = odd.count(k)
#            eve_c = eve.count(k-1)
#            print(i[:len(odd+eve)], len(odd+eve))
#            print(set(odd), k, odd_c, eve_c)
#            print(' ')
#            if odd_c > eve_c:
#                print('nani2!')
#                exit('zoya')
#        print('zap')
#        print(eve)
#        print(odd)

#        if len(odd)>len(eve):
#            print('nani!')
#            exit('oya')
#    print(i)
#    print(a)
#    print(' ')
#    print(len(i))
#    print(len(eve), len(odd))
#
#    exit()


# at a certain idx, count of of
