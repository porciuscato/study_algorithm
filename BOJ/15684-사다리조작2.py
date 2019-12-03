import sys

sys.stdin = open('15684.txt', 'r')


def check():
    global flag, LADDER, ans
    if hubo_LIST:
        for hubo in hubo_LIST:
            count = 1
            for h_row, h_col in hubo:
                LADDER[h_row][h_col] = count
                LADDER[h_row][h_col + 1] = count
                count += 1
            for n in range(N):
                n_row = 0
                n_col = n
                while n_row < H:
                    if not LADDER[n_row][n_col]:
                        n_row += 1
                    else:
                        val = LADDER[n_row][n_col]
                        for d in (-1, 1):
                            d_col = n_col + d
                            if 0 <= d_col < N and val == LADDER[n_row][d_col]:
                                n_row += 1
                                n_col = d_col
                                break
                if n_col == n:
                    continue
                else:
                    break
            else:
                flag = True
                ans = len(hubo)
                return
            for h_row, h_col in hubo:
                LADDER[h_row][h_col] = 0
                LADDER[h_row][h_col + 1] = 0


def combi(arr, depth, last):
    global hubo_LIST
    if depth == i:
        hubo_LIST.append(arr)
    else:
        for t in range(last, length):
            ar = arr[:]
            if ar and ar[-1][0] == HUBO[t][0] and ar[-1][1] + 1 == HUBO[t][1]:
                continue
            ar.append(HUBO[t])
            combi(ar, depth + 1, t + 1)


# N: column, H: row, M은 기본 사다리
N, M, H = map(int, input().split())
LADDER = [[0] * N for _ in range(H)]
lad_count = 4
for _ in range(M):
    l_r, l_c = map(int, input().split())
    LADDER[l_r - 1][l_c - 1] = lad_count
    LADDER[l_r - 1][l_c] = lad_count
    lad_count += 1
HUBO = []
for row in range(H):
    for col in range(N - 1):
        if not LADDER[row][col] and not LADDER[row][col + 1]:
            HUBO.append((row, col))
flag = False
length = len(HUBO)
ans = -1
hubo_LIST = []
for i in range(4):
    if i <= length:
        combi([], 0, 0)
    else:
        break
# for r in range(H):
#     print(LADDER[r])
# print(hubo_LIST)
check()
print(ans if flag else -1)