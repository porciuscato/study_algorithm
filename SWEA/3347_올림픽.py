import sys

sys.stdin = open('3347.txt', 'r')

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    event = list(map(int, input().split()))
    committee = list(map(int, input().split()))
    votes = [0] * N
    for ci, c in enumerate(committee):
        for ei, e in enumerate(event):
            if c >= e:
                votes[ei] += 1
                break
    answer, mx = 0, 0
    for vi, v in enumerate(votes):
        if mx < v:
            mx = v
            answer = vi
    print(f'#{T} {answer + 1}')
