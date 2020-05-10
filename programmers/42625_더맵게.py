#### 답은 맞지만 느림
# def solution(scoville, K):
#     scoville = sorted(scoville)
#     length = len(scoville)
#     mark = length
#     for i1, v1 in enumerate(scoville):
#         if v1 >= K:
#             mark = i1
#             break
#     if mark == 0:
#         return 0
#
#     smaller = scoville[0:mark]
#     last = mark
#     _iter = 0
#     while _iter < mark:
#         if last == 0:
#             break
#         _iter += 1
#         if last == 1:
#             break
#         new_sco = smaller[0] + (smaller[1] * 2)
#         smaller = smaller[2:]
#         if new_sco >= K:
#             last -= 2
#         else:
#             for i2, v2 in enumerate(smaller):
#                 if new_sco < v2:
#                     smaller.insert(i2, new_sco)
#                     break
#             else:
#                 smaller.append(new_sco)
#             last -= 1
#
#     return -1 if _iter == length else _iter


##### 이진 트리로 만들기
# def solution(scoville, K):
#     tree = Tree(Node(K))
#     size = 0
#     for sco in scoville:
#         if sco < K:
#             tree._insert(sco)
#             size += 1
#     # print(tree.get_min(tree.root).data)
#     # print(tree.get_max(tree.root).data)
#     minimum = tree.get_min(tree.root).data
#     min1 = tree._delete(minimum)
#     print(min1)
#     minimum = tree.get_min(tree.root).data
#     min2 = tree._delete(minimum)
#     print(min2)
#     # print(min1, min2)
#     return 0

from heapq import heappush, heappop, heapify


def solution(scoville, K):
    heapify(scoville)
    chance = 0
    while scoville:
        try:
            s_1 = heappop(scoville)
            if s_1 >= K:
                return chance
            s_2 = heappop(scoville)
        except IndexError:
            return -1
        heappush(scoville, s_1 + (s_2 * 2))
        chance += 1


problems = [
    ([1, 2, 3, 9, 10, 12], 7),
    ([1, 1, 1, 9, 10, 12], 8),
    ([1, 2, 3, 9, 10, 12], 100000),
]

for problem in problems:
    print(solution(*problem))
