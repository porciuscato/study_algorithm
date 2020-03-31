def solution(numbers):
    origin = list(map(str, numbers))
    result = []
    for idx, value in enumerate(origin):
        element = value[0]
        added = 4
        while len(value) < 4:
            value += element
            added -= 1
        result.append((idx, int(value), added))
    ordered = sorted(result, key=lambda x: x[1], reverse=True)
    # print(ordered)
    answer = ''
    for ele in ordered:
        answer += origin[ele[0]]
    answer = str(int(answer))
    return answer


# print(solution([3, 30, 34, 5, 9]))
# print(solution([6, 10, 2, 1, 3, 4, 5, 7, 8, 9, 123, 3, 31, 30, 325, 342, 325, 325, 321, 37, 397]))

# print(solution([0, 0, 0, 0, 1]))
# print(solution([10, 100, 1000]))
# print(solution([0, 0, 0, 0]))
# print(solution([12, 121]))
# print(solution([998, 9, 999]))
# print(solution([20, 200, 20]))

# 0,0,0,0,1 10000
# 10,100,1000 101001000
# 0,0,0 0 0
# 12,121 12121
# 998,9,999 9999998
# 20,200,20 2020200
a = [
    [40, 403],
    [40, 405],
    [40, 404],
    [12, 121], # 12121
    [2, 22, 223],
    [21, 212], # 틀림 -> 21221
    [41, 415],
    [2, 22],
    [70, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1000],
    [12, 1213],
]
for aa in a:
    print(solution(aa))
