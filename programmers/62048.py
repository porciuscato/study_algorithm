from math import ceil


def solution(w, h):
    k = h / w
    answer = w * h
    values = []
    for i in range(w + 1):
        values.append(i * k)

    # for i in range(w):
    #     answer -= ceil(values[i + 1]) - int(values[i])
    return answer


examples = [
    [8, 12],
]

for ele in examples:
    print(solution(*ele))
