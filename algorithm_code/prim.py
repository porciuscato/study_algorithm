# MST 알고리즘

INF = 1e10


def prim(G, s):                     # G: 그래프, s: 시작 정점
    N = len(G)
    weights = [1e9] * N             # 가중치 그래프를 무한대로 초기화
    parents = [None] * N            # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N           # 방문여부 초기화
    weights[s] = 0                  # 시작 정점의 가중치를 0으로 설정

    for _ in range(N):              # 정점의 수만큼 반복
        mn = 1e9
        m_idx = -1

        # 선별
        for idx in range(N):        # 방문 안 한 정점중 최소 가중치 정점 찾기
            if not visited[idx] and weights[idx] < mn:
                mn = weights[idx]
                m_idx = idx
        visited[m_idx] = True       # 최소 가중치 정점 방문처리

        # 가중치 업데이트
        for i in range(N):          # 선택 정점의 인접한 정점
            if not visited[i] and G[m_idx][i] != 0 and G[m_idx][i] < weights[i]:
                weights[i] = G[m_idx][i]
                parents[i] = m_idx  # 트리에서 연결될 부모 정점
