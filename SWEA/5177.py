import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    inp = list(map(int, input().split()))
    tree = [0] * (N + 1)
    idx = 1
    for val in range(N):
        tree[idx] = inp[val]
        position = idx
        parent = int(idx / 2)
        while parent:
            change = False
            if tree[position] < tree[parent]:
                tree[position], tree[parent] = tree[parent], tree[position]
                change = True
                position = parent
                parent = int(parent / 2)
            if not change:
                break
        idx += 1
    ans = 0
    pos = int(N / 2)
    while pos:
        ans += tree[pos]
        pos = int(pos / 2)
    print('#{} {}'.format(T, ans))
