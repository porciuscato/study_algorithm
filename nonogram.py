def possible(board, rows, cols, row, col):
    rlist = rows[row]
    clist = cols[col]
    rcandi = []
    ccandi = []
    i, j = 0, 0
    ccount, rcount = 0, 0
    while j <= col:
        if board[row][j] == 1:
            rcount += 1
            try:
                if board[row][j + 1] == 0:
                    rcandi.append(rcount)
                    rcount = 0
            except IndexError:
                rcandi.append(rcount)
        j += 1
    while i <= row:
        if board[i][col] == 1:
            ccount += 1
            try:
                if board[i + 1][col] == 0:
                    ccandi.append(ccount)
                    ccount = 0
            except IndexError:
                ccandi.append(ccount)
        i += 1
    
    if not rcandi:
        rcandi.append(0)
    if not ccandi:
        ccandi.append(0)

    if row == len(board) - 1 or col == len(board) - 1:
        if rcandi != rlist or ccandi != clist:
            return False
    try:
        for i in range(len(rcandi)):
            if rlist[i] < rcandi[i]:
                return False
        for j in range(len(ccandi)):
            if clist[j] < ccandi[j]:
                return False
    except IndexError:
        return False
    return True


def solve(board, rows, cols, row, col):
    if row == len(board):
        return True
    else:
        nr, nc = row, col
        nc += 1
        if nc == len(board):
            nr += 1
            nc = 0

        board[row][col] = 1
        flag = True
        if not possible(board, rows, cols, row, col):
            board[row][col] = 0
            flag = False
        if flag and solve(board, rows, cols, nr, nc):
            return True

        board[row][col] = 0
        if not possible(board, rows, cols, row, col):
            return False
        if solve(board, rows, cols, nr, nc):
            return True


def solution(N, rows, cols):
    board = [[0 for _ in range(N)] for __ in range(N)]
    solve(board, rows, cols, 0, 0)
    return board


cases = [
    [
        5, 
        [[2], [2], [3], [4], [2]],  # 가로 줄의 정보, 왼쪽에서부터 오른쪽으로
        [[1, 1], [3], [3], [1, 3],[1]] # 세로 줄의 정보, 위에서부터 아래로
    ]
]

for case in cases:
    print(solution(*case))