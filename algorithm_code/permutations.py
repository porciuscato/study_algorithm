from itertools import permutations
from time import time


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


SIZE = 15
chosen = 6

some = [i for i in range(SIZE)]

start = time()
permutation(some, chosen)
print(time() - start)

start = time()
for i in permutations(some, chosen):
    pass
print(time() - start)
