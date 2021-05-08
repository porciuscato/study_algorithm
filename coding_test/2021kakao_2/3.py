MAX = 1000001
MIN = -1
N = ...


def tree_init(left, right, node):
    global tree
    if left == right:
        tree[node] = 1
        return tree[node]
    else:
        tree[node] = tree_init(left, (left + right) // 2, node * 2 + 1) + \
            tree_init((left + right) // 2 + 1, right, node * 2 + 2)
        return tree[node]


def tree_size(left, right, node):
    global tree
    if left == right:
        return node
    else:
        return max(
            tree_size(left, (left + right) // 2, node * 2 + 1),
            tree_size((left + right) // 2 + 1, right, node * 2 + 2)
        )


def tree_update(left, right, index, node, diff: int):
    if index < left or right < index:
        return
    tree[node] += diff
    if left != right:
        tree_update(left, (left + right) // 2, index, node * 2 + 1, diff)
        tree_update((left + right) // 2 + 1, right, index, node * 2 + 2, diff)


def find_min(left, right, index, node):
    '''
    index 보다 큰 최소값
    '''
    if right < index:
        return MAX
    if tree[node] == 0:
        return MAX
    if left == right:
        if status_table[left] == 'O':
            return left
        else:
            return MAX
    return min(
        find_min(left, (left + right) // 2, index, node * 2 + 1),
        find_min((left + right) // 2 + 1, right, index, node * 2 + 2)
    )


def find_max(left, right, index, node):
    '''
     index 보다 작은 최대값
    '''
    if index < left:
        return MIN
    if tree[node] == 0:
        return MIN
    if left == right:
        if status_table[left] == 'O':
            return right
        else:
            return MIN
    return max(
        find_max(left, (left + right) // 2, index, node * 2 + 1),
        find_max((left + right) // 2 + 1, right, index, node * 2 + 2)
    )


def sub_count(left, right, start, end, node):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return tree[node]
    return sub_count(left, (left + right) // 2, start, end, node * 2 + 1) + \
        sub_count((left + right) // 2 + 1, right, start, end, node * 2 + 2)


def move_up(left, right, target):
    vleft = left
    while True:
        value = sub_count(0, N - 1, vleft, right, 0)
        if value == target:
            if vleft > 0:
                left_value = sub_count(0, N - 1, vleft - 1, right, 0)
                if left_value == target:
                    vleft -= 1
                else:
                    # 정답
                    return vleft
            else:
                return vleft
        vleft -= 1


def move_down(left, right, target):
    vright = right
    while True:
        value = sub_count(0, N - 1, left, vright, 0)
        if value == target:
            if vright < N - 1:
                right_value = sub_count(0, N - 1, left, vright + 1, 0)
                if right_value == target:
                    vright += 1
                else:
                    return vright
            else:
                return vright
        vright += 1


def solution(n, k, cmd):
    global tree, N, status_table
    N = n
    status_table = ['O' for _ in range(n)]
    size = tree_size(0, n - 1, 0) + 1
    tree = [0] * size
    tree_init(0, n - 1, 0)

    delete_list = []
    pos = k

    for c in cmd:
        if len(c) == 3:
            oper, v = c.split()
            v = int(v)
            # 위로
            if oper == 'U':
                pos = move_up(pos - v, pos, v + 1)
            # 아래로
            else:
                pos = move_down(pos, pos + v, v + 1)
        else:
            # 삭제
            if c == 'C':
                delete_list.append(pos)
                status_table[pos] = 'X'
                tree_update(0, n - 1, pos, 0, -1)

                # 현재위치 조정
                result = find_min(0, n - 1, pos, 0)
                if result == MAX:
                    result = find_max(0, n - 1, pos, 0)
                pos = result
            # 복구
            else:
                recover = delete_list.pop()
                status_table[recover] = 'O'
                tree_update(0, n - 1, recover, 0, 1)

    return ''.join(status_table)


cases = [
    (8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]),
    (8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
]

for case in cases:
    print(solution(*case))
