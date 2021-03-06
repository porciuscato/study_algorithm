import sys
from collections import deque

input = sys.stdin.readline


def move(d_board, direc):
    for line in range(N):
        combined = [False] * N
        cnt = 0
        result = []

        if direc == 0:  # 위
            temp = deque([d_board[r][line] for r in range(N)])
        elif direc == 1:  # 오른
            temp = deque([d_board[line][c] for c in range(N - 1, -1, -1)])
        elif direc == 2:  # 아래
            temp = deque([d_board[r][line] for r in range(N - 1, -1, -1)])
        else:  # 왼
            temp = deque([d_board[line][c] for c in range(N)])

        for _ in range(N):
            value = temp.popleft()
            if value != 0:
                if cnt == 0:
                    result.append(value)
                    cnt += 1
                else:
                    if value == result[cnt - 1] and not combined[cnt - 1]:
                        result[cnt - 1] *= 2
                        combined[cnt - 1] = True
                    else:
                        result.append(value)
                        cnt += 1
        result += [0] * (N - cnt)

        if direc == 0:
            for r in range(N):
                d_board[r][line] = result[r]
        elif direc == 1:
            for c in range(N - 1, -1, -1):
                d_board[line][c] = result[N - 1 - c]
        elif direc == 2:
            for r in range(N - 1, -1, -1):
                d_board[r][line] = result[N - 1 - r]
        else:
            for c in range(N):
                d_board[line][c] = result[c]

    return d_board


def solve(origin, depth):
    global answer
    if depth == 5:
        mx = 0
        for i in range(N):
            mx = max(mx, max(origin[i]))
        answer = max(answer, mx)
    else:
        for i in range(4):
            solve(move([[origin[r][c] for c in range(N)] for r in range(N)], i), depth + 1)


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    solve(board, 0)
    print(answer)
