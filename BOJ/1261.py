import sys
import heapq

input = sys.stdin.readline


INF = 10 ** 10
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def dijkstra(row, col):
    distance = [[INF] * COL for _ in range(ROW)]
    distance[row][col] = 0

    que = []
    heapq.heappush(que, (0, row, col))
    while que:
        until_now, r, c = heapq.heappop(que)
        if until_now <= distance[r][c]:
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROW and 0 <= nc < COL:
                    new_cost = until_now + maze[nr][nc]
                    if new_cost < distance[nr][nc]:
                        distance[nr][nc] = new_cost
                        heapq.heappush(que, (new_cost, nr, nc))
    return distance


if __name__ == "__main__":
    COL, ROW = map(int, input().split())
    maze = [list(map(int, list(input()[:-1]))) for _ in range(ROW)]
    distances = dijkstra(0, 0)
    print(distances[ROW - 1][COL - 1])
