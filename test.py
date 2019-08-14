import sys

sys.stdin = open('input.txt', 'r', encoding='utf-8')

for T in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, list(input()))) for i in range(N)]

    arr = []
    for i in range(int(N / 2) + 1):
        arr.append(i)
    for i in range(int(N / 2) - 1, -1, -1):
        arr.append(i)

    mid = int(N / 2)
    tot = 0
    for i in range(N):
        tot += sum(board[i][mid - arr[i]: mid + 1 + arr[i]])
    print('#{} {}'.format(T, tot))
