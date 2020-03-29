import sys

sys.stdin = open('3376.txt', 'r')

P = [1, 1, 1, 2]
for n in range(4, 101):
    P.append(P[n - 3] + P[n - 2])

for T in range(1, int(input()) + 1):
    N = int(input()) - 1
    print('#{} {}'.format(T, P[N]))