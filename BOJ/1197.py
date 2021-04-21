from heapq import heappush, heappop


def prim(graph) -> int:
    length = V
    distances = [MAX for _ in range(length)]
    distances[0] = 0
    visited = [False for _ in range(length)]

    que = [(distances[0], 0)]

    while que:
        _, m_idx = heappop(que)
        visited[m_idx] = True

        for node, dis in graph[m_idx]:
            if not visited[node] and dis < distances[node]:
                distances[node] = dis
                heappush(que, (distances[node], node))

    total = 0
    for i in range(length):
        total += distances[i] if visited[i] else 0
    return total


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    V, E = map(int, sys_input().split())
    board = [[] for _ in range(V)]

    MAX = 1000001
    for _ in range(E):
        x, y, d = map(int, sys_input().split())
        board[x - 1].append((y - 1, d))
        board[y - 1].append((x - 1, d))
    sys_print(f'{prim(board)}\n')
