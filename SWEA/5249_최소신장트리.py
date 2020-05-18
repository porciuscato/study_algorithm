import sys

sys.stdin = open('5249.txt', 'r')

for T in range(1, int(input()) + 1):
    answer = 0
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V + 1)] for __ in range(V + 1)]
    for edge in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2], graph[n2][n1] = w, w

    visited = [0] * (V + 1)
    weigths = [1e9] * (V + 1)
    weigths[0] = 0

    for _ in range(V + 1):
        # 선별
        mn = 1e9
        m_idx = -1
        for i in range(V + 1):
            if not visited[i] and weigths[i] < mn:
                mn = weigths[i]
                m_idx = i
        visited[m_idx] = True
        answer += mn
        # 가중치 초기화
        for idx, value in enumerate(graph[m_idx]):
            if not visited[idx] and 0 < value < weigths[idx]:
                weigths[idx] = value

    print('#{} {}'.format(T, answer))
