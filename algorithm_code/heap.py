from heapq import heappush, heappop

hip = []
arr = [1, 4, 7, 8, 3, 3, 1, 13, 4]

for i in arr:
    heappush(hip, i)

while hip:
    print(heappop(hip))
