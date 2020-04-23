T = int(input())
arr = []
for _ in range(T):
    x, y = map(int, input().split())
    arr.append((x, y))
for i in range(T):
    x, y = arr[i]
    ans = 0
    for j in range(T):
        if i != j:
            if x < arr[j][0] and y < arr[j][1]:
                ans += 1
    print(ans + 1, end=' ')
