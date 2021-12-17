import numpy as np

d, bracs = np.loadtxt('input', dtype='str'), '()[]{}<>'
bra_d = {i[0]: i[1] for i in zip(bracs[0::2], [1, 2, 3, 4])}
l_bra = {bracs[i]: bracs[i+1] for i in range(len(bracs))[::2]}
r_bra = {v: k for k, v in l_bra.items()}

brac1, brac2 = [], []
for i in d:
    i_mod = list(i)
    for _ in range(len(i)):
        l_rm = []
        for x, y in enumerate(i_mod[:-1]):
            if l_bra.get(y) == i_mod[x+1]:
                l_rm += [x, x+1]
        i_mod = [i_mod[k] for k in range(len(i_mod)) if k not in l_rm]
        if not l_rm:
            if not [j for j in i_mod if j not in bracs[::2]]:
                ans = 0
                for j in reversed(''.join(i_mod)):
                    ans = ans*5 + bra_d.get(j, 0)
                brac1 += [ans]
            break

print(sorted(brac1)[int(len(brac1)/2)])

