N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda X: (X[0], X[1]))
for x, y in arr:
    print(x, y)
