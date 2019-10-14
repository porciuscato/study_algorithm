import sys
import random

sys.stdout = open('input.txt', 'w')

T = 10
vari = 1000
print(T)
for t in range(T):
    maxi = 2
    N = random.randint(2, 5000)
    print(N)
    print(1)
    for _ in range(1, N):
        n = random.randint(maxi, maxi + vari)
        maxi = n + 1
        print(n)

