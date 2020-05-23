def solve(hammer, board, length):
    result = 0
    hr = hammer[0]
    hc = hammer[1]
    # 복사
    copied = [[0] * length for _ in range(length)]
    for rr in range(length):
        for cc in range(length):
            copied[rr][cc] = board[rr][cc]

    # 망치로 깨부수기
    result += 1
    while hr > 0:
        copied[hr][hc] = copied[hr - 1][hc]
        hr -= 1
    copied[hr][hc] = 0

    flag = True
    while flag:
        flag = False
        crushed = [[0] * length for _ in range(length)]
        # 가로로 탐색 -> 1로 바꾼다
        for r1 in range(length):
            for c1 in range(length - 2):
                if crushed[r1][c1] != 1 and copied[r1][c1]:
                    start = c1
                    pos = c1
                    point = copied[r1][c1]
                    size = 0
                    while pos < length and copied[r1][pos] == point:
                        pos += 1
                        size += 1
                    if size >= 3:
                        flag = True
                        for cru in range(start, start + size):
                            crushed[r1][cru] = 1
        # 세로로 탐색 -> 2로 바꾼다
        for c2 in range(length):
            for r2 in range(length - 2):
                if crushed[r2][c2] != 2 and copied[r2][c2]:
                    start = r2
                    pos = r2
                    point = copied[r2][c2]
                    size = 0
                    while pos < length and copied[pos][c2] == point:
                        pos += 1
                        size += 1
                    if size >= 3:
                        flag = True
                        for cru in range(start, start + size):
                            crushed[cru][c2] = 2
        if flag:
            # 터트리기
            for r3 in range(length):
                for c3 in range(length):
                    if crushed[r3][c3]:
                        copied[r3][c3] = 0
                        result += 1

            # 이동 / 아래서부터 이동 / 터지면 0이 된다.
            b_c = 0
            while b_c < length:
                origin = length - 1
                while origin > 0:
                    b_r = origin
                    if copied[origin][b_c] == 0:
                        while b_r >= 0 and not copied[b_r][b_c]:
                            b_r -= 1
                    if b_r >= 0:
                        copied[b_r][b_c], copied[origin][b_c] = copied[origin][b_c], copied[b_r][b_c]
                        origin -= 1
                    else:
                        break
                b_c += 1
    return result


def solution(board):
    answer = 0
    length = len(board)
    for r in range(length):
        for c in range(length):
            answer = max(answer, solve((r, c), board, length))
    return answer


problems = [
    [[1, 1, 3, 3], [4, 1, 3, 4], [1, 2, 1, 1], [2, 1, 3, 2]],
    [[1, 2, 3, 4, 1, 2, 3, 4, 1, 2], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2],
     [1, 2, 3, 4, 1, 2, 3, 4, 1, 2], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2],
     [1, 2, 3, 4, 1, 2, 3, 4, 1, 2], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2],
     [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]],
    []
]

for problem in problems:
    print(solution(problem))
