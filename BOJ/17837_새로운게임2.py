import sys

sys.stdin = open('17837.txt', 'r')


def together(idx):
    global mal_table
    origin = mal_table[mals[idx][0]][mals[idx][1]]
    witch = origin.index(idx)
    temporary = origin[witch:]
    mal_table[mals[idx][0]][mals[idx][1]] = origin[:witch]
    return temporary


# 각 칸 별 이동 후 4개 이상 쌓였나 바로 확인
def white(idx, row, col):
    global mal_table, mals
    moving = together(idx)  # 옮길 말들의 idx가 넘어옴
    # 목적지로 이동할 때 moving에 있는 모든 말들의 좌표 바꿈: mals 수정,
    for mov in moving:
        mals[mov][0] = row
        mals[mov][1] = col
    # 그 말들을 위치로 이동: mal_table 수정
    mal_table[row][col] += moving
    # 크기가 4를 넘었는지 확인
    return True if len(mal_table[row][col]) >= 4 else False


def red(idx, row, col):
    global mal_table, mals
    moving = together(idx)
    moving = moving[::-1]
    for mov in moving:
        mals[mov][0] = row
        mals[mov][1] = col
    mal_table[row][col] += moving
    return True if len(mal_table[row][col]) >= 4 else False


def blue(idx, row, col):
    global mal_table, mals
    moving = together(idx)
    # 새로 갈 좌표
    new_row = 0
    new_col = 0
    # 이동하려는 방향을 바꿔줌
    direc = mals[idx][2]
    if direc == 1:
        mals[idx][2] = 2
        new_row = row
        new_col = col - 2
    elif direc == 2:
        mals[idx][2] = 1
        new_row = row
        new_col = col + 2
    elif direc == 3:
        mals[idx][2] = 4
        new_row = row + 2
        new_col = col
    elif direc == 4:
        mals[idx][2] = 3
        new_row = row - 2
        new_col = col
    mal_table[mals[idx][0]][mals[idx][1]] += moving
    if 0 <= new_row < N and 0 <= new_col < N:
        color = TABLE[new_row][new_col]
        if color == 0:
            return white(idx, new_row, new_col)
        elif color == 1:
            return red(idx, new_row, new_col)
        elif color == 2:
            return False
    else:
        return False


def solve(idx, row, col):
    if 0 <= row < N and 0 <= col < N:
        color = TABLE[row][col]
        if color == 0:
            return white(idx, row, col)
        elif color == 1:
            return red(idx, row, col)
        elif color == 2:
            return blue(idx, row, col)
    else:
        return blue(idx, row, col)


def check(idx, direc):
    if direc == 1:
        return solve(idx, mals[idx][0], mals[idx][1] + 1)
    elif direc == 2:
        return solve(idx, mals[idx][0], mals[idx][1] - 1)
    elif direc == 3:
        return solve(idx, mals[idx][0] - 1, mals[idx][1])
    elif direc == 4:
        return solve(idx, mals[idx][0] + 1, mals[idx][1])


N, K = map(int, input().split())
# 체스판 정보
TABLE = [list(map(int, input().split())) for _ in range(N)]
# 실제 말을 놓는 판
mal_table = [[[] for _ in range(N)] for __ in range(N)]
# 말 데이터베이스
mals = []
for _ in range(K):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    mals.append(temp)
for k in range(K):
    mal_table[mals[k][0]][mals[k][1]].append(k)

ans = 0
turn = 1
while turn < 1000:
    exceed = False
    for k in range(K):
        exceed = check(k, mals[k][2])
        if exceed:
            break
    if exceed:
        ans = turn
        break
    turn += 1
print(-1 if turn == 1000 else ans)