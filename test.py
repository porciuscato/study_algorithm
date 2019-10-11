# 바이너리 트리를 구축한 다음에 삭제 연산을 구현해보자
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        self._append(self.root, data)

    def _append(self, node, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if data <= node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self._append(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self._append(node.right, data)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def delete(self, data):
        self._delete(self.root, self.root, data)

    def _delete(self, parent, sibling, data):
        # 부모노드를 반드시 알아야 한다
        # 지우려는 값이 노드와 동일할 경우
        if data == sibling.data:
            # 자식 노드가 몇개인지 봐야한다.
            # 자식이 둘 인 경우
            # 자식 노드가 없는 경우
            # 자식 노드가 하나인 경우
            pass
        # 지우려는 값이 노드와 다를 경우
        else:
            if data < parent.data:
                if parent.left.data == data:
                    return parent, parent.left
                else:
                    pass
            else:
                if parent.right.data == data:
                    return parent, parent.right
                else:
                    pass


lst = [58, 14, 12, 10, 40, 24, 15, 21, 32, 34, 40, 44, 52, 49, 51, 76, 60, 68, 64, 81]
tree = BST()
for item in lst:
    tree.append(item)
tree.preorder()
