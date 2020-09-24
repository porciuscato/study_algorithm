import sys

input = sys.stdin.readline

MAX_VALUE = 1e9


def dijkstra(costs, start):
    distance = [MAX_VALUE] * V
    visited = [False] * V
    distance[start] = 0

    for _ in range(V):
        mn = MAX_VALUE
        m_idx = -1
        for i in range(V):
            if not visited[i] and distance[i] < mn:
                mn = distance[i]
                m_idx = i
        visited[m_idx] = True

        for e, w in costs[m_idx]:
            if not visited[e] and w + mn < distance[e]:
                distance[e] = w + mn
    return distance


if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    costs = [[] for _ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        costs[s - 1].append((e - 1, w))

    distances = dijkstra(costs, K - 1)
    for d in distances:
        if d != MAX_VALUE:
            print(d)
        else:
            print("INF")
