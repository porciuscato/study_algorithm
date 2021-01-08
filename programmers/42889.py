def solution(N, stages):
    data = []
    length = len(stages)
    attendants = length
    stages.sort()
    idx = 0
    for n in range(1, N + 1):
        fail = 0
        while idx < length and stages[idx] == n:
            fail += 1
            idx += 1
        try:
            data.append((n, fail / attendants))
        except ZeroDivisionError:
            data.append((n, 0))
        attendants -= fail
    return [num for num, _ in sorted(data, key=lambda x: (-x[1], x[0]))]


cases = [
    (5, [2, 1, 2, 6, 2, 4, 3, 3]),
    (4, [4, 4, 4, 4, 4])
]

for case in cases:
    print(solution(*case))
