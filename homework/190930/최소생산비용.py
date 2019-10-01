def permu(depth, tot):
    global ans
    if depth == N:
        if tot < ans:
            ans = tot
    else:
        for i in range(N):
            if not v[i]:
                t = tot + B[depth][i]
                if t >= ans:
                    continue
                v[i] = 1
                permu(depth + 1, t)
                v[i] = 0


for T in range(1, int(input()) + 1):
    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 1e6
    permu(0, 0)
    print('#{} {}'.format(T, ans))