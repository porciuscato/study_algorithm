import sys

sys.stdin = open('input.txt')

S = [1, 2, 3, 4, 5, 6]
length = len(S)
face = S[0]
ans = 0
for idx in range(1, length):
    if S[idx] != face:
        if S[idx] + face == 7:
            ans += 2
        else:
            ans += 1
print(ans)