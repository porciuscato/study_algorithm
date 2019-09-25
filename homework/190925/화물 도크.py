def check(d, schedule, tot):
    global ans
    if d == N:
        if tot > ans:
            ans = tot
    else:
        table = schedule[:]
        s, e = time[d]
        pos = True
        for i in range(s, e):
            if table[i]:
                pos = False
                break
        if pos:
            for i in range(s, e):
                table[i] = 1
            t = tot + 1
            if N - d + t > ans:
                check(d + 1, table, t)
        if N - d + tot > ans:
            check(d + 1, schedule, tot)


for T in range(1, int(input()) + 1):
    ans = 0
    N = int(input())
    time = [0] * N
    for i in range(N):
        time[i] = tuple(map(int, input().split()))
    time = sorted(time, key=lambda ele: ele[1], reverse=True)
    check(0, [0] * 24, 0)
    print('#{} {}'.format(T, ans))
