import sys

sys.stdin = open('2105.txt', 'r')

# 시계 방향
delta = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def solve(cor, delt):
    global ans, can_make
    if delt == 4:
        print(counting)
        ans = max(ans, len(counting))
        can_make = True
    elif delt == 3:
        drow = cor[0] + delta[delt][0]
        dcol = cor[1] + delta[delt][1]
        while 0 <= drow < N and 0 <= dcol < N and drow != ROW:
            val = TABLE[drow][dcol]
            if val not in counting:
                counting.append(val)
            else:
                return False
            drow += delta[delt][0]
            dcol += delta[delt][1]
        if drow == ROW and dcol == COL:
            solve((0, 0), 4)
        else:
            return False
    else:
        # print(cor[0], cor[1])
        drow = cor[0] + delta[delt][0]
        dcol = cor[1] + delta[delt][1]
        while 0 <= drow < N and 0 <= dcol < N:
            val = TABLE[drow][dcol]
            if val not in counting:
                counting.append(val)
                solve((drow, dcol), delt + 1)
                counting.pop()
            else:
                return False
            drow += delta[delt][0]
            dcol += delta[delt][1]


for T in range(1, int(input()) + 1):
    global counting
    N = int(input())
    TABLE = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    can_make = False
    for ROW in range(N):
        for COL in range(N):
            counting = list()
            counting.append(TABLE[ROW][COL])
            solve((ROW, COL), 0)
    print('#{} {}'.format(T, ans if can_make else -1))
