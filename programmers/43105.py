def solution(triangle):
    level = len(triangle)
    dp = [[0] * level for _ in range(level)]
    dp[0][0] = triangle[0][0]
    for i in range(1, level):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            else:
                a = dp[i - 1][j - 1] + triangle[i][j]
                b = dp[i - 1][j] + triangle[i][j]
                dp[i][j] = max(a, b)
    return max(dp[level - 1])


cases = [
    [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],
]

for case in cases:
    print(solution(case))
