import sys

# sys.stdin = open('17142.txt', 'r')


def solve(arr):
    global ans, can_make
    table = [[col for col in TABLE[r]] for r in range(N)]
    viruses = []
    tot = TOT
    for rr, cc in arr:
        table[rr][cc] = 3
        viruses.append([rr, cc, 0])

    # print(table)
    front = -1
    rear = M - 1
    while tot > 0 and front != rear:
        front += 1
        t_r, t_c, t_t = viruses[front]
        for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            trow = t_r + d[0]
            tcol = t_c + d[1]
            if 0 <= trow < N and 0 <= tcol < N and (not table[trow][tcol] or table[trow][tcol] == 2):
                if not table[trow][tcol]:
                    viruses.append([trow, tcol, t_t + 1])
                    tot -= 1
                elif table[trow][tcol] == 2:
                    viruses.append([trow, tcol, t_t + 1])
                table[trow][tcol] = t_t + 4
                rear += 1
    # for row in range(N):
    #     print(table[row])
    # print()
    if tot == 0:
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
TOT = 0
for row in range(N):
    for col in range(N):
        if TABLE[row][col] == 2:
            VIRUSES.append([row, col])
        elif TABLE[row][col] == 0:
            TOT += 1
vir_unit = len(VIRUSES)
can_make = False
combi([], 0, 0)
print(ans if can_make else -1)