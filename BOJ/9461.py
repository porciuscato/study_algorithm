arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    value = arr[i - 2] + arr[i - 3]
    arr.append(value)

N = int(input())
for _ in range(N):
    print(arr[int(input())])
