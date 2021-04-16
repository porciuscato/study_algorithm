# MST 알고리즘

from heapq import heappush, heappop
INF = 1e10


def prim(G, s):                     # G: 그래프, s: 시작 정점
    N = len(G)
    weights = [1e9] * N             # 가중치 그래프를 무한대로 초기화
    parents = [None] * N            # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N           # 방문여부 초기화
    weights[s] = 0                  # 시작 정점의 가중치를 0으로 설정

    que = []
    heappush(que, (weights[s], s))
    for i in range(N):
        if i == s:
            continue
        heappush(que, (weights[i], i))

    while que:
        _, m_idx = heappop(que)
        visited[m_idx] = True

        temp = []
        while que:
            weight, adj_node = heappop(que)
            if not visited[adj_node] and G[m_idx][adj_node] != 0 and G[m_idx][adj_node] < weight:
                weights[adj_node] = G[m_idx][adj_node]
                parents[adj_node] = m_idx   #  부모 노드를 찾기 위한 옵션.
            heappush(temp, (weights[adj_node], adj_node))
        que = temp



