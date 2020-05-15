import sys

sys.stdin = open('5247.txt', 'r')

from collections import deque


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = [False] * 1000001
    que = deque([(N, 0)])
    visited[N] = True
    Flag = True
    while que and Flag:
        value, chance = que.popleft()
        if value == M:
            answer = chance
            break
        for ele in [value + 1, value - 1, value * 2, value - 10]:
            if 0 < ele <= 1000000:
                if not visited[ele]:
                    que.append((ele, chance + 1))
                    visited[ele] = True
    print('#{} {}'.format(T, answer))
