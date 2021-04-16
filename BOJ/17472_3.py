'''프림 알고리즘을 사용

인접 행렬 형태의 그래프를 생성한 뒤, 최소 신장 트리를 구한다.
'''


# bfs search
def find_island(i: int, j: int, num: int, visited: list) -> None:
    global area
    que = [(i, j)]
    front = -1
    rear = 0
    visited[i][j] = True
    area[i][j] = num
    while front != rear:
        front += 1
        r, c = que[front]
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M \
                    and area[nr][nc] \
                    and not visited[nr][nc]:
                que.append((nr, nc))
                visited[nr][nc] = True
                area[nr][nc] = num
                rear += 1


def num_of_island() -> int:
    visited = [[False for _ in range(M)] for __ in range(N)]
    num = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] and not visited[i][j]:
                num += 1
                find_island(i, j, num, visited)
    return num


def calculate_distance(row: int, col: int, graph: list) -> None:
    island_num = area[row][col]
    for dr, dc in delta:
        length = 0
        nr = row + dr
        nc = col + dc
        while 0 <= nr < N and 0 <= nc < M:
            pos = area[nr][nc]
            if pos == 0:
                nr += dr
                nc += dc
                length += 1
            elif pos != island_num:
                if 2 <= length < graph[island_num - 1][pos - 1]:
                    graph[island_num - 1][pos - 1] = length
                    graph[pos - 1][island_num - 1] = length
                else:
                    break
            else:
                break


def find_distance(graph: list) -> None:
    for r in range(N):
        for c in range(M):
            if area[r][c]:
                calculate_distance(r, c, graph)


def prim(graph: list) -> None:
    global answer
    weights = [1e9] * total_islands
    parents = [None] * total_islands
    visited = [False] * total_islands
    weights[0] = 0

    for _ in range(total_islands):
        mn = 1e9
        m_idx = -1

        for idx in range(total_islands):
            if not visited[idx] and weights[idx] < mn:
                mn = weights[idx]
                m_idx = idx
        visited[m_idx] = True

        for i in range(total_islands):
            if not visited[i] and graph[m_idx][i] != 0 and graph[m_idx][i] < weights[i]:
                weights[i] = graph[m_idx][i]
                parents[i] = m_idx

    for visit in visited:
        if not visit:
            return
    answer = min(answer, sum(weights))


def main() -> None:
    graph = [[MAX for _ in range(total_islands)] for __ in range(total_islands)]
    find_distance(graph)
    for i in range(total_islands):
        for j in range(total_islands):
            if graph[i][j] == MAX:
                graph[i][j] = 0
    prim(graph)


if __name__ == '__main__':
    MAX = 100
    answer = MAX
    delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    total_islands = num_of_island()

    main()
    print(answer if answer != MAX else -1)
