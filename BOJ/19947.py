def solve(m, year):
    global ans
    arr = [(int(m * 1.05), 1), (int(m * 1.2), 3), (int(m * 1.35), 5)]
    for v, s in arr:
        if year - s >= 0:
            ans = max(ans, v)
            solve(v, year - s)


H, Y = map(int, input().split())
ans = 0
solve(H, Y)
print(ans)