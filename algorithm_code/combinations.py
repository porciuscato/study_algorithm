from itertools import combinations


def combination(origin, aim, array: list=[], depth=0, last=0):
    if depth == aim:
        pass
        # print(array)
    else:
        for i in range(last, len(origin)):
            arr = array[:]
            arr.append(origin[i])
            combination(origin, aim, arr, depth + 1, i + 1)

import time


some = [i for i in range(22)]


start = time.time()
combination(some, 11)
print(time.time() - start)
start = time.time()
for i in combinations(some, 11):
    pass
print(time.time() - start)


# 라이브러리가 월등히 빠르다.
