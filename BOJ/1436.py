size = 0
N = int(input())
for i in range(666, 3000000):
    if '666' in str(i):
        size += 1
        if size == N:
            print(i)
            break
