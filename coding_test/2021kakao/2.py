from itertools import combinations


def make_combinations(course_dict, order, choose):
    for result in combinations(order, choose):
        course = "".join(sorted(list(result)))
        if course_dict[choose].get(course):
            course_dict[choose][course] += 1
        else:
            course_dict[choose][course] = 1


def find_max(course_dict, choose):
    result = []
    mx = 0
    for key, value in course_dict[choose].items():
        if value > 1 and value >= mx:
            if value == mx:
                result.append(key)
            elif value > mx:
                result = [key]
                mx = value
    return result


def solution(orders, course):
    answer = []
    course_dict = [dict() for __ in range(11)]
    for order in orders:
        length = len(order)
        for choose in course:
            if length >= choose:
                make_combinations(course_dict, order, choose)
    for choose in course:
        answer += find_max(course_dict, choose)
    answer.sort()
    return answer


cases = [
    (["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]),
    (["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]),
    (["XYZ", "XWY", "WXA"], [2, 3, 4])
]

for case in cases:
    print(solution(*case))
