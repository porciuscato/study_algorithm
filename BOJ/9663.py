answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
# 13개부터 10초 미만으로 안 나온다

def check(row, col, board):
    l_r, l_c = row - 1, col - 1
    while l_r >= 0 and l_c >= 0:
        if board[l_r][l_c]:
            return False
        l_r -= 1
        l_c -= 1

    u_r, u_c = row - 1, col
    while u_r >= 0:
        if board[u_r][u_c]:
            return False
        u_r -= 1

    r_r, r_c = row - 1, col + 1
    while r_r >= 0 and r_c < N:
        if board[r_r][r_c]:
            return False
        r_r -= 1
        r_c += 1
    return True


def solve(row, aim, Board):
    global answer, visited
    if row == aim - 1:
        answer += 1
    else:
        for column in range(N):
            if not visited[column]:
                if check(row + 1, column, Board):
                    Board[row + 1][column] = 1
                    visited[column] = True
                    solve(row + 1, aim, Board)
                    visited[column] = False
                    Board[row + 1][column] = 0


import time
N = int(input())
st = time.time()
answer = 0
ORIGIN = [[0] * N for _ in range(N)]
visited = [False] * N
for n in range(N):
    ORIGIN[0][n] = 1
    visited[n] = True
    solve(0, N, ORIGIN)
    visited[n] = False
    ORIGIN[0][n] = 0

print(answer)
print(time.time() - st)
