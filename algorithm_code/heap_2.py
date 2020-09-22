from collections import deque


def heappush(heap: deque, n):
    idx = len(heap)
    heap.append(n)
    while idx:
        if idx % 2:
            parent = idx // 2
        else:
            parent = idx // 2 - 1
        if heap[parent] > heap[idx]:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break


def heappop(heap: deque):
    if heap:
        ret_val = heap.popleft()
        if heap:
            last = heap[-1]
            heap.appendleft(last)
            heap.pop()
            length = len(heap)
            idx = 0
            while True:
                left = idx * 2 + 1
                right = idx * 2 + 2
                if left >= length:
                    break
                if right >= length:
                    if heap[idx] > heap[left]:
                        heap[idx], heap[left] = heap[left], heap[idx]
                        idx = left
                    else:
                        break
                else:
                    sm = left if heap[left] < heap[right] else right
                    if heap[idx] > heap[sm]:
                        heap[idx], heap[sm] = heap[sm], heap[idx]
                        idx = sm
                    else:
                        break
        return ret_val
    else:
        return


heap = deque([])
arr = [1, 4, 7, 8, 3, 3, 1, 13, 4, 2]

for i in arr:
    heappush(heap, i)

print(heap)

while heap:
    print(heappop(heap))
