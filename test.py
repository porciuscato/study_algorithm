# prim algorithm

# 그래프 정보가 주어졌을 때, 모든 정점들을 잇는, 미니멈 스패닝 트리를 작성하려면?

# 가중치 -> 매번 특정 정점과 연결된 노드들의 가중치를 갱신해야 한다.
# 방문 여부
# 부모 표시

def PRIM(G, s):
    # G는 그래프, s는 시작 정점
    N = len(G)
    visited = [False] * N
    parents = [None] * N
    weigths = [1e9] * N
    weigths[s] = 0

    # 선별 -> 아직 방문하지 않았으면서 가중치 최소인 거
    for _ in range(N): # 정점의 개수만큼 반복
        min = 1e9
        m_idx = -1
        for i in range(N):
            if not visited[i] and weigths[i] < min:
                min = weigths[i]
                m_idx = i
        visited[m_idx] = True

        # 가중치 업데이트
        for idx, value in enumerate(G[m_idx]):
            if not visited[idx] and value < weigths[idx]:
                weigths = value
                parents[idx] = m_idx
