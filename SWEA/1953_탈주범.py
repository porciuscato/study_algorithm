import sys

sys.stdin = open('1953.txt', 'r')


def finish(direc, vari):
    if direc == 0 and vari in [1, 2, 5, 6]:
        return True
    elif direc == 1 and vari in [1, 3, 6, 7]:
        return True
    elif direc == 2 and vari in [1, 2, 4, 7]:
        return True
    elif direc == 3 and vari in [1, 3, 4, 5]:
        return True
    else:
        return False


def value(direc, origin, vari):
    if origin == 1:
        if direc in [0, 1, 2, 3]:
            return finish(direc, vari)
    elif origin == 2:
        if direc in [0, 2]:
            return finish(direc, vari)
    elif origin == 3:
        if direc in [1, 3]:
            return finish(direc, vari)
    elif origin == 4:
        if direc in [0, 1]:
            return finish(direc, vari)
    elif origin == 5:
        if direc in [1, 2]:
            return finish(direc, vari)
    elif origin == 6:
        if direc in [2, 3]:
            return finish(direc, vari)
    elif origin == 7:
        if direc in [3, 0]:
            return finish(direc, vari)
    else:
        return False


def check(prev_r, prev_c, now_r, now_c):
    # 터널 유형
    prev_tunnel = TABLE[prev_r][prev_c]
    now_tunnel = TABLE[now_r][now_c]
    # 위쪽
    if now_r - prev_r == -1:
        return value(0, prev_tunnel, now_tunnel)
    # 오른쪽
    elif now_c - prev_c == 1:
        return value(1, prev_tunnel, now_tunnel)
    # 아래쪽
    elif now_r - prev_r == 1:
        return value(2, prev_tunnel, now_tunnel)
    # 왼쪽
    elif now_c - prev_c == -1:
        return value(3, prev_tunnel, now_tunnel)


def tunnel(num):
    if num == 1:
        return (-1, 0), (0, 1), (1, 0), (0, -1)
    elif num == 2:
        return (-1, 0), (1, 0)
    elif num == 3:
        return (0, 1), (0, -1)
    elif num == 4:
        return (-1, 0), (0, 1)
    elif num == 5:
        return (0, 1), (1, 0)
    elif num == 6:
        return (1, 0), (0, -1)
    elif num == 7:
        return (0, -1), (-1, 0)


def bfs(limit):
    visit = [[0] * M for _ in range(N)]
    # 방문 여부를 count로 체크. 결국 count가 총 방문할 수 있는 터널 수를 의미
    count = 1
    visit[R][C] = count
    # 좌표, 시간
    que = [(R, C, 1)]
    front = -1
    rear = 0
    while front != rear and que[front + 1][2] < limit:
        front += 1
        t_r, t_c, t_h = que[front]  # row, col, hour
        for d in tunnel(TABLE[t_r][t_c]): # 터널 유형에 따라 탐색하면서 갈 수 있는지 확인
            dr = t_r + d[0]
            dc = t_c + d[1]
            if 0 <= dr < N and 0 <= dc < M and not visit[dr][dc]:  # 범위 내, 방문 여부를 체크
                # 터널의 유형에 따라 갈 수 있는 게 달라짐
                if check(t_r, t_c, dr, dc):
                    rear += 1
                    que.append([dr, dc, t_h + 1])
                    count += 1
                    visit[dr][dc] = count
    return count


for T in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    TABLE = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(T, bfs(L)))
