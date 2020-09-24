import sys
import heapq

input = sys.stdin.readline

MAX_VALUE = 1e9


def dijkstra(costs, start):
    distance = [MAX_VALUE] * V
    distance[start] = 0

    que = []
    heapq.heappush(que, (distance[start], start))
    while que:
        cur_distance, cur_node = heapq.heappop(que)
        if distance[cur_node] < cur_distance:
            continue
        for adj, w in costs[cur_node]:
            d = cur_distance + w
            if d < distance[adj]:
                distance[adj] = d
                heapq.heappush(que, (d, adj))
    return distance


if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    costs = [[] for _ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        costs[s - 1].append((e - 1, w))

    distances = dijkstra(costs, K - 1)
    print(costs)
    for d in distances:
        if d != MAX_VALUE:
            print(d)
        else:
            print("INF")
