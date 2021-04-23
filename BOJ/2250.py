def count_siblings(now: int, dep: int) -> int:
    global database, depth
    if table[now][0] == -1 and table[now][1] == -1:
        database[now] = {
            'l_sibs': 0,
            'depth': dep
        }
        depth = max(depth, dep)
        return 1
    else:
        l_siblings = 0
        r_siblings = 0

        l_sib = table[now][0]
        r_sib = table[now][1]
        if l_sib != -1:
            l_siblings += count_siblings(l_sib, dep + 1)
        if r_sib != -1:
            r_siblings += count_siblings(r_sib, dep + 1)

        database[now] = {
            'l_sibs': l_siblings,
            'depth': dep
        }
        return l_siblings + r_siblings + 1


def find_pos(now, left, right) -> None:
    global database, position_table
    pos = left + database[now]['l_sibs']
    # database[now]['pos'] = pos

    l_sib = table[now][0]
    r_sib = table[now][1]
    if l_sib != -1:
        find_pos(l_sib, left, pos - 1)
    if r_sib != -1:
        find_pos(r_sib, pos + 1, right)

    position_table[database[now]['depth']][pos] = now


def find_root(table) -> int:
    for i in range(1, N + 1):
        l_sib = table[i][0]
        r_sib = table[i][1]
        if l_sib != -1:
            table[l_sib][2] = i
        if r_sib != -1:
            table[r_sib][2] = i

    for i in range(1, N + 1):
        if table[i][2] == 0:
            return i


if __name__ == "__main__":
    import sys

    s_input = sys.stdin.readline
    s_print = sys.stdout.write

    N = int(s_input())

    table = [[0, 0, 0] for _ in range(N + 1)]
    for _ in range(N):
        n, l, r = map(int, s_input().split())
        table[n] = [l, r, 0]  # left_sib, right_sib, parent

    root = find_root(table)

    database = {}
    depth = 0
    count_siblings(root, 1)

    position_table = [[0 for _ in range(N + 1)] for __ in range(depth + 1)]
    find_pos(root, 1, N)

    mx_idx = 0
    mx_val = 0
    for d in range(1, depth + 1):
        start = 0
        end = N + 1
        t = position_table[d]
        for le in range(1, N + 1):
            if t[le] > 0:
                start = le
                break
        for ri in range(N, 0, -1):
            if t[ri] > 0:
                end = ri
                break
        val = end - start + 1
        if val > mx_val:
            mx_idx = d
            mx_val = val

    s_print(f'{mx_idx} {mx_val}\n')
