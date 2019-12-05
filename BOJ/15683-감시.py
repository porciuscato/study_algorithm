import sys

sys.stdin = open('15683.txt')

delta = ((0, 1), (-1, 0), (0, -1), (1, 0))
c_directions = (
    [10, 11, 12, 13],
    [20, 21],
    [30, 31, 32, 33],
    [40, 41, 42, 43],
    [50],
)
c_delta = (
    [[delta[0]], [delta[1]], [delta[2]], [delta[3]]],
    [[delta[0], delta[2]], [delta[1], delta[3]]],
    [[delta[0], delta[1]], [delta[1], delta[2]], [delta[2], delta[3]], [delta[3], delta[0]]],
    [[delta[0], delta[1], delta[2]], [delta[0], delta[1], delta[3]], [delta[0], delta[2], delta[3]], [delta[1], delta[2], delta[3]]],
    [[delta[0], delta[1], delta[2], delta[3]]],
)


def solve():
    global ans, G
    for Hubo in HUBO:
        idx = 0
        for cctv in Hubo:
            value = cctv // 10 - 1
            rem = cctv % 10
            cctv_delta = c_delta[value][rem]
            o_row, o_col = CCTV[idx][0]
            for vari in cctv_delta:
                d_row = o_row + vari[0]
                d_col = o_col + vari[1]
                while 0 <= d_row < N and 0 <= d_col < M and G[d_row][d_col] != 6:
                    if G[d_row][d_col] == 0:
                        G[d_row][d_col] = -1
                    d_row += vari[0]
                    d_col += vari[1]
            idx += 1
        count = 0
        for row in range(N):
            for col in range(M):
                if G[row][col] == 0:
                    count += 1
                elif G[row][col] == -1:
                    G[row][col] = 0
        ans = min(ans, count)


def make(arr, order):
    global HUBO
    if order == length:
        HUBO.append(arr)
    else:
        c_type = CCTV[order][1]
        for ele in c_directions[c_type - 1]:
            ar = arr[:]
            ar.append(ele)
            make(ar, order + 1)


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
CCTV = []
for r in range(N):
    for c in range(M):
        if 1 <= G[r][c] <= 5:
            CCTV.append([(r, c), G[r][c]])
length = len(CCTV)
HUBO = []
make([], 0)
ans = 1e5
solve()
print(ans)