import sys
from datetime import datetime

sys.stdin = open('input.txt', 'r')

start = datetime.now()
for T in range(1, int(input()) + 1):
    N = int(input())
    num = list(map(int, input().split()))
    save = [1] + ([0] * sum(num))
    ans = 1
    temp = [0]
    for n in num:
        for i in range(ans):
            if save[n + temp[i]] == 0:
                save[n + temp[i]] = 1
                ans += 1
                temp += [n + temp[i]]
    print('#{} {}'.format(T, ans))
print(datetime.now() - start)
