import sys

sys.stdin = open('14891.txt')

delta = (-1, 1)
d_delta = (6, 2, 6)


def direc_setting(number, direc):
    global ROTATE
    for change in range(2):
        vari = number + delta[change]
        if 0 <= vari <= 3 and ROTATE[vari] == -2:
            if ROTATE[number] == 0:
                ROTATE[vari] = 0
            elif WHEELS[number][d_delta[change]] == WHEELS[vari][d_delta[change + 1]]:
                ROTATE[vari] = 0
            else:
                ROTATE[vari] = direc * -1
            direc_setting(vari, ROTATE[vari])


WHEELS = [list(map(int, list(input()))) for _ in range(4)]
for ___ in range(int(input())):
    number, direc = map(int, input().split())
    number -= 1
    ROTATE = [-2] * 4   # 회전하게 될 모든 상태를 저장
    ROTATE[number] = direc
    direc_setting(number, direc) # 회전 방향 세팅
    for num in range(4):
        if ROTATE[num] == 1:
            WHEELS[num].insert(0, WHEELS[num].pop(-1))
        elif ROTATE[num] == -1:
            WHEELS[num].append(WHEELS[num].pop(0))

answer = 0
for i in range(4):
    answer += WHEELS[i][0] * (2 ** i)
print(answer)