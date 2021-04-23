def tree_init(left, right, node):
    global tree
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    else:
        tree[node] = min(
            tree_init(left, (left + right) // 2, node * 2 + 1),
            tree_init((left + right) // 2 + 1, right, node * 2 + 2)
        )
        return tree[node]


def get_mn(start, end, left, right, node):
    if end < left or right < start:
        return MAX
    elif start <= left and right <= end:
        return tree[node]
    else:
        return min(
            get_mn(start, end, left, (left + right) // 2, node * 2 + 1),
            get_mn(start, end, (left + right) // 2 + 1, right, node * 2 + 2)
        )


def update(index, val, left, right, node):
    global tree
    if index < left or right < index:
        return tree[node]
    if left == right:
        tree[node] = val
        return tree[node]
    else:
        tree[node] = min(
            update(index, val, left, (left + right) // 2, node * 2 + 1),
            update(index, val, (left + right) // 2 + 1, right, node * 2 + 2)
        )
    return tree[node]


if __name__ == "__main__":
    import sys

    s_input = sys.stdin.readline
    s_print = sys.stdout.write

    MAX = 1000000001
    N = int(s_input())
    arr = list(map(int, s_input().split()))

    s = 1
    while s < N:
        s *= 2
    tree = [0] * (s * 2)
    tree_init(0, N - 1, 0)

    M = int(s_input())
    for _ in range(M):
        a, i, j = map(int, s_input().split())
        if a == 1:
            update(i - 1, j, 0, N - 1, 0)
            arr[i - 1] = j
        else:
            s_print(f'{get_mn(i - 1, j - 1, 0, N - 1, 0)}\n')
