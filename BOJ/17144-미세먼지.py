import sys

sys.stdin = open('17144.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
b_delta = ((1, 0), (0, 1), (-1, 0), (0, -1))


def up_go(dir):
    global G, u_w_c, u_w_r
    next_r = u_w_r + delta[dir][0]
    next_c = u_w_c + delta[dir][1]
    G[u_w_r][u_w_c] = G[next_r][next_c]
    G[next_r][next_c] = 0
    u_w_r = next_r
    u_w_c = next_c


def below_go(dir):
    global G, b_w_c, b_w_r
    next_r = b_w_r + b_delta[dir][0]
    next_c = b_w_c + b_delta[dir][1]
    G[b_w_r][b_w_c] = G[next_r][next_c]
    G[next_r][next_c] = 0
    b_w_r = next_r
    b_w_c = next_c


def clean():
    global G, u_w_c, u_w_r, b_w_c, b_w_r
    # 윗 공기청정기부터 upper, 0
    # upper_wind row
    direc = 0
    while u_w_r >= 1:
        up_go(direc)
    direc += 1
    while u_w_c <= C - 2:
        up_go(direc)
    direc += 1
    while u_w_r <= upper - 1:
        up_go(direc)
    direc += 1
    while u_w_c >= 2:
        up_go(direc)

    # 아래 청정기 belower, 0
    # down_wind
    direc = 0
    while b_w_r <= R - 2:
        below_go(direc)
    direc += 1
    while b_w_c <= C - 2:
        below_go(direc)
    direc += 1
    while b_w_r >= belower + 1:
        below_go(direc)
    direc += 1
    while b_w_c >= 2:
        below_go(direc)

    # 다 끝나고 초기화
    G[upper][0] = -1
    G[belower][0] = -1
    u_w_r = upper
    u_w_c = 0
    b_w_r = belower
    b_w_c = 0


def spread():
    global G, CB
    # 원본데이터의 미세먼지 정보를 CB에 업데이트 시킨다.
    for rr in range(R):
        for cc in range(C):
            CB[rr][cc] = G[rr][cc]
    # 돌며 공기 확산
    for rr in range(R):
        for cc in range(C):
            # 미세먼지의 위치를 찾는다.
            if CB[rr][cc] > 0:
                # 사방 검색. -1 이거나 범위를 벗어나면 확산하지 않는다.
                for tr, tc in delta:
                    dr = rr + tr
                    dc = cc + tc
                    if 0 <= dr < R and 0 <= dc < C and CB[dr][dc] != -1:
                        val = int(CB[rr][cc] / 5)
                        G[dr][dc] += val
                        G[rr][cc] -= val
                # 처리가 끝났기에 다시 0으로 만들어줌
                CB[rr][cc] = 0


R, C, T = map(int, input().split())
# 원본 데이터
G = [list(map(int, input().split())) for _ in range(R)]
# Check Box. 미세먼지 확산 전에 원본 데이터를 이곳에 저장한다.
CB = [[0] * C for _ in range(R)]
# 공기청정기의 위치.
upper = belower = 0
for rr in range(R):
    if G[rr][0] == -1:
        upper = rr
        belower = rr + 1
        break
u_w_r = upper
u_w_c = 0
b_w_r = belower
b_w_c = 0
time = 1
while time <= T:
    spread()
    clean()
    time += 1
ans = 0
for rr in range(R):
    for cc in range(C):
        # 비었거나 공기청정기면 넘어간다.
        if G[rr][cc] == 0 or G[rr][cc] == -1:
            continue
        ans += G[rr][cc]
print(ans)
