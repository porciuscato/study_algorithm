def solution(N, number):
    def solve(depth, total):
        nonlocal answer
        if total < 0:
            return
        if depth > 4:
            return
        if total == number:
            answer = min(answer, depth)
        tmp = 0
        for i in range(1, 4):
            tmp = tmp * 10 + N
            solve(depth + 1, total + tmp)
            solve(depth + 1, total - tmp)
            solve(depth + 1, total // tmp)
            solve(depth + 1, total * tmp)

    answer = 9
    solve(0, 0)
    if answer > 8:
        return -1
    return answer


cases = [
    (5, 12),
    (5, 31168)
]

for case in cases:
    print(solution(*case))
