from math import ceil


def solution(w, h):
    k = h / w
    answer = w * h
    tot = 0
    values = []
    for i in range(w + 1):
        values.append(i * k)
    for i in range(w):
        tot += ceil(values[i + 1]) - int(values[i])
    return answer - tot


print(solution(8, 12))

