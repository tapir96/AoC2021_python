import numpy as np

def parse(inp):
    boards, board = [], []
    with open(inp) as file:
        for i, line in enumerate(file):
            if i == 0:
               arr = [int(i) for i in line.split(',')] 
            elif i != 0 and line != '\n':
                board.extend([int(i) for i in line.rstrip().split()])
                if len(board) == 25:
                    boards.append(board)
                    board = []
    return arr, boards

def checker(arr0, board):
    x, y, z = np.zeros(5), np.zeros(5), []
    for i, j in enumerate(arr0):
        if j in board:
            z.append(j)
            idx = board.index(j)
            a = idx % 5
            b = int((idx-a)/5)
            x[a]+=1
            y[b]+=1
        if 5 in x or 5 in y:
            c = [i for i in board if i not in z]
            print(i, j, j*sum(c))
            return i, j, j*sum(c)

arr0, boards0 = parse('input0')
l = []
for i, j in enumerate(boards0):
    a, b, c = checker(arr0, j)
    l.append(a)
print(np.argmin(l))




    
