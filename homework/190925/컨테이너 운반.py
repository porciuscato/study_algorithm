for T in range(1, int(input()) + 1):
    ans = 0
    N, M = map(int, input().split())
    con = sorted(list(map(int, input().split())), reverse=True)
    tru = sorted(list(map(int, input().split())), reverse=True)
    cp = tp = 0
    while cp < N and tp < M:
        if tru[tp] >= con[cp]:
            ans += con[cp]
            tp += 1
            cp += 1
        else:
            cp += 1
    print('#{} {}'.format(T, ans))
