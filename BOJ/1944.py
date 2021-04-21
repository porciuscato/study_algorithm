from heapq import heappush, heappop


def bfs(row, col, network):
    visited = [[False for _ in range(N)] for __ in range(N)]

    start = KEYS[row][col]
    que = [(row, col, 0)]
    visited[row][col] = True
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c, d = que[front]
        for dr, dc in ((0, -1), (-1, 0), (1, 0), (0, 1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N \
                    and board[nr][nc] != '1' \
                    and not visited[nr][nc]:
                que.append((nr, nc, d + 1))
                rear += 1
                visited[nr][nc] = True
                if board[nr][nc] in ['S', 'K']:
                    end = KEYS[nr][nc]
                    network[start][end] = d + 1
                    network[end][start] = d + 1


def prim(graph) -> int:
    distances = [MAX for _ in range(M + 1)]
    visited = [False for _ in range(M + 1)]
    distances[0] = 0

    que = [(0, 0)]

    while que:
        _, m_idx = heappop(que)
        visited[m_idx] = True

        for node in range(M + 1):
            if not visited[node] and graph[m_idx][node] != 0 and graph[m_idx][node] < distances[node]:
                distances[node] = graph[m_idx][node]
                heappush(que, (distances[node], node))

    for visit in visited:
        if not visit:
            return -1
    return sum(distances)


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    N, M = map(int, sys_input().split())

    MAX = 2501

    board = []
    for _ in range(N):
        board.append(list(sys_input())[:-1])

    KEYS = [[-1 for _ in range(N)] for __ in range(N)]

    k = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'S':
                KEYS[i][j] = 0
            elif board[i][j] == 'K':
                KEYS[i][j] = k
                k += 1

    network = [[0 for _ in range(M + 1)] for __ in range(M + 1)]
    for i in range(N):
        for j in range(N):
            if KEYS[i][j] >= 0:
                bfs(i, j, network)
    sys_print(f'{prim(network)}\n')
