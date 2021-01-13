erasable = [
    [[1, 0, 0],
     [1, 1, 1]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[0, 0, 1],
     [1, 1, 1]],
    [[1, 0],
     [1, 0],
     [1, 1]],
    [[0, 1],
     [0, 1],
     [1, 1]]
]


def aboveNone(r, c, board, pattern):
    if pattern in [0, 1, 2]:
        if pattern == 0 and c + 2 >= len(board): return False
        if pattern == 1 and (c + 1 >= len(board) or c - 1 < 0): return False
        if pattern == 2 and c - 2 < 0: return False
        if r + 1 >= len(board): return False

        cols = [[1, 2], [-1, 1], [-2, -1]]
        for col in cols[pattern]:
            row = r
            while row >= 0:
                if board[row][c + col]:
                    return False
                row -= 1
    else:
        if pattern == 3 and c + 1 >= len(board): return False
        if pattern == 4 and c - 1 < 0: return False
        if r + 2 >= len(board): return False

        cols = [c + 1, c - 1]
        row = r
        while row >= 0:
            if board[row][cols[pattern - 3]]:
                return False
            row -= 1
    return True


def check_pattern(r, c, board, pattern):
    val = board[r][c]
    temp = []
    if pattern in [0, 1, 2]:
        for row in range(r, r + 2):
            t = []
            for col in range(c - pattern, c + 3 - pattern):
                if board[row][col] == val:
                    t.append(1)
                elif board[row][col] == 0:
                    t.append(0)
                else:
                    return [], False
            temp.append(t)
    else:
        for row in range(r, r + 3):
            t = []
            for col in range(c + 3 - pattern, c + 5 - pattern):
                if board[row][col] == val:
                    t.append(1)
                elif board[row][col] == 0:
                    t.append(0)
                else:
                    return [], False
            temp.append(t)
    if temp in erasable:
        return temp, True
    else:
        return [], False


def erase(r, c, board, shape, pattern):
    if pattern in [0, 1, 2]:
        for row in range(r, r + len(shape)):
            for col in range(c - pattern, c + 3 - pattern):
                board[row][col] = 0
    else:
        for row in range(r, r + len(shape)):
            for col in range(c + 3 - pattern, c + 5 - pattern):
                board[row][col] = 0


def solve(r, c, board):
    global answer
    for p in range(5):
        if board[r][c] and aboveNone(r, c, board, p):
            shape, result = check_pattern(r, c, board, p)
            if result:
                erase(r, c, board, shape, p)
                answer += 1


def solution(board):
    global answer
    answer = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:
                solve(r, c, board)
        for c in range(len(board) - 1, -1, -1):
            if board[r][c]:
                solve(r, c, board)
    return answer


cases = [
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
     [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
     [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
     [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]],
    [[2, 2, 0, 0],
     [2, 1, 0, 0],
     [2, 1, 0, 0],
     [0, 1, 1, 0]]
]

for case in cases:
    print(solution(case))
