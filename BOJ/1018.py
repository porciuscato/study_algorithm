WHITE = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
BLACK = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


def check(r, c, arr):
    global answer
    white, black = 0, 0
    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if WHITE[i - r][j - c] != arr[i][j]:
                white += 1
            if BLACK[i - r][j - c] != arr[i][j]:
                black += 1
    answer = min((answer, white, black))


N, M = map(int, input().split())
ORIGIN = [input() for _ in range(N)]
answer = 1e9
for n in range(N - 7):
    for m in range(M - 7):
        check(n, m, ORIGIN)
print(answer)
