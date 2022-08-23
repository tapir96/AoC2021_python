
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

        if len(path) == 6 and path[2] == 'b' and 'c' in path and 'A' in path:
            print('--- bogi 1 ---')
            print(path, route, routes)
            print(small)
            print(route.islower(), 2 in small.values(), small[route] in (1, 2))
            print(route.islower() and 2 in small.values() and small[route] in (1, 2))
            print('--- bogi 2 ---')

        if route.islower() and 2 in small.values() and small[route] in (1, 2):
            continue
        
        elif route.islower() and route not in ('start', 'end'):
            if small[route] == 2:
                print(' ---- ')
                print(path, route)
                print('small', small)
                print(route.islower(), 2 in small.values(), route in small.keys(), small[route] != 2)
                print(route in small.keys(), path, list(small.keys()))
                print(' ---- ')
                exit('z')
            small[route] += 1

        if sum(['b'== kk for kk in path]) == 2 and route == 'b':
            print(' ---- ')
            print(path, route)
            print('small', small)
            print(route.islower(), 2 in small.values(), route in small.keys(), small[route] != 2)
            print(route in small.keys(), path, list(small.keys()))
            print(' ---- ')
            exit('hike')
        paths.append(path + [route])
        if len(path) == 6 and path[2] == 'c' and 'b' in path and 'A' in path:
            print(path + [route])
            print('--- bogi 3 ---')

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
    for zzz in paths2:
        print(','.join(zzz))
    for idx, path in enumerate(paths2):
        if 'end' in path:
            paths.append(path)
    paths0 = paths2
    paths2 = []

    counter += 1
    if counter == 14:
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
