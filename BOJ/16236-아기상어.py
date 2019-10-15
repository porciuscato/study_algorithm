import sys

sys.stdin = open('input.txt', 'r')

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 이 함수는 현재 위치에서 먹을 수 있는 물고기를 한 번만 찾을 수 있는 것에 집중한다.
def bfs(row, col):
    global W, size, eat, ans
    vis = [[0] * N for _ in range(N)]
    # 물고기를 찾을 때까지 que에 넣는다. 
    que = [(row, col, 0)]
    vis[row][col] = 1
    front = -1
    rear = 0
    # 여기에는 찾은 물고기를 넣자
    find = []
    while front != rear:
        front += 1
        trow, tcol, distance = que[front]
        for d in delta:
            drow = trow + d[0]
            dcol = tcol + d[1]
            if 0 <= drow < N and 0 <= dcol < N and not vis[drow][dcol] and W[drow][dcol] <= size:
                if W[drow][dcol] < size:
                    # 물고기를 찾으면 여기에 넣자
                    match = distance + 1
                    vis[drow][dcol] = 1
                    find.append((drow, dcol, match))
                vis[drow][dcol] = 1
                que.append((drow, dcol, distance + 1))
    # find가 비어있으면 모든 것 종료
    # find가 안 비어있으면 먹을 수 있는 물고기의 위치를 shark에 저장하고, 그 값은 0으로 바꾸고 eat을 +=1 증가시킨다.
    # 이때 먹은 수가 size와 같게 되면 크기를 늘린다.
                    

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
size = 2
eat = 0
ans = 0
r = c = 0
shark = (0, 0)
while r < N:
    if W[r][c] == 9:
        shark = (r, c)
        break
    c += 1
    if c == N:
        c = 0
        r += 1
bfs(shark[0], shark[1])
# 제자리에서 BFS를 돌며 먹을 수 있는 물고기를 찾는다.
# vis는 물고기를 먹을 때마다 초기화된다.
# vis로 가까운 곳에 있는 물고기를 찾는다. -> 이때 큰 게 나오면 지나가지 못하고, 같은 게 나오면 지나가기만 하고
# 작은 게 나오면, 그 거리에 있는 모든 지점들을 찾은 뒤 어디로 갈지 정하자.

# 그런데 이때 모든 장소를 다 돌았는데도, 먹을 수 있는 물고기가 나온다면 탐색을 종료한다. (que가 빈 순간)
# 먼저 출발은 현재 위치부터다. 현재 위치에서 출발하면서 먹을 수 있는 물고기를 탐색한다.

print(ans)
