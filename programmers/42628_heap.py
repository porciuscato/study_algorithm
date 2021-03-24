from heapq import heappush, heappop


def solution(operations):
    mx_heap, mn_heap = [], []
    for oper in operations:
        if oper == "D 1":
            if mx_heap:
                heappop(mx_heap)
                if mx_heap == [] or -mx_heap[0] < mn_heap[0]:
                    mx_heap = []
                    mn_heap = []
                pass
        elif oper == "D -1":
            if mn_heap:
                heappop(mn_heap)
                if mn_heap == [] or -mx_heap[0] < mn_heap[0]:
                    mx_heap = []
                    mn_heap = []
        else:
            num = int(oper[2:])
            heappush(mn_heap, num)
            heappush(mx_heap, -num)

    return [-mx_heap[0], mn_heap[0]] if mn_heap else [0, 0]



import random


# chars = ["I ", "D "]
# sample = []
# for _ in range(1000000):
#     char = random.randint(0, 1)
#     if char == 0:
#         sample.append(chars[char] + str(random.randint(-10000, 10000)))
#     else:
#         sample.append(chars[char] + str(random.randint(0, 1)))

cases = [
    ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],  # [0, 0]
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"],  # [333, -45]
    # [chars[random.randint(0, 1)] + str(random.randint(-1000000, 1000000)) for _ in range(1000000)],
    # ['I -9914', 'I 7273', 'I -5679', 'D 1', 'I -4308', 'I 7547', 'I 4819', 'I -1522', 'D 1', 'I -2369'],
    # sample
]

for case in cases:
    print(solution(case))

