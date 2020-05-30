arr = []
N = int(input())
for n in range(N):
    age, name = input().split()
    arr.append((n, int(age), name))
arr.sort(key=lambda x: (x[1], x[0]))
for idx, age, name in arr:
    print(age, name)

