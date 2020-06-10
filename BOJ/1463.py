from collections import deque


def main():
    N = int(input())
    visited = [False] * 1000001
    que = deque([])
    que.append((1, 0))
    visited[1] = True
    while que:
        first, _count = que.popleft()
        if first == N:
            return _count
        for ele in [first + 1, first * 2, first * 3]:
            if ele <= 1000000 and not visited[ele]:
                visited[ele] = True
                que.append((ele, _count + 1))


print(main())
