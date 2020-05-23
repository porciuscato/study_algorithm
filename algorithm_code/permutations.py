from itertools import permutations


def permutation(origin, aim, array=[], depth=0, visited=[]):
    if depth == 0:
        visited = [0] * len(origin)
    if depth == aim:
        pass
    else:
        for i in range(len(origin)):
            if not visited[i]:
                arr = array[:]
                arr.append(origin[i])
                visited[i] = 1
                permutation(origin, aim, arr, depth + 1, visited)
                visited[i] = 0

import time


SIZE = 15

some = [i for i in range(SIZE)]

start = time.time()
for i in permutations(some, SIZE // 2):
    pass
print(time.time() - start)
