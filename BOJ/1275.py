def tree_init(left, right, node, arr, tree):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    else:
        tree[node] = \
            tree_init(left, (left + right) // 2, node * 2 + 1, arr, tree) + \
            tree_init((left + right) // 2 + 1, right, node * 2 + 2, arr, tree)
        return tree[node]


def get_subsum(start, end, left, right, node, arr, tree):
    if end < left or right < start:
        return 0
    elif start <= left and right <= end:
        return tree[node]
    else:
        return (
            get_subsum(start, end, left, (left + right) // 2, node * 2 + 1, arr, tree) +
            get_subsum(start, end, (left + right) // 2 + 1, right, node * 2 + 2, arr, tree)
        )


def update(index, val, left, right, node, arr, tree):
    if index < left or right < index:
        return
    else:
        tree[node] += val
        if left != right:
            update(index, val, left, (left + right) // 2, node * 2 + 1, arr, tree)
            update(index, val, (left + right) // 2 + 1, right, node * 2 + 2, arr, tree)


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [0] * 262141
    tree_init(0, N - 1, 0, arr, tree)

    for _ in range(Q):
        x, y, a, b = map(int, sys_input().split())
        if x > y:
            x, y = y, x
        sys_print(f'{get_subsum(x - 1, y - 1, 0, N - 1, 0, arr, tree)}\n')
        vari = b - arr[a - 1]
        update(a - 1, vari, 0, N - 1, 0, arr, tree)
        arr[a - 1] = b
