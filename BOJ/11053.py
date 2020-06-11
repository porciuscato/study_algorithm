def main():
    N = int(input())
    ans = [list(map(int, input().split())), [1] * N]
    for n in range(N):
        val = ans[0][n]
        temp = []
        for i in range(n - 1, -1, -1):
            if val > ans[0][i]:
                temp.append(ans[1][i])
        try:
            ans[1][n] = max(temp) + 1
        except ValueError:
            continue
    return max(ans[1])


print(main())
