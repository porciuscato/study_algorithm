def solution(n, costs):
    graph = [[0] * n for _ in range(n)]
    for s, e, w in costs:
        graph[s][e] = w
        graph[e][s] = w

    # prim
    weights = [1e10] * n
    visited = [False] * n
    weights[0] = 0

    for _ in range(n):
        mn = 1e9
        m_idx = -1
        for i in range(n):
            if not visited[i] and weights[i] < mn:
                mn = weights[i]
                m_idx = i
        visited[m_idx] = True

        for j in range(n):
            if not visited[j] and 0 < graph[m_idx][j] + mn < weights[j]:
                weights[j] = graph[m_idx][j] + mn

    return sum(weights)


cases = [
    (4, [[0, 1, 1], [0, 2, 7], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
]

for c in cases:
    print(solution(*c))
