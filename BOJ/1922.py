from heapq import heappush, heappop


def prim(graph) -> int:
    distances = [MAX for _ in range(N)]
    visited = [False for _ in range(N)]
    distances[0] = 0

    que = [(0, 0)]

    while que:
        _, m_idx = heappop(que)
        visited[m_idx] = True

        for node, dist in graph[m_idx]:
            if not visited[node] and dist < distances[node]:
                distances[node] = dist
                heappush(que, (distances[node], node))

    return sum(distances)


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    N = int(sys_input())
    M = int(sys_input())
    MAX = 10001

    board = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, sys_input().split())
        board[a - 1].append((b - 1, c))
        board[b - 1].append((a - 1, c))
    sys_print(f'{prim(board)}\n')
