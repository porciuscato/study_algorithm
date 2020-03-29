# 위장
#
# answer = 0
#
#
# def subset(origin, array, depth, aim):
#     global answer
#     if depth == aim:
#         total = 1 if array else 0
#         for j in array:
#             total *= origin[j]
#         answer += total
#     else:
#         for i in range(2):
#             ar = array[:]
#             if i:
#                 ar.append(depth)
#             subset(origin, ar, depth + 1, aim)


def solution(clothes):
    all_clothes = {}
    for cloth in clothes:
        if all_clothes.get(cloth[1]):
            all_clothes[cloth[1]].append(cloth[0])
        else:
            all_clothes[cloth[1]] = [cloth[0]]
    to_number_list = []
    for cloth in all_clothes:
        to_number_list.append(len(all_clothes[cloth]))
    answer = 1
    for number in to_number_list:
        answer *= (number + 1)
    return answer - 1



print(solution([
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"]
        ]))


# print(subset([1,2,3], [], 0, 3))