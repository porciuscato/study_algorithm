import sys
import random

sys.stdout = open('input.txt', 'w')

T = 5
value = 2000
print(T)
for t in range(T):
    maxi = 2
    N = random.randint(10, 10)
    print(1)
    for _ in range(1, N):
        n = random.randint(maxi, value)
        maxi = n + 1
        print(n)