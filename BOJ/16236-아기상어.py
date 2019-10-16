import sys

sys.stdin = open('input.txt', 'r')

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 이 함수는 현재 위치에서 먹을 수 있는 물고기를 한 번만 찾을 수 있는 것에 집중한다.
def bfs(row, col):
    global W, size, eat, ans, shark, check
    vis = [[0] * N for _ in range(N)]
    # 물고기를 찾을 때까지 que에 넣는다. 
    que = [(row, col, 0)]
    vis[row][col] = 1
    front = -1z
    rear = 0
    # 여기에는 찾은 물고기를 넣자
    find = [[0] * N for _ in range(N)]
    # 물고기를 찾았을 때 물고기까지의 거리
    fish_at = 1e7
    # 찾은 물고기 개수
    fish_num = 0
    while front != rear:
        front += 1
        trow, tcol, distance = que[front]
        if distance >= fish_at:
            break
        for d in delta:
            drow = trow + d[0]
            dcol = tcol + d[1]
            if 0 <= drow < N and 0 <= dcol < N and not vis[drow][dcol] and W[drow][dcol] <= size:
                # 물고기를 찾으면 여기에 넣자
                if 0 < W[drow][dcol] < size:
                    fish_at = distance + 1
                    fish_num += 1
                    vis[drow][dcol] = 1
                    find[drow][dcol] = 1
                # 물고기를 못 찾았다면
                else:
                    vis[drow][dcol] = 1
                    que.append((drow, dcol, distance + 1))
                    rear += 1
    if fish_num == 0:
        check = False
    else:
        for rr in range(N):
            for cc in range(N):
                if find[rr][cc] == 1:
                    W[rr][cc] = 0
                    eat += 1
                    if eat == size:
                        size += 1
                        eat = 0
                    shark = (rr, cc)
                    ans += fish_at
                    return
                    

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
size = 2
eat = 0
ans = 0
r = c = 0
shark = (0, 0)
while r < N:
    if W[r][c] == 9:
        W[r][c] = 0
        shark = (r, c)
        break
    c += 1
    if c == N:
        c = 0
        r += 1
check = True
while check:
    bfs(shark[0], shark[1])

print(ans)
