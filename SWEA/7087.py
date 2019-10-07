import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    alpha = [0] * 26
    for n in range(N):
        word = input()
        alpha[ord(word[0]) - 65] = 1
    ans = 0
    for n in range(26):
        if not alpha[n]:
            break
        ans += 1
    print("#{} {}".format(T, ans))
