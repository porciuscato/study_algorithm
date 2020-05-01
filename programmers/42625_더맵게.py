def solution(scoville, K):
    scoville = sorted(scoville)
    length = len(scoville)
    mark = length
    for i1, v1 in enumerate(scoville):
        if v1 >= K:
            mark = i1
            break
    if mark == 0:
        return 0

    smaller = scoville[0:mark]
    last = mark

    _iter = 0
    while _iter < mark:
        if last == 0:
            break
        _iter += 1
        if last == 1:
            break
        new_sco = smaller[0] + (smaller[1] * 2)
        smaller = smaller[2:]
        if new_sco >= K:
            last -= 2
        else:
            for i2, v2 in enumerate(smaller):
                if new_sco < v2:
                    smaller.insert(i2, new_sco)
                    break
            else:
                smaller.append(new_sco)
            last -= 1
        # 처리후 K 보다 크면 빼

    return -1 if _iter == length else _iter


problems = [
    ([1, 2, 3, 9, 10, 12], 7),
    ([1, 1, 1, 9, 10, 12], 8),
    ([1, 2, 3, 9, 10, 12], 100000),
]

for problem in problems:
    print(solution(*problem))
