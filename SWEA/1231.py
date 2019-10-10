import sys

sys.stdin = open('input.txt', 'r')


def inorder(node):
    if data[node][1]:
        inorder(data[node][1])
    print(data[node][0], end='')
    if data[node][2]:
        inorder(data[node][2])


for T in range(1, int(input()) + 1):
    N = int(input())
    data = [[0] * 3 for _ in range(N + 1)]
    for _ in range(N):
        d = list(input().split())
        d += [0, 0]
        idx = int(d[0])
        data[idx][0] = d[1]
        data[idx][1] = int(d[2])
        data[idx][2] = int(d[3])
    print("#{}".format(T), end=' ')
    inorder(1)
    print()
