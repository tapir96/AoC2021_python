
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
    for route in routes:
        if 'start' in route:
            continue
        if route.islower() and route in path:
            paths.append(path + [route] + ['end2'])
            continue
        else:
            paths.append(path + [route])

    return paths


# path = ['start'] # start path
paths0 = generate_paths(path_dic, ['start']) # start path
paths = []
paths2 = []
counter = 0
while paths0:
    # paths0 = generate_paths(path_dic, paths0)
    # print('0', paths0)
    for path in paths0:
        paths1 = generate_paths(path_dic, path)
        paths2 += paths1
    for idx, path in enumerate(paths2):
        if 'end' in path:
            paths.append(path)
    paths0 = paths2
    paths2 = []


    counter += 1
    # if counter == 11:
    #     for path in paths:
    #         print(path)
    #     exit('zo')


# for path in paths0:
#     paths1 = generate_paths(path_dic, path)
#     print(path)
#     print(paths1)
#     print(' ')
#     paths.append(paths1)

for path in paths:
    print(path)
print(len(paths))
exit('huh')
print(paths)


# print(paths)
# for i in range(10):
# 
# print(path_dic)
# paths = generate_paths(path_dic, start_path)
# print(paths)
# dummy = generate_paths(path_dic, paths[0])
# print(dummy)



