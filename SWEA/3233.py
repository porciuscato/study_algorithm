import sys

sys.stdin = open("3233.txt", "r")

for T in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    print('#{} {}'.format(T, int((A**2) / (B**2))))