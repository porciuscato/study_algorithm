class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def search(self, node, parent):
        if node.data == parent:
            return node
        if not node.left and not node.right:
            return
        else:
            if node.left:
                self.search(node.left, parent)
            if node.right:
                self.search(node.right, parent)

    def append(self, parent, data):
        if not self.root:
            node = Node(parent)
            self.root = node
        par = self.search(self.root, parent)  # root는 시작점. 여기서부터 parent를 찾자.
        if par:
            node = Node(data)
            if not par.left:
                par.left = node
            else:
                par.right = node

    def preorder(self, node):
        if node.data:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node.data:
            self.preorder(node.left)
            print(node.data, end=' ')
            self.preorder(node.right)

    def postorder(self, node):
        if node.data:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.data, end=' ')


data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
tree = Tree()
for d in range(0, len(data), 2):
    tree.append(data[d], data[d + 1])
tree.preorder()
