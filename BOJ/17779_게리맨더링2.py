import sys

sys.stdin = open('17779.txt', 'r')


def solve(ur, uc, lr, lc, rr, rc, br, bc):
    global ans
    visit = [[0] * N for _ in range(N)]
    people = [0, 0, 0, 0, 0]

    people[4] += TABLE[ur][uc]
    visit[ur][uc] = 5
    people[4] += TABLE[lr][lc]
    visit[lr][lc] = 5
    people[4] += TABLE[rr][rc]
    visit[rr][rc] = 5
    people[4] += TABLE[br][bc]
    visit[br][bc] = 5
    # 위에 선 긋기
    t_ur = ur - 1
    while 0 <= t_ur < N:
        people[0] += TABLE[t_ur][uc]
        visit[t_ur][uc] = 1
        t_ur -= 1
    # 오른쪽에 선 긋기
    t_rc = rc + 1
    while 0 <= t_rc < N:
        people[1] += TABLE[rr][t_rc]
        visit[rr][t_rc] = 2
        t_rc += 1
    # 왼쪽에 선 긋기
    t_lc = lc - 1
    while 0 <= t_lc < N:
        people[2] += TABLE[lr][t_lc]
        visit[lr][t_lc] = 3
        t_lc -= 1
    # 아래에 선 긋기
    t_br = br + 1
    while 0 <= t_br < N:
        people[3] += TABLE[t_br][bc]
        visit[t_br][bc] = 4
        t_br += 1
    # 5 구역 선 긋기
    temp_r = ur
    temp_c = uc
    temp_r += 1
    temp_c -= 1
    while temp_r != lr and temp_c != lc:
        people[4] += TABLE[temp_r][temp_c]
        visit[temp_r][temp_c] = 5
        temp_r += 1
        temp_c -= 1
    temp_r = ur
    temp_c = uc
    temp_r += 1
    temp_c += 1
    while temp_r != rr and temp_c != rc:
        people[4] += TABLE[temp_r][temp_c]
        visit[temp_r][temp_c] = 5
        temp_r += 1
        temp_c += 1
    temp_r = lr
    temp_c = lc
    temp_r += 1
    temp_c += 1
    while temp_r != br and temp_c != bc:
        people[4] += TABLE[temp_r][temp_c]
        visit[temp_r][temp_c] = 5
        temp_r += 1
        temp_c += 1
    temp_r = rr
    temp_c = rc
    temp_r += 1
    temp_c -= 1
    while temp_r != br and temp_c != bc:
        people[4] += TABLE[temp_r][temp_c]
        visit[temp_r][temp_c] = 5
        temp_r += 1
        temp_c -= 1
    # 나머지 넓이 구하기
    # 시작 좌표들
    coordi = ((0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1), (ur + 1, uc), (br - 1, bc))
    var = 1
    for cor in coordi:
        start_row, start_col = cor
        if var == 6:
            if visit[start_row][start_col]:
                continue
            else:
                visit[start_row][start_col] = 5
                people[4] += TABLE[start_row][start_col]
        else:
            visit[start_row][start_col] = var
            people[var - 1] += TABLE[start_row][start_col]
        que = [(start_row, start_col)]
        front = -1
        rear = 0
        while front != rear:
            front += 1
            s_row, s_col = que[front]
            for d in ((-1, 0), (0, 1), (1, 0), (0, - 1)):
                d_row = s_row + d[0]
                d_col = s_col + d[1]
                if 0 <= d_row < N and 0 <= d_col < N and not visit[d_row][d_col]:
                    if var == 6:
                        visit[d_row][d_col] = 5
                        people[4] += TABLE[d_row][d_col]
                    else:
                        visit[d_row][d_col] = var
                        people[var - 1] += TABLE[d_row][d_col]
                    que.append((d_row, d_col))
                    rear += 1
        var += 1
    value = max(people) - min(people)
    if value < ans:
        ans = value


def get_right(ur, uc, lr, lc, rr, rc):
    from_left = []
    from_right = []
    temp_lr = lr + 1
    temp_lc = lc + 1
    while 0 <= temp_lr < N and 0 <= temp_lc < N:
        from_left.append((temp_lr, temp_lc))
        temp_lr += 1
        temp_lc += 1
    temp_rr = rr + 1
    temp_rc = rc - 1
    while 0 <= temp_rr < N and 0 <= temp_rc < N:
        from_right.append((temp_rr, temp_rc))
        temp_rr += 1
        temp_rc -= 1
    result = list(set(from_left) & set(from_right))
    if result:
        br, bc = result[0]
        solve(ur, uc, lr, lc, rr, rc, br, bc)
    else:
        return


def get_left(ur, uc, lr, lc):
    rr = ur + 1
    rc = uc + 1
    while 0 <= rr < N and 0 <= rc < N:
        get_right(ur, uc, lr, lc, rr, rc)
        rr += 1
        rc += 1


def get_up(ur, uc):
    lr = ur + 1
    lc = uc - 1
    while 0 <= lr < N and 0 <= lc < N:
        get_left(ur, uc, lr, lc)
        lr += 1
        lc -= 1


N = int(input())
TABLE = [list(map(int, input().split())) for _ in range(N)]
ans = 1e5
for row in range(N):
    for col in range(N):
        get_up(row, col)
print(ans)
