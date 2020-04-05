# https://programmers.co.kr/learn/courses/30/lessons/42895


# def bfs(num, aim, depth):
#     # 먼저 현재 하려는 값이 memo에 있는가?
#     if (num, depth) in memo:
#         return
#     # 이후에 bfs로 탐색


# def solution(num, aim):
#     memo = [(num, 1)]
#     head = -1
#     tail = 0
#     while head != tail:
#         print(memo)
#         head += 1
#         prev_num, depth = memo[head]
#         if depth > 8:
#             return -1
#         # 원하는 값이 맞으면 바로 끝내
#         if prev_num == aim:
#             return depth
#         # 아니야? 그러면 돌면서 하나씩 추가하자
#         for i in range(5):
#             new_ele = 0
#             if i == 0:
#                 new_ele = (prev_num + num, depth + 1)
#             elif i == 1:
#                 new_ele = (prev_num - num, depth + 1)
#             elif i == 2:
#                 new_ele = (prev_num * num, depth + 1)
#             elif i == 3:
#                 new_ele = (int(prev_num / num), depth + 1)
#             elif i == 4:
#                 new_ele = (int(str(prev_num) + str(num)), depth + 1)
#             if new_ele not in memo:
#                 memo.append(new_ele)
#                 tail += 1


def solution(num, aim):
    memo = [[num], [], [], [], [], [], [], []]
    for idx, me in enumerate(memo):
        print(me)
        for n in me:
            if n == aim:
                return idx + 1
            for i in range(5):
                new_ele = 0
                if i == 0:
                    new_ele = n + num
                elif i == 1:
                    new_ele = n - num
                elif i == 2:
                    new_ele = n * num
                elif i == 3:
                    new_ele = int(n / num)
                elif i == 4:
                    new_ele = int(str(n) + str(num))
                if new_ele == aim:
                    return idx + 2
                if new_ele > 0 and new_ele not in sum(memo, []):
                    if idx + 1 >= 8:
                        return -1
                    memo[idx + 1].append(new_ele)


# print(solution(5, 31168))
# print(solution(8, 22312))
# print(solution(5, 26))
# print(5, 624)
# print(solution(4, 17))
# print(solution(4, 4))