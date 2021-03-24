from collections import deque


def find_spot(deq: deque, left, right, num: int):
    # binary search
    if num < deq[left]: return left - 1
    if num > deq[right]: return right + 1

    mid = (left + right) // 2
    if num == deq[mid]:
        return mid
    elif num < deq[mid]:
        return find_spot(deq, left, mid - 1, num)
    else:
        return find_spot(deq, mid + 1, right, num)


def input_num(deq: deque, num: int):
    length = len(deq)
    if length == 0:
        deq.append(num)
    elif length == 1:
        if num <= deq[0]:
            deq.appendleft(num)
        else:
            deq.append(num)
    else:
        if num <= deq[0]:
            deq.appendleft(num)
        elif num >= deq[-1]:
            deq.append(num)
        else:
            pos = find_spot(deq, 0, len(deq) - 1, num)
            l = list(deq)
            deq = deque(l[0:pos + 1] + [num] + l[pos:])


def solution(operations):
    deq = deque([])
    for operation in operations:
        oper, num = operation.split(" ")
        if oper == "I":
            input_num(deq, int(num))
        else:
            if deq:
                if num == "1":
                    deq.pop()
                else:
                    deq.popleft()

    return [deq[-1], deq[0]] if deq else [0, 0]



import random
chars = ["I ", "D "]
sample = []
for _ in range(1000000):
    char = random.randint(0, 1)
    if char == 0:
        sample.append(chars[char] + str(random.randint(-10000, 10000)))
    else:
        sample.append(chars[char] + str(random.randint(0, 1)))

cases = [
    # ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
    # ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"],
    # [chars[random.randint(0, 1)] + str(random.randint(-1000000, 1000000)) for _ in range(1000000)],
    # ['I -9914', 'I 7273', 'I -5679', 'D 1', 'I -4308', 'I 7547', 'I 4819', 'I -1522', 'D 1', 'I -2369'],
    sample
]

for case in cases:
    print(solution(case))

