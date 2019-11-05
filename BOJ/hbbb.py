from collections import deque

import sys
sys.stdin = open('input.txt', 'r')


R, C, M = map(int, input().split())
shark = [[deque() for _ in range(C + 1)] for _ in range(R + 1)]
shark[0] = [0] * (C + 1)
for i in range(R + 1):
    shark[i][0] = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[r][c].append([s, d, z])
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]


def find_dist(x, direction):
    if direction in [1, 2]:
        x %= ((R - 1) * 2)
    else:
        x %= ((C - 1) * 2)
    return x


def find_point(direction, flag, dist, init_val1, init_val2, val):
    while True:
        if flag:
            moving = abs(val - init_val1)
            if moving < dist:
                dist -= moving
                val += dy[direction] * moving
                val += dx[direction] * moving
                flag = not flag
            else:
                val += dy[direction] * dist
                val += dx[direction] * dist
                return val, flag
        else:
            moving = abs(val - init_val2)
            if moving < dist:
                dist -= moving
                val -= dy[direction] * moving
                val -= dx[direction] * moving
                flag = not flag
            else:
                val -= dy[direction] * dist
                val -= dx[direction] * dist
                return val, flag


def move(y, x, velocity, direction, size):
    next_y, next_x = y, x
    dist = find_dist(velocity, direction)

    if direction == 1:
        value = next_y - dist
        if 1 <= value <= R:
            next_y = value
        elif 2 - R <= value < 1:
            shark[y][x][0][1] = 2
            next_y = 2 - value
        else:
            next_y = value + 2 * (R - 1)
    elif direction == 2:
        value = next_y + dist
        if 1 <= value <= R:
            next_y = value
        elif R < value <= 2 * R - 1:
            shark[y][x][0][1] = 1
            next_y = 2 * R - value
    elif direction == 3:
        value = next_x + dist
        if 1 <= value <= C:
            next_x = value
        elif C < value <= 2 * C - 1:
            shark[y][x][0][1] = 4
            next_x = 2 * C - value
        else:
            next_x = value - 2 * (C - 1)
    else:
        value = next_x - dist
        if 1 <= value <= C:
            next_x = value
        elif 2 - C <= value < 1:
            shark[y][x][0][1] = 3
            next_x = 2 - value
        else:
            next_x = value + 2 * (C - 1)
    if shark[next_y][next_x]:
        eat_candi.append((next_y, next_x))
    shark[next_y][next_x].append(shark[y][x].popleft())


total_size = 0
for i in range(1, C + 1):
    # 상어 잡기
    for j in range(1, R + 1):
        if shark[j][i]:
            total_size += shark[j][i].pop()[2]
            break
    # 상어 이동
    points = []
    for j in range(1, R + 1):
        for k in range(1, C + 1):
            if shark[j][k]:
                points.append((j, k))
    eat_candi = []
    for j, k in points:
        move(j, k, shark[j][k][0][0], shark[j][k][0][1], shark[j][k][0][2])
    # 상어 잡아먹기
    for j, k in eat_candi:
        shark[j][k] = deque([max(shark[j][k], key=lambda x: x[2])])
print(total_size)
