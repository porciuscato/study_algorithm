import sys

sys.stdin = open('17144.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
b_delta = ((1, 0), (0, 1), (-1, 0), (0, -1))


def clean():
    global G
    # 윗 공기청정기부터 upper, 0
    # up_wind가 처리할 위치
    # 항상 좌표가 맞는지 확인
    # direc
    # 돌아온 위치가 처음과 같으면 종료
    # 공기청정기 위에 있는지 확인
    # upper wind row
    u_w_r = upper
    u_w_c = 0
    direc = 0
    while direc < 4:
        next_r = u_w_r + delta[direc][0]
        next_c = u_w_c + delta[direc][1]
        if 0 <= next_r < R and 0 <= next_c < C:
            G[u_w_r][u_w_c] = G[next_r][next_c]
            G[next_r][next_c] = 0
            u_w_r = next_r
            u_w_c = next_c
        else:
            direc += 1


    # 아래 청정기 belower, 0
    # down_wind
    b_w_r = belower
    b_w_c = 0
    direc = 0
    while direc < 4:
        next_r = b_w_r + b_delta[direc][0]
        next_c = b_w_c + b_delta[direc][1]
        if 0 <= next_r < R and 0 <= next_c < C:
            G[b_w_r][b_w_c] = G[next_r][next_c]
            G[next_r][next_c] = 0
            b_w_r = next_r
            b_w_c = next_c
        else:
            direc += 1

    # 다 끝나고 -1로 초기화
    G[upper][0] = -1
    G[belower][0] = -1


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
                # 사방 검색. -1 이거나 범위 끝이면 안 간다.
                for tr, tc in delta:
                    dr = rr + tr
                    dc = cc + tc
                    if 0 <= dr < R and 0 <= dc < C and CB[dr][dc] != -1:
                        val = int(CB[rr][cc] / 5)
                        G[dr][dc] += val
                        G[rr][cc] -= val
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
