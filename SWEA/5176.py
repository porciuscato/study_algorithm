# import sys
#
# sys.stdin = open('input.txt', 'r')


def inorder(node):
    global temp
    if node:
        inorder(tree[node][1])
        temp.append(node)
        inorder(tree[node][2])


for T in range(1, int(input()) + 1):
    N = int(input())
    # 중위 순회로 돌자
    tree = [[i, 0, 0] for i in range(0, N + 1)]
    for i in range(1, N + 1):
        t1 = i * 2
        t2 = i * 2 + 1
        if t1 <= N:
            tree[i][1] = t1
        if t2 <= N:
            tree[i][2] = t2
    temp = []
    inorder(1)
    print(temp)
    print('#{} {} {}'.format(T, temp.index(1) + 1, temp.index(int(N / 2)) + 1))
