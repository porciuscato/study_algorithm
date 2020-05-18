import sys

sys.stdin = open('1251.txt', 'r')

INF = 1e15

for T in range(1, int(input()) + 1):
    N = int(input())
    islands = []
    x = map(int, input().split())
    y = map(int, input().split())
    for cor in zip(x, y):
        islands.append(cor)
    RATE = float(input())

    graph = [[0] * N for _ in range(N)]
    for r in range(N - 1):
        x1, y1 = islands[r]
        for c in range(r + 1, N):
            x2, y2 = islands[c]
            cost = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * RATE
            graph[r][c], graph[c][r] = cost, cost

    # 프림 알고리즘
    visited = [False] * N
    weights = [INF] * N
    weights[0] = 0
    answer = 0
    for _ in range(N):
        mn = INF
        m_idx = -1
        for i in range(N):
            if not visited[i] and weights[i] < mn:
                mn = weights[i]
                m_idx = i
        visited[m_idx] = True
        answer += mn
        for idx, value in enumerate(graph[m_idx]):
            if not visited[idx] and value < weights[idx]:
                weights[idx] = value
    print('#{} {}'.format(T, round(answer)))
