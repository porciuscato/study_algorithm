def aboveNone(r, c, board, blank):
    for i in range(blank):
        for col in range(c - i, c + blank - i):
            if c - i >= 0 or c + blank - i < len(board):
                r -= 1
                while r >= 0:
                    if board[r][col]:
                        return False
                    r -= 1
    return True


def check_pattern1(r, c, board):
    global N
    return [], False


def check_pattern2(r, c, board):
    global N
    return [], False


def solution(board):
    global N
    answer = 0
    N = len(board)
    visited = [[False for _ in range(N)] for __ in range(N)]  # 앞과 뒤 모두 했음에도 지울 수 없으면 visited 처리하자.
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and board[r][c]:
                shape, result = check_pattern1(r, c, board)
                if result:
                    if aboveNone(r, c, board, 3):
                        pass
                    else:
                        # 전부 visited로 바꾼다.
                        continue
                if not result:
                    shape, result = check_pattern2(r, c, board)
                    if aboveNone(r, c, board, 2):
                        pass
                # shape eraseable check

                pass
        for c in range(N - 1, -1, -1):
            if not visited[r][c] and board[r][c]:
                pass

            if not visited[r][c] and board[r][c]:
                match = False
                # 어떤 패턴인지 모르잖아.
                if aboveNone(r, c, board, 3):
                    if check_pattern1(r, c, board):
                        match = True
                        # 가능하면 지우고

                if not match and aboveNone(r, c, board, 2):
                    if check_pattern2(r, c, board):
                        match = True
                        # 가능하면 지운다.

                if match:
                    answer += 1
                if not match:
                    # match가 안 됐으면 전부 true 로 바꾼다.
                    pass

    return answer


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
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
]

for case in cases:
    print(solution(case))

a = [[1, 1, 0], [1, 1, 0]]
b = [[1, 1, 0], [1, 1, 0]]
print(a == b)
