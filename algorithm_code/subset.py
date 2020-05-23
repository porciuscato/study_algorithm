from collections import deque


def subset(array):
    for i in range(1 << len(array)):
        temp = deque([])
        for j in range(len(array)):
            if i & (1 << j):
                temp.append(array[j])
        print(temp)

