import sys

input = sys.stdin.readline

D_3 = (
    (0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4),
    (5, 1, 2), (5, 1, 3), (5, 2, 4), (5, 3, 4)
)
D_2 = (
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3),
    (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)
)


def main():
    N = int(input())
    dice = list(map(int, input().split()))
    if N == 1:
        print(sum(dice) - max(dice))
    else:
        dice_3_min = 150
        dice_2_min = 150
        dice_1_min = min(dice)
        for a, b, c in D_3:
            dice_3_min = min(dice_3_min, dice[a] + dice[b] + dice[c])
        for a, b in D_2:
            dice_2_min = min(dice_2_min, dice[a] + dice[b])
        ans = (dice_3_min * 4) + (dice_2_min * (4 * (N - 1) + 4 * (N - 2))) + (dice_1_min * ((N - 2) * (N - 1) * 4 + (N - 2) ** 2))
        print(ans)


main()

# 1000000
# 50 50 50 50 50 50
# 250000000000000

# 3
# 1 1 1 1 1 1
# 45

# 1
# 6 5 4 3 2 1
# 15

# 2
# 1 2 10 11 12 3
# 64

# 2
# 1 5 5 5 5 1
# 68