# MST 알고리즘

from heapq import heappush, heappop

INF = 1e10


def prim(G, s):
    N = len(G)
    visited = [False] * N

    que = []
    heappush(que, (0, s))
    for i in range(N):
        if i == s:
            continue
        heappush(que, (INF, i))

    while que:
        _, m_idx = heappop(que)
        visited[m_idx] = True

        temp = []
        while que:
            weight, adj_node = heappop(que)
            if not visited[adj_node] and G[m_idx][adj_node] != 0 and G[m_idx][adj_node] < weight:
                heappush(temp, (G[m_idx][adj_node], adj_node))
            else:
                heappush(temp, (weight, adj_node))
        que = temp



