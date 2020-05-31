def dijkstra(G, r):
    N = len(G)
    D = [1e9] * N
    P = [None] * N
    visited = [False] * N
    D[r] = 0

    for _ in range(N):
        mn = 1e9
        m_idx = -1
        for i in range(N):
            if not visited[i] and D[i] < mn:
                mn = D[i]
                m_idx = i
        visited[m_idx] = True

        for j in range(N):
            if not visited[j] and G[m_idx][j] != 0 and D[m_idx] + G[m_idx][j] < D[j]:
                D[j] = D[m_idx] + G[m_idx][j]
                P[j] = m_idx
