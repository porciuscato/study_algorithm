import sys

sys.stdin = open('17142.txt', 'r')


def solve(arr):
    global ans, can_make
    table = [[c for c in TABLE[r]] for r in range(N)]
    viruses = []
    for rr, cc in arr:
        table[rr][cc] = 3
        viruses.append([rr, cc, 0, 0])
    var = 3
    front = -1
    rear = M - 1
    while front != rear:
        front += 1
        t_r, t_c, t_t, void = viruses[front]
        for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            trow = t_r + d[0]
            tcol = t_c + d[1]
            if 0 <= trow < N and 0 <= tcol < N and (not table[trow][tcol] or table[trow][tcol]):
                if not table[trow][tcol]:
                    viruses.append([trow, tcol, t_t + 1, 0])
                elif table[trow][tcol] == 2:
                    viruses.append([trow, tcol, t_t + 1, 1])
                table[trow][tcol] = var + 1
                rear += 1
        var += 1
    # for row in range(N):
    #     print(table[row])
    # print()
    for rr in range(N):
        for cc in range(N):
            if table[rr][cc] == 0:
                return
    can_make = True
    time = viruses[rear][2]
    if time < ans:
        ans = time


def combi(arr, depth, last):
    if depth == M:
        solve(arr)
    else:
        for i in range(last, vir_unit):
            ar = arr[:]
            ar.append(VIRUSES[i])
            combi(ar, depth + 1, i + 1)


N, M = map(int, input().split())
VIRUSES = []
ans = 1e5
TABLE = [list(map(int, input().split())) for _ in range(N)]
for row in range(N):
    for col in range(N):
        if TABLE[row][col] == 2:
            VIRUSES.append([row, col])
vir_unit = len(VIRUSES)
can_make = False
combi([], 0, 0)
print(ans if can_make else -1)