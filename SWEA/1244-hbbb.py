import sys

sys.stdin = open('input.txt', 'r')
T = int(input())


def backtrack(k):
    global max_val
    if visited[k][int(''.join(info))]:
        return
    visited[k][int(''.join(info))] = True
    if k == chance:
        val = int(''.join(info))
        if max_val < val:
            max_val = val
    else:
        for i in range(len(info) - 1):
            for j in range(i + 1, len(info)):
                info[i], info[j] = info[j], info[i]
                backtrack(k + 1)
                info[i], info[j] = info[j], info[i]


for tc in range(1, T + 1):
    info, chance = input().split()
    info = list(info)
    chance = int(chance)
    max_val = 0
    visited = [[0] * 1000000 for _ in range(chance + 1)]
    backtrack(0)
    print('#{} {}'.format(tc, max_val))
