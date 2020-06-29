import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def main():
    import random
    N = 50
    crains = [random.randint(1, 1000000) for _ in range(N)]
    M = 10000
    i_boxes = [random.randint(900000, 950000) for __ in range(M)]
    # N = int(input())
    # crains = list(map(int, input().split()))
    # M = int(input())
    # i_boxes = list(map(int, input().split()))
    crains.sort(reverse=True)
    boxes = []
    for i_box in i_boxes:
        heappush(boxes, (-i_box, i_box))
    if crains[0] < boxes[0][1]:
        return -1
    ans = 0
    while boxes:
        temp = []
        for crain in crains:
            while True:
                if boxes:
                    first = heappop(boxes)
                    mx = first[1]
                    if crain >= mx:
                        break
                    else:
                        temp.append(mx)
                elif not temp:
                    ans += 1
                    return ans
                else:
                    break
        for ele in temp:
            heappush(boxes, (-ele, ele))
        ans += 1
    return ans


print(main())

# 4
# 6 8 9 2
# 10
# 3 5 3 4 7 9 1 1 2 1
