class SegmentTree:
    def __init__(self, arr: list):
        self.arr = arr
        self.__tree_size = self.__get_tree_size(len(self.arr))
        self.tree = [0] * self.__tree_size
        self.__tree_init(self.arr, self.tree, 0, len(self.arr) - 1)

    def __get_tree_size(self, size) -> int:
        s = 1
        while s < size:
            s *= 2
        return s * 2

    def __tree_init(self, arr: list, tree: list, left: int, right: int, node: int = 0):
        if left == right:
            tree[node] = arr[left]
            return tree[node]
        else:
            tree[node] = self.__tree_init(arr, tree, left, (left + right) // 2, node * 2 + 1) + \
                        self.__tree_init(arr, tree, (left + right) // 2 + 1, right, node * 2 + 2)
            return tree[node]

    def get_subsum(self, start: int, end: int, tree: list = None, left: int = None, right: int = None, node: int = 0):
        if tree is None:
            tree = self.tree
        if left is None:
            left = 0
        if right is None:
            right = len(self.arr) - 1

        if end < left or right < start:
            return 0
        elif start <= left and right <= end:
            return tree[node]
        else:
            return self.get_subsum(start, end, tree, left, (left + right) // 2, node * 2 + 1) + \
                    self.get_subsum(start, end, tree, (left + right) // 2 + 1, right, node * 2 + 2)

    def update(self, index: int, val, tree: list = None, left: int = None, right: int = None, node: int = 0) -> None:
        '''
        :param val: 해당 index 에 새로 바꿀 값
        '''
        if tree is None:
            tree = self.tree
        if left is None:
            left = 0
        if right is None:
            right = len(self.tree) - 1

        if index < left or right < index:
            return
        tree[node] += val - self.arr[index]
        if left != right:
            self.update(index, val, tree, left, (left + right) // 2, node * 2 + 1)
            self.update(index, val, tree, (left + right) // 2 + 1, right, node * 2 + 2)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seg_tree = SegmentTree(arr)
    print(seg_tree.tree)
    print(seg_tree.get_subsum(2, 3))
