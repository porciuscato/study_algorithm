people = 0


def binary_search(left, right, arr):
    mid = (left + right) // 2
    result = sum(map(lambda ele: mid // ele, arr))
    left_result = sum(map(lambda ele: (mid - 1) // ele, arr))
    if result > people:
        if left_result < people:
            return mid  # answer
        else:
            return binary_search(left, mid - 1, arr)
    elif result == people:
        if left_result == people:
            return binary_search(left, mid - 1, arr)
        else:
            return mid  # answer
    else:
        return binary_search(mid + 1, right, arr)


def solution(n, times):
    global people
    people = n
    times.sort()
    return binary_search(1, n * times[-1], times)


cases = [
    (6, [7, 10]),  # 28
    (2, [1, 2]),  # 2
    # (random.randint(900000000, 1000000000), [random.randint(1, 1000000000) for _ in range(100000)])
]

for case in cases:
    print(solution(*case))

