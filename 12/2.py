
path_dic = {}
with open('./input0', 'r') as file:
    for line in file:
        start, end = line.strip().split('-')
        if not start in path_dic.keys():
            path_dic[start] = []
        if not end in path_dic.keys():
            path_dic[end] = []
        path_dic[start].append(end)
        path_dic[end].append(start)


def generate_paths(path_dic, path):
    paths = []

    if 'end' in path:
        return paths

    routes = path_dic[path[-1]]
    # small = {i: path.count(i) for i in path if i.islower()} 
    for route in routes:
        small = {i: path.count(i) for i in path if i.islower()} 
        if route not in small.keys():
            small[route] = 0
        if 'start' in route:
            continue
        if 'end' in route:
            paths.append(path + [route])
            continue


        if route.islower() and 2 in small.values() and small[route] in (1, 2):
            continue
        
        elif route.islower() and route not in ('start', 'end'):
            small[route] += 1

        paths.append(path + [route])

    return paths


paths0 = generate_paths(path_dic, ['start']) # start path
paths = []
paths2 = []
counter = 0
print(path_dic)
while paths0:
    for path in paths0:
        paths1 = generate_paths(path_dic, path)
        paths2 += paths1
    print('bang')
    for idx, path in enumerate(paths2):
        if 'end' in path:
            paths.append(path)
    paths0 = paths2
    paths2 = []

    counter += 1
    if counter == 18:
        print('               ')
        for path in paths:
            print(path)
        exit('haha')

print(' --------woh-------- ')
for path in paths:
    print(','.join(path))
print(len(paths))
exit('huh')
print(paths)
