import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    row_cnt = [0] * N
    col_cnt = [0] * M
    for r in range(N):
        temp = list(input()[:-1])
        for c in range(M):
            if temp[c] == 'X':
                row_cnt[r] += 1
                col_cnt[c] += 1
    row_zero = 0
    col_zero = 0
    for r in range(N):
        if not row_cnt[r]:
            row_zero += 1
    for c in range(M):
        if not col_cnt[c]:
            col_zero += 1
    print(max(row_zero, col_zero))


main()
