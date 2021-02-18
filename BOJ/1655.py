import sys

input = sys.stdin.readline

import heapq
from collections import deque


if __name__ == "__main__":
    N = int(input())
    list = []
    for i in range(1, N + 1):
        val = int(input())
        if i % 2:
            target = i // 2
        else:
            target = i // 2 - 1
        temp = deque()
        heapq.heappush(list, val)
        j = 0
        while j <= target:
            if j == target:
                result = heapq.heappop(list)
                heapq.heappush(list, result)
            else:
                temp.append(heapq.heappop(list))
            j += 1
        print(result)

        while temp:
            heapq.heappush(list, temp.popleft())
