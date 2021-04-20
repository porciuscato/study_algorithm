def tree_init(arr, tree, left, right, node):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    else:
        tree[node] = min(
            tree_init(arr, tree, left, (left + right) // 2, node * 2 + 1),
            tree_init(arr, tree, (left + right) // 2 + 1, right, node * 2 + 2)
        )
        return tree[node]


def get_min(tree, start, end, left, right, node):
    if start > right or end < left:
        return MAX
    elif start <= left and right <= end:
        return tree[node]
    else:
        return min(
            get_min(tree, start, end, left, (left + right) // 2, node * 2 + 1),
            get_min(tree, start, end, (left + right)// 2 + 1, right, node * 2 + 2)
        )


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    arr = []
    N, M = map(int, sys_input().split())
    for _ in range(N):
        arr.append(int(sys_input()))

    s = 1
    while s < N:
        s *= 2
    tree = [0] * (s * 2)
    tree_init(arr, tree, 0, N - 1, 0)

    MAX = 1000000000

    for _ in range(M):
        a, b = map(int, sys_input().split())
        sys_print(f'{get_min(tree, a - 1, b - 1, 0, N - 1, 0)}\n')


