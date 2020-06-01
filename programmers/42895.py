from collections import deque


def solution(N, number):
    visited = deque([False] * 3200000)
    que = deque([(N, 1)])
    visited[N] = True
    while que:
        value, check = que.popleft()
        if check > 8:
            return -1
        if value == number:
            return check
        results = [
            int(str(value) + str(N)),
            value + N,
            value - N,
            value * N,
            value // N
        ]
        for result in results:
            if not visited[result]:
                if 0 < result < 320000:
                    que.append((result, check + 1))
                    visited[result] = True


problems = [
    (5, 12),
    (2, 11),
    (5, 31168),
    (8, 22312),
    (5, 26),  # 5 * 5 + 5 // 5
    (5, 624),
    (4, 17),  # 4 * 4 + 4 // 4 => 4개
    (4, 4)
]

for pro in problems:
    print(solution(*pro))

