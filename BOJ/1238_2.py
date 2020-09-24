import sys
import heapq

input = sys.stdin.readline


INF = 10 ** 10


def dijkstra(s):
    distance = [INF] * N
    distance[s] = 0

    que = []
    heapq.heappush(que, (distance[s], s))
    while que:
        until_now, current_city = heapq.heappop(que)
        if until_now <= distance[current_city]:
            for next_city, time in roads[current_city]:
                will_take = until_now + time
                if will_take < distance[next_city]:
                    distance[next_city] = will_take
                    heapq.heappush(que, (will_take, next_city))
    return distance


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    roads = [[] for _ in range(N)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        roads[s - 1].append([e - 1, t])

    taken_times = dijkstra(X - 1)
    for n in range(N):
        a = dijkstra(n)
        print(a)
        taken_times[n] += dijkstra(n)[X - 1]

    print(max(taken_times))
