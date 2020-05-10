from IPython import embed
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_node):
        self.root = root_node

    def get_root(self):
        return self.root

    def insert(self, value):
        now_node = self.root
        prev_node = now_node
        while now_node:
            prev_node = now_node
            if value < now_node.data:
                now_node = now_node.left
                left = 1
            else:
                now_node = now_node.right
                left = 0
        new_node = Node(value)
        new_node.parent = prev_node
        if left:
            prev_node.left = new_node
        else:
            prev_node.right = new_node

    def insert2(self, value):
        now_node = self.root
        while now_node:
            if value < now_node.data:
                if now_node.left is None:
                    new_node = Node(value)
                    now_node.left = new_node
                    new_node.parent = now_node
                    break
                else:
                    now_node = now_node.left
            else:
                if now_node.right is None:
                    new_node = Node(value)
                    now_node.right = new_node
                    new_node.parent = now_node
                    break
                else:
                    now_node = now_node.right

    def find_mx(self, node):
        now_node = node
        prev_node = now_node
        while now_node:
            prev_node = now_node
            now_node = now_node.right
        return prev_node

    def find_mn(self, node):
        now_node = node
        prev_node = now_node
        while now_node:
            prev_node = now_node
            now_node = now_node.left
        return prev_node

    def delete(self, value):
        now_node = self.root
        while now_node:
            if value == now_node.data:
                if now_node == self.root:
                    if now_node.left:
                        mx_node = self.find_mx(now_node.left)
                        mx_node.left = now_node.left
                        mx_node.right = now_node.right
                        if mx_node.parent.left == mx_node:
                            mx_node.parent.left = None
                        else:
                            mx_node.parent.right = None
                        self.root = mx_node
                    elif now_node.right:
                        mn_node = self.find_mn(now_node.right)
                        mn_node.left = now_node.left
                        mn_node.right = now_node.right
                        if mn_node.parent.left == mn_node:
                            mn_node.parent.left = None
                        else:
                            mn_node.parent.right = None
                        self.root = mn_node
                    else:
                        self.root = None
                    return value
                if now_node.left:
                    mx_node = self.find_mx(now_node.left)
                    mx_node.left = now_node.left
                    mx_node.right = now_node.right
                    if mx_node.parent.left == mx_node:
                        mx_node.parent.left = None
                    else:
                        mx_node.parent.right = None
                    if now_node.parent.left == now_node:
                        now_node.parent.left = mx_node
                    else:
                        now_node.parent.right = mx_node
                elif now_node.right:
                    mn_node = self.find_mn(now_node.right)
                    mn_node.left = now_node.left
                    mn_node.right = now_node.right
                    if mn_node.parent.left == mn_node:
                        mn_node.parent.left = None
                    else:
                        mn_node.parent.right = None
                    if now_node.parent.left == now_node:
                        now_node.parent.left = mn_node
                    else:
                        now_node.parent.right = mn_node
                else:
                    if now_node.parent.left.data == value:
                        now_node.parent.left = None
                    else:
                        now_node.parent.right = None
                return value
            elif value < now_node.data:
                now_node = now_node.left
            else:
                now_node = now_node.right

    def for_preorder(self, node, arr):
        if node is None:
            return
        arr.append(node.data)
        # print(node.data, end=' ')
        self.for_preorder(node.left, arr)
        self.for_preorder(node.right, arr)
        return arr

    def for_inorder(self, node, arr):
        if node is None:
            return
        self.for_inorder(node.left, arr)
        arr.append(node.data)
        # print(node.data, end=' ')
        self.for_inorder(node.right, arr)
        return arr

    def for_postortder(self, node, arr):
        if node is None:
            return
        self.for_postortder(node.left, arr)
        self.for_postortder(node.right, arr)
        arr.append(node.data)
        # print(node.data, end=' ')
        return arr

    def preorder(self):
        return self.for_preorder(self.root, [])

    def inorder(self):
        return self.for_inorder(self.root, [])

    def postorder(self):
        return self.for_postortder(self.root, [])


node = Node(30)
tree = BinaryTree(node)
ar = [15, 45, 8, 20, 4, 12, 17, 24, 38, 56, 33, 42, 48, 60]
# for i in range(10):
#     v = random.randint(1, 100)
#     tree.insert(v)

for a in ar:
    tree.insert(a)


# print(tree.find_mx(tree.root).data)
# print(tree.find_mn(tree.root).data)

print(tree.preorder())
print(tree.inorder())
print(tree.postorder())

