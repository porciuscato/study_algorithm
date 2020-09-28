import sys
import heapq

input = sys.stdin.readline

INF = 10 ** 10


def dijkstra(s):
    shortest = [INF] * N
    shortest[s] = 0
    que = []
    heapq.heappush(que, (shortest[s], s))
    while que:
        until_now, node = heapq.heappop(que)
        if until_now <= shortest[node]:
            for adj_node, cost in routes[node]:
                new_cost = until_now + cost
                if new_cost < shortest[adj_node]:
                    shortest[adj_node] = new_cost
                    heapq.heappush(que, (new_cost, adj_node))
    return shortest


if __name__ == "__main__":
    N, E = map(int, input().split())
    routes = [[] for _ in range(N)]
    for _ in range(E):
        s, e, c = map(int, input().split())
        routes[s - 1].append((e - 1, c))
        routes[e - 1].append((s - 1, c))
    via1, via2 = map(lambda x: x - 1, map(int, input().split()))

    dij_0 = dijkstra(0)
    dij_v1 = dijkstra(via1)
    dij_v2 = dijkstra(via2)

    results1 = dij_0[via1] + dij_v1[via2] + dij_v2[N - 1]
    results2 = dij_0[via2] + dij_v2[via1] + dij_v1[N - 1]
    answer = min(results1, results2)

    if answer >= INF:
        print(-1)
    else:
        print(answer)
