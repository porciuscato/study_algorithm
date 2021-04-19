class SegmentTree:
    def __init__(self, arr: list):
        self.arr = arr
        self.__tree_size = self.__get_tree_size(len(self.arr))
        self.tree = [0] * self.__tree_size
        self.__tree_init(self.arr, 0, len(self.arr) - 1, self.tree)

    def __get_tree_size(self, size):
        s = 1
        while s < size:
            s *= 2
        return s * 2

    def __tree_init(self, arr, left, right, tree, node=0):
        if left == right:
            tree[node] = arr[left]
            return tree[node]
        else:
            tree[node] = self.__tree_init(arr, left, (left + right) // 2, tree, node * 2 + 1) + \
                        self.__tree_init(arr, (left + right) // 2 + 1, right, tree, node * 2 + 2)
            return tree[node]

    def sub_sum(self, start, end, left, right, tree, node=0):
        if end < left or start > right:
            return 0
        elif start <= left and right <= end:
            return tree[node]
        else:
            return self.sub_sum(start, end, left, (left + right) // 2, tree, node * 2 + 1) + \
                    self.sub_sum(start, end, (left + right) // 2 + 1, right, tree, node * 2 + 2)

    def update(self, index, val, left, right, arr, tree, node=0):
        if index < left or index > right:
            return
        tree[node] += val - arr[index]
        if left != right:
            self.update(index, val, left, (left + right) // 2, arr, tree, node * 2 + 1)
            self.update(index, val, (left + right) // 2 + 1, right, arr, tree, node * 2 + 2)


if __name__ == "__main__":
    import sys

    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    N, M, K = map(int, sys_input().split())
    arr = []
    for _ in range(N):
        arr.append(int(sys_input()))
    seg_tree = SegmentTree(arr)
    for _ in range(M + K):
        a, b, c = map(int, sys_input().split())
        if a == 1:
            seg_tree.update(b - 1, c, 0, len(seg_tree.arr) - 1, seg_tree.arr, seg_tree.tree)
            seg_tree.arr[b - 1] = c
        else:
            result = seg_tree.sub_sum(b - 1, c - 1, 0, len(seg_tree.arr) - 1, seg_tree.tree)
            sys_print(f'{result}\n')
