import sys

input = sys.stdin.readline
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def find_guest(row, col):
    global taxi, fuel
    visited = [[False for _ in range(N)] for __ in range(N)]
    huboes = []
    que = [(row, col, 0)]
    if isinstance(board[row][col], tuple):
        _, gi = board[row][col]
        board[row][col] = 0
        return gi
    visited[row][col] = True
    f = -1
    r = 0
    while f != r:
        f += 1
        cr, cc, cd = que[f]
        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            nd = cd + 1
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] != 1:
                if board[nr][nc] == 0:
                    que.append((nr, nc, nd))
                    visited[nr][nc] = True
                    r += 1
                elif isinstance(board[nr][nc], tuple):
                    huboes.append((nd, nr, nc, board[nr][nc][1]))
                    que.append((nr, nc, nd))
                    visited[nr][nc] = True
                    r += 1
    if huboes:
        huboes.sort(key=lambda x: (x[0], x[1], x[2]))
        gd, gr, gc, gi = huboes[0]
        if fuel - gd >= 0:
            taxi = [gr, gc]
            board[gr][gc] = 0
            fuel -= gd
            return gi
    return -1


def guest_to_desti(arr):
    global taxi, fuel
    dep_r, dep_c, des_r, des_c = arr
    found = False
    distance = 0
    visited = [[False for _ in range(N)] for __ in range(N)]
    que = [(dep_r, dep_c, 0)]
    visited[dep_r][dep_c] = True
    f = -1
    r = 0
    while f != r:
        f += 1
        cr, cc, cd = que[f]
        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            nd = cd + 1
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] != 1:
                if nr == des_r and nc == des_c:
                    distance = nd
                    found = True
                    taxi = [nr, nc]
                    break
                else:
                    que.append((nr, nc, nd))
                    visited[nr][nc] = True
                    r += 1
        if found:
            break
    if found:
        if fuel - distance >= 0:
            fuel += distance
            return True
    return False


if __name__ == "__main__":
    N, M, fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    taxi = list(map(lambda x: x - 1, map(int, input().split())))
    guests = []
    for i in range(M):
        temp = list(map(lambda x: x - 1, map(int, input().split())))
        guests.append(temp)
        board[temp[0]][temp[1]] = (2, i)
    for i in range(M):
        guest = find_guest(*taxi)
        if guest >= 0:
            if not guest_to_desti(guests[guest]):
                print(-1)
                exit()
        else:
            print(-1)
            exit()
    print(fuel)



# 6 4 15
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 6 5
# 2 2 5 6
# 5 4 1 6
# 4 2 3 5
# 1 6 5 4