def solution(board, r, c):
    answer = 0
    return answer


cases = [
    ([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0),  # 14
    ([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1),  # 16

]

for case in cases:
    print(solution(*case))
