def solution(gems):
    left_gems = {}
    for gem in gems:
        if left_gems.get(gem):
            left_gems[gem] += 1
        else:
            left_gems[gem] = 1
    left = 0
    right = len(gems) - 1
    while left < right:
        gem = gems[right]
        if left_gems[gem] - 1 == 0:
            break
        else:
            left_gems[gem] -= 1
            right -= 1
    while left < right:
        gem = gems[left]
        if left_gems[gem] - 1 == 0:
            break
        else:
            left_gems[gem] -= 1
            left += 1

    answer = [left + 1, right + 1]
    return answer


cases = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
    ["a", 'b', 'b', 'a', 'b', 'c', 'a']
]

for case in cases:
    print(solution(case))
