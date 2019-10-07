def solve(depth, last):
    global count
    if depth == 5:
        count += 1
    else:
        for r in range(4):
            for c in range(last, 13):
                if not v[c]:
                    v[c] = 1
                    solve(depth + 1, c + 1)
                    v[c] = 0


count = 0
v = [0] * 13
solve(0, 0)
print(count)
