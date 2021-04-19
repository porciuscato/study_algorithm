class SegmentTree:
    def __init__(self, arr: list):
        '''
        self.tree는 각 구간 별 최소, 최대값을 가지고 있다.
        '''
        self.arr = arr
        self.tree = [(0, 0)] * self.__get_tree_size(len(arr))
        self.__tree_init(self.arr, self.tree, 0, len(self.arr) - 1)

    def __get_tree_size(self, size):
        s = 1
        while s < size:
            s *= 2
        return s * 2

    def __tree_init(self, arr, tree, left, right, node=0) -> tuple:
        '''
        해당 구간의 최소, 최대값을 설정한다.
        '''
        if left == right:
            tree[node] = (arr[left], arr[left])
            return tree[node]
        else:
            l_node = self.__tree_init(arr, tree, left, (left + right) // 2, node * 2 + 1)
            r_node = self.__tree_init(arr, tree, (left + right) // 2 + 1, right, node * 2 + 2)
            tree[node] = (min(l_node[0], r_node[0]), max(l_node[1], r_node[1]))
            return tree[node]

    def get_min_max(self, start, end, left, right, tree, node=0) -> tuple:
        if end < left or right < start:
            return None, None
        elif start <= left and right <= end:
            return tree[node]
        else:
            l_node = self.get_min_max(start, end, left, (left + right) // 2, self.tree, node * 2 + 1)
            r_node = self.get_min_max(start, end, (left + right) // 2 + 1, right, self.tree, node * 2 + 2)
            try:
                return min(l_node[0], r_node[0]), max(l_node[1], r_node[1])
            except TypeError:
                return l_node if r_node[0] is None else r_node


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    N, M = map(int, sys_input().split())
    arr = []
    for _ in range(N):
        arr.append(int(sys_input()))

    seg_tree = SegmentTree(arr)

    for _ in range(M):
        a, b = map(int, sys_input().split())
        res = seg_tree.get_min_max(a - 1, b - 1, 0, N - 1, seg_tree.tree)
        sys_print(f'{res[0]} {res[1]}\n')
