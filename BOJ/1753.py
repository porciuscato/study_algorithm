import sys

input = sys.stdin.readline

MAX_VALUE = 1e9


def dijkstra(costs):
    distance = [MAX_VALUE] * V
    visited = [False] * V
    distance[0] = 0

    for _ in range(V):
        mn = MAX_VALUE
        m_idx = -1
        for i in range(V):
            if not visited[i] and distance[i] < mn:
                mn = distance[i]
                m_idx = i
        visited[m_idx] = True

        for s, e, w in costs:
            if s == m_idx and not visited[e] and w + mn < distance[e]:
                distance[e] = w + mn
    return distance


if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    costs = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        costs.append((s - 1, e - 1, w))
    costs.sort(key=lambda x: x[0])

    distances = dijkstra(costs)
    for d in distances:
        if d != MAX_VALUE:
            print(d)
        else:
            print("INF")
