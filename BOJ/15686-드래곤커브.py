import sys

sys.stdin = open('15685.txt', 'r')

delta = ((0, 1), (-1, 0), (0, -1), (1, 0))


def dragon(col, row, direc, curve):
    global DRAGON
    ORIGIN = [(row, col), (row + delta[direc][0], col + delta[direc][1])]
    if curve >= 1:
        # 횟수만큼 돌면서 ORIGIN에 업데이트
        # 일단 마지막 껄 골라
        temp = 1
        while temp <= curve:
            abs_row, abs_col = ORIGIN[-1]
            # 마지막 좌표는 회전의 기준점이므로, 이를 제외한 나머지 좌표를 가공하여 to_zero에 담는다.
            # 이때 마지막 좌표를 (0, 0)으로 바꿔주고, 나머지 좌표들도 그 차 만큼 평행이동
            to_zero = [((ccol - abs_col) + abs_row, -(rrow - abs_row) + abs_col) for rrow, ccol in ORIGIN[0:-1]]
            # (c, -r) 변환을 시행, 변환 값을 add_to_origin에 담고 ORIGIN에 뒤집은 채 붙인다.
            # add_to_origin = [(cc + abs_row, -rr + abs_col) for rr, cc in to_zero]
            ORIGIN += to_zero[::-1]
            # 반복
            temp += 1
    for origin in ORIGIN:
        o_row, o_col = origin
        if 0 <= o_row <= 100 and 0 <= o_col <= 100:
            DRAGON[o_row][o_col] = 1


# 유효한 좌표는 오직 0 <= x, y <= 100
# 드래곤 커브인 점들을 표기하기 위한 그래프를 그려 -> 그래곤 커브는 여기다가 표시해
DRAGON = [[0] * 101 for _ in range(101)]
for c in range(int(input())):
    # 각 점마다 드래곤 커브 시행
    col, row, direc, curve = map(int, input().split())
    dragon(col, row, direc, curve)

# 드래곤 커브가 끝나면 하나씩 돌면서 모두 드래곤 커브인지 확인해. 맞아? 그러면 ans에 더해
ans = 0
for row in range(100):
    for col in range(100):
        if DRAGON[row][col] and DRAGON[row][col + 1] and DRAGON[row + 1][col] and DRAGON[row + 1][col + 1]:
            ans += 1
print(ans)