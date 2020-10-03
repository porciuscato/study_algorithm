n = int(input())
for r in range(65):
    v = (2 ** r - 1) * (2 ** (64 - r))
    if v == n:
        print(r)
        break
