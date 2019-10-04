import sys
from datetime import datetime


def permu(depth, arr):
    if depth == M:
        return
    else:
        for i in range(N):
            if not v[i]:
                ar = arr[:]
                ar.append(i)
                v[i] = 1
                permu(depth + 1, ar)
                v[i] = 0


def combi(arr, depth, last):
    if depth == 5:
        return
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi(ar, depth + 1, i + 1)


N = 12
M = 6

start = datetime.now()
v = [0] * N
permu(0, [])
print('재귀 순열',datetime.now() - start)

start = datetime.now()
q = [(0, [])]  # depth, arr
while q:
    td, tarr = q.pop(0)
    if td == M:
        continue
    else:
        for i in range(N):
            
            if i not in tarr:
                ta = tarr[:]
                ta.append(i)
                q.append((td + 1, ta))
print('반복 순열',datetime.now() - start)

start = datetime.now()
combi([], 0, 0)
print('재귀 조합',datetime.now() - start)

start = datetime.now()
q = [(0, [], 0)]  # depth, arr
while q:
    td, tarr, tlast = q.pop(0)
    if td == M:
        continue
    else:
        for i in range(tlast, N):
            ta = tarr[:]
            ta.append(i)
            q.append((td + 1, ta, i + 1))
print('반복 조합',datetime.now() - start)
