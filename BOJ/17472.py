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


def is_bridge_possible(row, col, dr, dc, island_num, check_connec) -> (bool, int, int):
    length = 1
    while 0 <= row < N and 0 <= col < M:
        if area[row][col] == 0:
            row += dr
            col += dc
            length += 1
        else:
            target = area[row][col]
            if not check_connec[target] and target != island_num:
                if length >= 2:
                    return True, length - 1, target
                else:
                    return False, 0, 0
            else:
                return False, 0, 0
    return False, 0, 0


def make_bridges(row, col, check_connec, bridges):
    global answer
    if row == N:
        answer = min(answer, bridges)
    else:
        if area[row][col]:
            island_num = area[row][col]
            for dr, dc in delta:
                is_possible, length, target_island = is_bridge_possible(row + dr, col + dc, dr, dc,
                                                                        island_num, check_connec)
                if is_possible:
                    check_connec[island_num] += 1
                    check_connec[target_island] += 1
                    make_bridges(row, col, check_connec, bridges + length)
                    check_connec[island_num] -= 1
                    check_connec[target_island] -= 1
        col += 1
        if col == M:
            col = 0
            row += 1
        make_bridges(row, col, check_connec, bridges)


def main() -> None:
    total_islands = num_of_island()
    check_connec = [False for _ in range(total_islands + 1)]
    make_bridges(0, 0, check_connec, 0)
    pass


if __name__ == '__main__':
    MAX = 100
    answer = MAX
    delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    main()
    print(answer if answer != MAX else -1)
