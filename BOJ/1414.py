from heapq import heappush, heappop


def prim(graph) -> int:
    distances = [MAX for _ in range(N)]
    visited = [False for _ in range(N)]
    distances[0] = 0

    que = [(0, 0)]

    while que:
        _, m_idx = heappop(que)
        visited[m_idx] = True

        for n in range(N):
            if not visited[n] and graph[m_idx][n] != 0 and graph[m_idx][n] < distances[n]:
                distances[n] = graph[m_idx][n]
                heappush(que, (distances[n], n))

    for visit in visited:
        if not visit:
            return -1
    return sum(distances)


if __name__ == "__main__":
    import sys

    s_input = sys.stdin.readline
    s_print = sys.stdout.write

    N = int(s_input())
    total = 0
    MAX = 53
    rooms = [[MAX for __ in range(N)] for _ in range(N)]
    for i in range(N):
        data = list(s_input())[:-1]
        for j in range(N):
            asc_num = ord(data[j])
            if asc_num >= 97:
                val = asc_num - 96
                rooms[i][j] = val
                total += val
            elif asc_num == 48:
                rooms[i][j] = 0
            else:
                val = asc_num - 38
                rooms[i][j] = val
                total += val

    result = prim(rooms)
    if result == -1:
        s_print(f'{result}\n')
    else:
        s_print(f'{total - result}\n')

# 3
# abA
# def
# ghi

# 3
# abA
# 0ef
# 0hi