    def main():
        n, k = map(int, input().split())
        weights = [0] * n
        values = [0] * n
        for i in range(n):
            weights[i], values[i] = map(int, input().split())

        dp = [0] * (k + 1)
        for i in range(n):
            for j in range(k, 0, -1):
                if j >= weights[i]:
                    dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
        print(dp[k])


    main()
