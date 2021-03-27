from heapq import heappush, heappop


def dijkstra(fare_matrix, distances, start):
    distances[start] = 0
    que = []
    heappush(que, (distances[start], start))

    while que:
        dis_until_now, pos = heappop(que)

        if dis_until_now > distances[pos]:
            continue
        for i in range(len(distances)):
            if fare_matrix[pos][i]:
                new_distance = dis_until_now + fare_matrix[pos][i]
                if new_distance < distances[i]:
                    distances[i] = new_distance
                    heappush(que, (new_distance, i))


def solution(n, s, a, b, fares):
    # 전처리
    fare_matrix = [[0 for _ in range(n)] for __ in range(n)]
    for fare in fares:
        depart, arrive, cost = fare
        fare_matrix[depart - 1][arrive - 1] = cost
        fare_matrix[arrive - 1][depart - 1] = cost

    # dijkstra
    min_distances = [[1e8 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        dijkstra(fare_matrix, min_distances[i], i)

    # 최단거리 계산
    answer = 1e8
    for i in range(n):
        answer = min(answer, min_distances[s - 1][i] + min_distances[i][a - 1] + min_distances[i][b - 1])
    return answer


cases = [
    (6, 4, 6, 2,
     [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]),
    (7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]),
    (6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]),
]

for case in cases:
    print(solution(*case))
