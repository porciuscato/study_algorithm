def solution(board):
    length = len(board)
    answer = 0
    visited = [[False for _ in range(length)] for __ in range(length)]

    def is_possible(row, col):
        row -= 1
        while 0 <= row:
            if visited[row][col]:
                return False
            row -= 1
        return True

    def brute(depth, point):
        nonlocal answer
        if depth == length:
            answer = max(answer, point)
        else:
            for i in range(length):
                if is_possible(depth, i):
                    visited[depth][i] = True
                    brute(depth + 1, point + board[depth][i])
                    visited[depth][i] = False

    brute(0, 0)
    return answer


cases = [
    [[12, 15], [19, 21]],
    [[3, 6, 8], [1, 4, 7], [2, 1, 4]]
]

for case in cases:
    print(solution(case))
