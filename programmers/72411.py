from itertools import combinations


def check(order, combi):
    for menu in combi:
        if menu not in order:
            return False
    return True


def solution(orders, course):
    orders = sorted(list(map(lambda x: ''.join(x), map(sorted, orders))), key=lambda x: (len(x), x))
    candidates = {}
    for count in course:
        for order in orders:
            if count <= len(order):
                for combi in combinations(order, count):
                    if candidates.get(combi):
                        candidates[combi] += 1
                    else:
                        candidates[combi] = 1
    answer = []
    for key, value in candidates.items():
        if value >= 2:
            answer.append(''.join(key))
    answer.sort()
    return answer


cases = [
    (["ABC", "ABCD"], [2, 3]),
    (["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]),
    (["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]),
    (["XYZ", "XWY", "WXA"], [2, 3, 4]),
]

for case in cases:
    print(solution(*case))
