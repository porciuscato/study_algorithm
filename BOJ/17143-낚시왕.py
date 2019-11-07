import sys

sys.stdin = open('17143.txt', 'r')


def clear():
    global sharks, ocean, how_many
    for row in range(1, R + 1):
        for col in range(1, C + 1):
            if how_many[row][col] >= 2:
                fishes = []
                # 같은 위치에 있는 상어들을 넣어
                for i in range(1, M + 1):
                    if sharks[i][0] == row and sharks[i][1] == col:
                        fishes.append(i)
                # print(fishes)
                mx = 0
                for i in range(1, len(fishes)):
                    if sharks[fishes[mx]][4] < sharks[fishes[i]][4]:
                        mx = i
                for i in range(len(fishes)):
                    if i != mx:
                        sharks[fishes[i]][5] = 0
                ocean[row][col] = fishes[mx]
                how_many[row][col] = 1


def moves():
    global sharks, ocean, how_many
    # i는 상어의 id
    for i in range(1, M + 1):
        if sharks[i][5]:
            # 원래 있던 자리에서 빼
            shark_row = sharks[i][0]
            shark_col = sharks[i][1]
            ocean[shark_row][shark_col] -= i
            how_many[shark_row][shark_col] -= 1
            direction = sharks[i][3]
            if direction == 1:
                value = sharks[i][0] - sharks[i][2] % ((R - 1) * 2)
                if 1 < value <= R:
                    sharks[i][0] = value
                elif 2 - R < value <= 1:
                    sharks[i][3] = 2
                    sharks[i][0] = 2 - value
                else:
                    sharks[i][0] = value + 2 * (R - 1)
            elif direction == 2:
                value = sharks[i][0] + sharks[i][2] % ((R - 1) * 2)
                if 1 <= value < R:
                    sharks[i][0] = value
                elif R <= value < 2 * R - 1:
                    sharks[i][3] = 1
                    sharks[i][0] = 2 * R - value
                else:
                    sharks[i][0] = value - 2 * (R - 1)
            elif direction == 3:
                value = sharks[i][1] + sharks[i][2] % ((C - 1) * 2)
                if 1 <= value < C:
                    sharks[i][1] = value
                elif C <= value < 2 * C - 1:
                    sharks[i][3] = 4
                    sharks[i][1] = 2 * C - value
                else:
                    sharks[i][1] = value - 2 * (C - 1)
            elif direction == 4:
                value = sharks[i][1] - sharks[i][2] % ((C - 1) * 2)
                if 1 < value <= C:
                    sharks[i][1] = value
                elif 2 - C < value <= 1:
                    sharks[i][3] = 3
                    sharks[i][1] = 2 - value
                else:
                    sharks[i][1] = value + 2 * (C - 1)
            ocean[sharks[i][0]][sharks[i][1]] += i
            how_many[sharks[i][0]][sharks[i][1]] += 1


def fishing(king):
    global ans, sharks, ocean, how_many
    for row in range(1, R + 1):
        if ocean[row][king]:
            # 상어 id
            num = ocean[row][king]
            # print(num)
            ans += sharks[num][4]
            ocean[row][king] = 0
            sharks[num][5] = 0
            how_many[row][king] = 0
            return


R, C, M = map(int, input().split())
# 격자판
ocean = [[0] * (C + 1) for _ in range(R + 1)]
# 동일한 위치에 상어가 몇 마리 있는지
how_many = [[0] * (C + 1) for _ in range(R + 1)]
# 상어들의 정보 row, col, speed, direc, size, alive / 첫줄을 0으로
sharks = [[0, 0, 0, 0, 0, 0]]
for _ in range(M):
    temp = list(map(int, input().split()))
    temp.append(1)
    sharks.append(temp)

# ocean에 상어위치 초기화
for i in range(1, M + 1):
    r = sharks[i][0]
    c = sharks[i][1]
    ocean[r][c] = i
    how_many[r][c] += 1
ans = 0
king = 1
while king <= C:
    fishing(king)
    moves()
    clear()
    king += 1
    # for rrow in range(1, R + 1):
    #     for ccol in range(1, C + 1):
    #         print(ocean[rrow][ccol], end=' ')
    #     print()
    # print()
    #############
    # for rrow in range(1, 1 + M):
    #     for ccol in range(6):
    #         print(sharks[rrow][ccol], end=' ')
    #     print()
    # print()
print(ans)
