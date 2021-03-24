from pprint import pprint


def solution(a):
    answer = 0
    check = [[10e7 for _ in range(len(a))] for __ in range(2)]
    left, right = 10e7, 10e7
    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
        check[0][i] = left
    for i in range(len(a) - 1, -1, -1):
        if a[i] < right:
            right = a[i]
        check[1][i] = right

    for i in range(len(a)):
        if a[i] <= check[0][i] or a[i] <= check[1][i]:
            # print(a[i])
            answer += 1

    return answer


cases = [
    [9, -1, -5],
    [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
]

for case in cases:
    print(solution(case))
