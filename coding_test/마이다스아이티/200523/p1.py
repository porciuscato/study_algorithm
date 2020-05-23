# from collections import deque
# from heapq import heapify
# from itertools import combinations, permutations


def solution(strs):
    strs.sort(key=len)
    words_count = len(strs)
    if not words_count:
        return ""
    length = len(strs[0])
    answer = ''
    for c in range(length):
        flag = True
        criteria = strs[0][c]
        for r in range(words_count):
            if criteria != strs[r][c]:
                flag = False
                break
        if flag:
            answer += criteria
        else:
            break
    return answer


problems = [
    ['aaaaaaaa', 'aaaaaa', 'aaaa', 'aaa'],
    ["abcaefg", "abcdefg", "abcdhfg"],
    ["a", "b", "c"],
    []
]

for problem in problems:
    print(solution(problem))
