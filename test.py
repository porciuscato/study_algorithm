import random
from datetime import datetime


def merge(left, right):
    global m_count
    m_count += 1
    result = []
    llen = len(left)
    rlen = len(right)
    lp = rp = 0
    while lp < llen and rp < rlen:
        if left[lp] < right[rp]:
            result += [left[lp]]
            lp += 1
        else:
            result += [right[rp]]
            rp += 1
    if lp == llen:
        result += right[rp:rlen]
    else:
        result += left[lp:llen]
    return result


def merge_sort(L, R):
    global d_count
    d_count += 1
    if L == R - 1:
        return arr[L:R]
    else:
        M = (L + R) // 2
        left = merge_sort(L, M)
        right = merge_sort(M, R)
        return merge(left, right)


d_count = 0
m_count = 0
N = 10000000
arr = [random.randint(1, 1000000) for _ in range(N)]
# print(arr)
start = datetime.now()
arr = merge_sort(0, N)
print(datetime.now() - start)
print('count : {}, {}'.format(d_count, m_count))
# print(arr)
