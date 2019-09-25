import copy


def chess(board, d):
    global count
    if d == N:
        count += 1
    else:
        b = copy.deepcopy(board)
        for r in range(N):
            for c in range(N):
                if valid(r, c):
                    b[r][c] = 1
                    check(board, d + 1)


N = int(input())
count = 0
board = [[0] * N for _ in range(N)]
print(count)
