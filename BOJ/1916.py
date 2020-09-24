import sys
import heapq

input = sys.stdin.readline


INF = 10 ** 10


def dijkstra(route, s):
    distance = [INF] * N
    distance[s] = 0
    que = []
    heapq.heappush(que, (distance[s], s))
    while que:
        until_now_distance, node = heapq.heappop(que)
        if until_now_distance <= distance[node]:
            for adj, cost in route[node]:
                new_distance = until_now_distance + cost
                if new_distance < distance[adj]:
                    distance[adj] = new_distance
                    heapq.heappush(que, (new_distance, adj))
    return distance


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    route_map = [[] for _ in range(N)]

    for _ in range(M):
        s, e, w = map(int, input().split())
        route_map[s - 1].append([e - 1, w])

    depart, arrive = map(lambda x: x - 1, (map(int, input().split())))
    distances = dijkstra(route_map, depart)

    print(distances[arrive])
