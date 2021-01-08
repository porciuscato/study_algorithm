import heapq


def dijkstra(G, s):
    N = len(G)
    distance = [1e9] * N
    distance[s] = 0

    que = []
    # 가중치와 노드 순서로 힙큐에 넣는 이유는 가중치 오름차순으로 정렬하기 위함이다.
    heapq.heappush(que, (distance[s], s))

    while que:
        distance_until_now, node = heapq.heappop(que)

        if distance_until_now > distance[node]:
            continue
        for adjacent, cost in G[node]:
            new_distance = distance_until_now + cost
            if new_distance < distance[adjacent]:
                distance[adjacent] = new_distance
                heapq.heappush(que, (new_distance, adjacent))