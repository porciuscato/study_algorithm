from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())
maxheap, minheap = [], []
for i in range(N):
    num = int(input())
    if not i % 2:
        heappush(maxheap, (-num, num))
    else:
        heappush(minheap, (num, num))
    if i >= 1 and maxheap[0][1] > minheap[0][1]:
        _, big = heappop(maxheap)
        _, sml = heappop(minheap)
        heappush(minheap, (big, big))
        heappush(maxheap, (-sml, sml))
    print(maxheap[0][1])
