def tree_init(arr, tree, left, right, node=0):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    else:
        tree[node] = (
                             tree_init(arr, tree, left, (left + right) // 2, node * 2 + 1) *
                             tree_init(arr, tree, (left + right) // 2 + 1, right, node * 2 + 2)
                     ) % divisor
        return tree[node]


def update(index, val, left, right, arr, tree, node=0):
    if index < left or right < index:
        return tree[node]
    elif left == right:
        tree[node] = val
        return tree[node]
    else:
        tree[node] = (
                             update(index, val, left, (left + right) // 2, arr, tree, node * 2 + 1) *
                             update(index, val, (left + right) // 2 + 1, right, arr, tree, node * 2 + 2)
                     ) % divisor
        return tree[node]


def sub_mul(tree, start, end, left, right, node=0):
    if end < left or right < start:
        return 1
    elif start <= left and right <= end:
        return tree[node]
    else:
        return (
                       sub_mul(tree, start, end, left, (left + right) // 2, node * 2 + 1) *
                       sub_mul(tree, start, end, (left + right) // 2 + 1, right, node * 2 + 2)
               ) % divisor


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    N, M, K = map(int, sys_input().split())
    arr = []
    for _ in range(N):
        arr.append(int(sys_input()))

    divisor = 1000000007

    tree = [0] * 2097149
    tree_init(arr, tree, 0, N - 1)

    for _ in range(M + K):
        a, b, c = map(int, sys_input().split())
        if a == 1:
            update(b - 1, c, 0, N - 1, arr, tree)
            arr[b - 1] = c
        else:
            sys_print(f'{sub_mul(tree, b - 1, c - 1, 0, N - 1)}\n')

# 3 1 1
# 1
# 2
# 3
# 1 2 5
# 2 1 3


