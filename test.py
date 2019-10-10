def preorder(node):
    print(node, end=' ')
    if graph[node][0]:
        preorder(graph[node][0])
    if graph[node][1]:
        preorder(graph[node][1])


def inorder(node):
    if graph[node][0]:
        inorder(graph[node][0])
    print(node, end=' ')
    if graph[node][1]:
        inorder(graph[node][1])


def postorder(node):
    if graph[node][0]:
        postorder(graph[node][0])
    if graph[node][1]:
        postorder(graph[node][1])
    print(node, end=' ')


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def append(self, parent, data):
        if not self.root:
            node = Node(data)
            self.root = node
        else:
            # parent를 찾아라.


data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
graph = [[0] * 3 for _ in range(max(data) + 1)]

# for d in range(0, len(data), 2):
#     a = data[d]
#     b = data[d + 1]
#     if graph[a][0] == 0:
#         graph[a][0] = b
#     else:
#         graph[a][1] = b
#     graph[b][2] = a
#
# print('pre  : ', end=' ')
# preorder(1)
# print()
# print('in   : ', end=' ')
# inorder(1)
# print()
# print('post : ', end=' ')
# postorder(1)
