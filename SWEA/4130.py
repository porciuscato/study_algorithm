import sys

sys.stdin = open("4130.txt", 'r')

from collections import deque


def solve(num, direc, wheels):
    rotate_info = [0, 0, 0, 0]
    now = num - 1
    rotate_info[now] = direc
    if num == 1:
        # 아래로 가며 체크
        nxt = 1
        while nxt < 4:
            if rotate_info[now] != 0:
                if wheels[now][2] != wheels[nxt][6]:
                    rotate_info[nxt] = rotate_info[now] * -1
            now += 1
            nxt += 1
    elif num == 2:
        # 위로 한 칸, 아래로 두 칸
        if wheels[now][6] != wheels[0][2]:
            rotate_info[0] = rotate_info[now] * -1
        nxt = 2
        while nxt < 4:
            if rotate_info[now] != 0:
                if wheels[now][2] != wheels[nxt][6]:
                    rotate_info[nxt] = rotate_info[now] * -1
            now += 1
            nxt += 1
    elif num == 3:
        # 위로 두 칸, 아래로 한 칸
        if wheels[now][2] != wheels[3][6]:
            rotate_info[3] = rotate_info[now] * -1
        nxt = 1
        while nxt >= 0:
            if rotate_info[now] != 0:
                if wheels[now][6] != wheels[nxt][2]:
                    rotate_info[nxt] = rotate_info[now] * -1
            now -= 1
            nxt -= 1
    elif num == 4:
        nxt = 2
        while nxt >= 0:
            if rotate_info[now] != 0:
                if wheels[now][6] != wheels[nxt][2]:
                    rotate_info[nxt] = rotate_info[now] * -1
            now -= 1
            nxt -= 1
    for i in range(4):
        if rotate_info[i] == 1:
            wheels[i].rotate()
        elif rotate_info[i] == -1:
            wheels[i].rotate(-1)


for T in range(1, int(input()) + 1):
    K = int(input())
    data = deque([deque(list(map(int, input().split()))) for _ in range(4)])
    for _ in range(K):
        n, d = map(int, input().split())
        solve(n, d, data)
    answer = 0
    for pow in range(4):
        if data[pow][0]:
            answer += 2 ** pow
    print("#{} {}".format(T, answer))
