import sys
sys.setrecursionlimit(1500)

class Node:
    def __init__(self, x, num):
        self.x = x
        self.num = num
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None
        self.preorder_list = []
        self.postorder_list = []

    def push(self, x, num):
        if self.head is None:
            self.head = Node(x, num)
        else:
            now = self.head
            while True:
                if x < now.x:
                    if now.left is None:
                        now.left = Node(x, num)
                        break
                    else:
                        now = now.left
                else:
                    if now.right is None:
                        now.right = Node(x, num)
                        break
                    else:
                        now = now.right

    def for_preorder(self, node):
        if node is None:
            return
        self.preorder_list.append(node.num)
        self.for_preorder(node.left)
        self.for_preorder(node.right)

    def for_postorder(self, node):
        if node is None:
            return
        self.for_postorder(node.left)
        self.for_postorder(node.right)
        self.postorder_list.append(node.num)

    def preorder(self):
        self.for_preorder(self.head)
        return self.preorder_list

    def postorder(self):
        self.for_postorder(self.head)
        return self.postorder_list


def solution(nodeinfo):
    for idx in range(len(nodeinfo)):
        nodeinfo[idx].append(idx + 1)
    nodeinfo.sort(key=lambda x:(-x[1], x[0]))

    tree = Tree()
    for node in nodeinfo:
        tree.push(node[0], node[2])

    return [tree.preorder(), tree.postorder()]

cases = [
    [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
]

for case in cases:
    print(solution(case))
