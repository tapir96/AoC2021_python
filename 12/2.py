
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

    if 'end' in path or 'end2' in path:
        return paths

    routes = path_dic[path[-1]]
    small = {i: path.count(i) for i in path if i.islower()} 
    for route in routes:
        if 'start' in route:
            continue
        if 'end' in route:
            paths.append(path + [route])
            continue

        if route.islower() and 2 in small.values():
            print('wind', route, small)
            continue
        elif route.islower() and route not in ('start', 'end'):
            if route not in small.keys():
                small[route] = 0
            small[route] += 1
        # if route.islower() and route in path:
        #     paths.append(path + [route] + ['end2'])
        #     continue
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
    print(paths2)
    for idx, path in enumerate(paths2):
        if 'end' in path:
            print('fire', path)
            paths.append(path)
    paths0 = paths2
    paths2 = []

    counter += 1
    if counter == 9:
        print('               ')
        for path in paths:
            print(path)
        exit('haha')

print(' --------woh-------- ')
for path in paths:
    print(path)
print(len(paths))
exit('huh')
print(paths)
