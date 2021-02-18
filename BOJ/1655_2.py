import sys

input = sys.stdin.readline

import heapq
from collections import deque


if __name__ == "__main__":
    N = int(input())
    list = []
    for i in range(1, N + 1):
        num = int(input())
        if i % 2:
            target = i // 2
        else:
            target = i // 2 - 1
        list.append(num)
        list.sort()
        print(list[target])

