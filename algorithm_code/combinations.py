from itertools import combinations
from time import time

some = [i for i in range(22)]


def combination(origin, aim, array: list=[], depth=0, last=0):
    if depth == aim:
        pass
    else:
        for i in range(last, len(origin)):
            arr = array[:]
            arr.append(origin[i])
            combination(origin, aim, arr, depth + 1, i + 1)


start = time()
combination(some, 11)
print(time() - start)
start = time()
for i in combinations(some, 11):
    pass
print(time() - start)

