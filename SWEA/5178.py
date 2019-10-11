import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N * 2)
    start = 1e10
    for m in range(M):
        i, v = map(int, input().split())
        tree[i] = v
        start = min(start, i)
    for idx in range(start - 1, 0, -1):
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
    print('#{} {}'.format(T, tree[L]))
