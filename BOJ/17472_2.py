'''disjoint set을 사용해 완탐을 하려했으나 문제 풀이가 되지 않았다.

방법을 바꿔보자.
'''

import sys
sys.setrecursionlimit(10000)


class DisjointSet:
    def __init__(self, num: int):
        self.parent = [e for e in range(num + 1)]

    def find_set(self, x: int) -> int:
        if x != self.parent[x]:
            return self.find_set(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> None:
        self.parent[y] = self.parent[x]

    def separate(self, x: int) -> None:
        self.parent[x] = x


def find_island(i, j, num, visited) -> None:  # bfs search
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


def bridge_test(row: int, col: int, dr: int, dc: int,  dis_set: DisjointSet) -> (bool, int, int):
    start = area[row][col]
    row += dr
    col += dc
    length = 0
    while 0 <= row < N and 0 <= col < M:
        if area[row][col] == 0:
            length += 1
            row += dr
            col += dc
        elif length >= 2:
            if area[row][col] == start:
                return False, 0, 0
            else:
                if dis_set.find_set(start) != dis_set.find_set(area[row][col]):
                    return True, length, area[row][col]
                else:
                    return False, 0, 0
        else:
            return False, 0, 0
    return False, 0, 0


def make_bridges(row: int, col: int, bridges: int, dis_set: DisjointSet) -> None:
    global answer
    if row == N:
        parent = dis_set.find_set(1)
        for i in range(2, total_islands + 1):
            if dis_set.find_set(i) != parent:
                return
        answer = min(answer, bridges)
    else:
        if area[row][col]:
            nr = row
            nc = col + 1
            if nc == M:
                nr = row + 1
                nc = 0
            island_num = area[row][col]
            for dr, dc in delta:
                is_possible, length, target_island = bridge_test(row, col, dr, dc, dis_set)
                if is_possible:
                    dis_set.unite(island_num, target_island)
                    make_bridges(nr, nc, bridges + length, dis_set)
                    dis_set.separate(target_island)
            # make_bridges(nr, nc, bridges, dis_set)

        col += 1
        if col == M:
            col = 0
            row += 1
        make_bridges(row, col, bridges, dis_set)


def main() -> None:
    global total_islands
    total_islands = num_of_island()
    disjoint_set = DisjointSet(total_islands)
    make_bridges(0, 0, 0, disjoint_set)


if __name__ == '__main__':
    MAX = 100
    answer = MAX
    delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    total_islands = ...
    main()
    print(answer if answer != MAX else -1)


# 5 6
# 1 1 0 0 0 1
# 1 1 0 0 0 1
# 0 0 0 0 0 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1

# 6 5
# 1 1 0 0 1
# 1 1 0 0 1
# 0 0 0 0 1
# 0 0 0 0 1
# 0 0 0 0 1
# 1 1 1 1 1