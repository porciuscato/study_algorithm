board = [
    [0, 0, 1, 0], [1, 2, 2, 0], [2, 4, 3, 0], [3, 6, 4, 0], [4, 8, 5, 0],
    [5, 10, 6, 21], [6, 12, 7, 0], [7, 14, 8, 0], [8, 16, 9, 0], [9, 18, 10, 0],
    [10, 20, 11, 25], [11, 22, 12, 0], [12, 24, 13, 0], [13, 26, 14, 0], [14, 28, 15, 0],
    [15, 30, 16, 27], [16, 32, 17, 0], [17, 34, 18, 0], [18, 36, 19, 0], [19, 38, 20, 0],
    [20, 40, 32, 0], [21, 13, 22, 0], [22, 16, 23, 0], [23, 19, 24, 0], [24, 25, 30, 0],
    [25, 22, 26, 0], [26, 24, 24, 0], [27, 28, 28, 0], [28, 27, 29, 0], [29, 26, 24, 0],
    [30, 30, 31, 0], [31, 35, 20, 0], [32, -1, -1, -1]
]


def solve(horses, depth, point):
    global ans
    if depth == 10:
        ans = max(ans, point)
    else:
        for i in range(4):
            if horses[i] != -1:
                horse = horses[:]
                cur = board[horse[i]]
                for n in range(dices[depth]):
                    if n == 0 and cur[3] != 0:
                        cur = board[cur[3]]
                    else:
                        cur = board[cur[2]]
                    if cur[0] == 32:
                        horse[i] = -1
                        break
                if horse[i] >= 0:
                    for h in horse:
                        if 0 <= h == cur[0]:
                            break
                    else:
                        horse[i] = cur[0]
                        solve(horse, depth + 1, point + cur[1])
                else:
                    solve(horse, depth + 1, point)


if __name__ == "__main__":
    dices = list(map(int, input().split()))
    ans = 0
    solve([0, 0, 0, 0], 0, 0)
    print(ans)

