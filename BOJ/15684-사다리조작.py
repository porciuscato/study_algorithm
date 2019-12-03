import sys

sys.stdin = open('15684.txt', 'r')


# 입력을 받는다
# 이제 실험을 해보는 거지
# 여기서 만들 수 있는 모든 조합들을 생각해보자
# 0인 경우가 있지? 그러면 이건 안 됨! 하고 -1 출력하면 됨
# 하나밖에 놓을 수 없다? 그러면 하나만 하면 됨
# 두개밖에? 그러면 두개. 세개밖에 그러면 세개
# 즉 4개 이상인 경우에만 여러 가지 실험이 가능하다는 얘기
# 그러면...

# 1) 입력 받기
# 2) 가능한지 불가능한지 판단 -> 나올 수 있는 경우의 수 뽑아내기
# 3) 한 번에 갈 수 있는지도 확인

# 기본 루트는 설치 -> 가능? 반복구조


# 돌면서 자기 자리로 가는지 확인
def check(hubo_list):
    global flag
    ladder = [[LADDER[r][c] for c in range(N)] for r in range(H)]
    if hubo_list:
        count = 1
        for h_row, h_col in hubo_list:
            ladder[h_row][h_col] = count
            ladder[h_row][h_col + 1] = count
            count += 1
    for n in range(N):
        n_row = 0
        n_col = n
        while n_row < H:
            if not ladder[n_row][n_col]:
                n_row += 1
            else:
                val = ladder[n_row][n_col]
                for d in (-1, 1):
                    d_col = n_col + d
                    if 0 <= d_col < N and val == ladder[n_row][d_col]:
                        n_row += 1
                        n_col = d_col
                        break
        if n_col == n:
            continue
        else:
            return False
    flag = True
    return True


def combi(arr, depth, last):
    if flag:
        return
    if depth == i:
        check(arr)
    else:
        for t in range(last, length):
            ar = arr[:]
            if ar and ar[-1][1] + 1 == HUBO[t][1]:
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

# 가능한 곳 좌표를 구하자.
HUBO = []
for row in range(H):
    for col in range(N - 1):
        if not LADDER[row][col] and not LADDER[row][col + 1]:
            HUBO.append((row, col))
# 후보까지 다 구했으니까, 이제 해볼까?
# 먼저... 그냥 돌려봐. -> 됨 -> 끝내
flag = False
length = len(HUBO)
ans = -1
for i in range(4):
    if i <= length:
        # i 만큼 hubo 중 조합을 만들어
        combi([], 0, 0)
        if flag:
            ans = i
            break
    else:
        break
print(ans if flag else -1)