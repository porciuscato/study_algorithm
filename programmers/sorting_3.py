def solution(citations):
    origin = sorted(citations, reverse=True)
    mx = origin[0]
    table = [[0] * (mx + 1) for _ in range(2)]
    incre_count = 0
    decre_count = len(origin)
    idx = 0
    for ele in range(mx, -1, -1):
        while idx < len(origin) and ele == origin[idx]:
            incre_count += 1
            decre_count -= 1
            table[0][ele] = incre_count
            table[1][ele] = decre_count
            idx += 1
        if ele != origin[idx - 1]:
            table[0][ele] = incre_count
            table[1][ele] = decre_count
        if table[1][ele] <= ele <= table[0][ele]:
            return ele


# print(solution([3, 0, 6, 1, 5, 6, 6, 0, 0, 0, 0]))
print(solution([0, 0, 0, 1, 1, 1, 1, 9]))
# print(solution([4, 3, 3, 3, 3]))