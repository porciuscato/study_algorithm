def inorder(node):
    global ans
    if node:
        inorder(tree[node][0])
        ans += 1
        inorder(tree[node][1])


for T in range(1, int(input()) + 1):
    ans = 0
    E, N = map(int, input().split())
    tree = [[0] * 2 for _ in range(E + 2)]
    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        if not tree[data[i]][0]:
            tree[data[i]][0] = data[i + 1]
        else:
            tree[data[i]][1] = data[i + 1]
    inorder(N)
    print('#{} {}'.format(T, ans))
