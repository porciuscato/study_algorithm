from heapq import heappush, heappop


def prim(graph, alreay_visits) -> int:
    distances = [MAX for _ in range(N)]
    visited = [False for _ in range(N)]

    que = []
    for vis in alreay_visits:
        distances[vis] = 0
        que.append((0, vis))

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

    N, M, K = map(int, sys_input().split())
    generators = list(map(lambda x: x - 1, map(int, sys_input().split())))

    MAX = 10001

    board = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, sys_input().split())
        board[u - 1].append((v - 1, w))
        board[v - 1].append((u - 1, w))
    sys_print(f'{prim(board, generators)}\n')
