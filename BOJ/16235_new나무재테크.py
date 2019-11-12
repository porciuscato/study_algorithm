import sys

sys.stdin = open('16235.txt', 'r')

delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def spring():
    global land, tree_info, ans, how_many, dead_trees, thrive_trees
    dead_trees = []
    thrive_trees = []
    for row in range(N):
        for col in range(N):
            if how_many[row][col] == 0:
                continue
            else:
                for idx in range(len(tree_info[row][col])):
                    if land[row][col] >= tree_info[row][col][idx]:
                        land[row][col] -= tree_info[row][col][idx]
                        tree_info[row][col][idx] += 1
                        if tree_info[row][col][idx] % 5 == 0:
                            # thrive_trees.append([row, col])
                            thrive_trees += [[row, col]]
                    else:
                        for i in range(idx, len(tree_info[row][col])):
                            # dead_trees.append([row, col, tree_info[row][col].pop(idx)])
                            dead_trees += [[row, col, tree_info[row][col].pop(idx)]]
                            how_many[row][col] -= 1
                            ans -= 1
                        break


def summer():
    global land, dead_trees
    for tree in dead_trees:
        land[tree[0]][tree[1]] += tree[2] // 2


def fall():
    global thrive_trees, tree_info, how_many, ans
    for tree in thrive_trees:
        tr = tree[0]
        tc = tree[1]
        for d in delta:
            dr = tr + d[0]
            dc = tc + d[1]
            if 0 <= dr < N and 0 <= dc < N:
                tree_info[dr][dc].insert(0, 1)
                how_many[dr][dc] += 1
                ans += 1


def winter():
    global land
    for r in range(N):
        for c in range(N):
            land[r][c] += NOURISH[r][c]


# M 개의 나무, K 년 후
N, M, K = map(int, input().split())
# N * N 크기의 땅. 처음엔 모든 양분이 5씩
land = [[5] * N for _ in range(N)]
# 겨울에 각 칸에 추가되는 양분의 양
NOURISH = [list(map(int, input().split())) for _ in range(N)]
# 나무의 수
how_many = [[0] * N for _ in range(N)]
# 해당하는 좌표에 나무를 넣고 age 저장
tree_info = [[[] for _ in range(N)] for __ in range(N)]
# 죽은 나무는 [row, col, age] 형태로 이 배열에 저장한다.
dead_trees = []
# 번성할 나무는 [row, col] 형태로 이 배열에 저장
thrive_trees = []
for _ in range(M):
    x, y, z = map(int, input().split())
    how_many[x - 1][y - 1] += 1
    tree_info[x - 1][y - 1] += [z]
ans = M
k = 0
while k < K:
    spring()
    summer()
    fall()
    winter()
    k += 1
print(ans)