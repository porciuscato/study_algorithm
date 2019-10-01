def subset(arr, depth, battery, change):
    global ans
    if depth == N - 1:
        if change < ans:
            ans = change
    else:
        if change >= ans:
            return
        ar = arr[:]
        ar += [depth]
        if battery == 0:
            ch = change + 1
            if ch >= ans:
                return
            subset(ar, depth + 1, stops[depth] - 1, ch)
        else:
            subset(ar, depth + 1, stops[depth] - 1, change + 1)
            subset(arr, depth + 1, battery - 1, change)


for T in range(1, int(input()) + 1):
    inp = list(map(int, input().split()))
    N = inp[0]
    stops = inp[1:]
    ans = N
    subset([0], 1, stops[0] - 1, 0)
    print('#{} {}'.format(T, ans))