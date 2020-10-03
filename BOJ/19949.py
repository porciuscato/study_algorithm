def solve(arr, depth, point):
    global ans
    if depth >= 6 and point <= depth - 6:
        return
    if depth == 10:
        if point >= 5:
            ans += 1
    else:
        for i in range(1, 6):
            ar = arr[:]
            ar.append(i)
            p = point + 1 if i == answers[depth] else point
            if depth >= 2:
                if not (i == ar[depth - 1] and i == ar[depth - 2]):
                    solve(ar, depth + 1, p)
            else:
                solve(ar, depth + 1, p)


answers = list(map(int, input().split()))
ans = 0
solve([], 0, 0)
print(ans)
