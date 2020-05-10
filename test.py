from heapq import heappush, heappop, heapify
import random


data = []
for i in range(10):
    data.append(random.randint(1, 100))

heapify(data)
print(data)

while data:
    print(heappop(data))

