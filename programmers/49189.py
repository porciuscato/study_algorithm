from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for p1, p2 in edge:
        graph[p1 - 1].append(p2 - 1)
        graph[p2 - 1].append(p1 - 1)

    answer = 0

    mx = 0
    que = deque([(0, 0)])
    visited[0] = True
    while que:
        node, distance = que.popleft()

        if distance > mx:
            mx = distance
            answer = 1
        elif distance == mx:
            answer += 1

        for adjacent in graph[node]:
            if not visited[adjacent]:
                visited[adjacent] = True
                que.append((adjacent, distance + 1))
    return answer


cases = [
    (6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),
]

for case in cases:
    print(solution(*case))
