import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def spring():
    global land, trees, ans, dead_tree, tree_list
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                trees[r][c] = sorted(trees[r][c])
                for i in range(len(trees[r][c])):
                    if land[r][c] >= trees[r][c][i]:
                        # tree_list에서 찾아낸다
                        for k in range(len(tree_list)):
                            if tree_list[k][0] == r and tree_list[k][1] == c and tree_list[k][2] == trees[r][c][i]:
                                land[r][c] -= trees[r][c][i]
                                trees[r][c][i] += 1
                                tree_list[k][2] += 1
                                break
                    else:
                        for k in range(len(tree_list)):
                            if tree_list[k][0] == r and tree_list[k][1] == c and tree_list[k][2] == trees[r][c][i]:
                                ans -= 1
                                dead_tree.append(tree_list.pop(k))
                                break


def summer():
    global dead_tree, land
    while dead_tree:
        x, y, z = dead_tree.pop(0)
        land[x][y] += z // 2


def fall():
    global trees, tree_list, ans
    # tree_list 에는 트리들의 좌표와 나이가 담겨있다. [x, y, z]
    for x, y, z in tree_list:
        if z % 5 == 0:
            for d in delta:
                dx = x + d[0]
                dy = y + d[1]
                if 0 <= dx < N and 0 <= dy < N:
                    tree_list.append([dx, dy, 1])
                    trees[dx][dy].append(1)
                    ans += 1


def winter():
    global land
    for r in range(N):
        for c in range(N):
            land[r][c] += nourish[r][c]


# N : 땅 크기
# M : 묘목 수
# K : K 년 후
N, M, K = map(int, input().split())
# 양분이 저장될 영토
land = [[5] * N for _ in range(N)]
# 겨울마다 추가될 양분의 양
nourish = [list(map(int, input().split())) for _ in range(N)]
# 해당 위치별 나무의 갯수가 나이값으로 저장되어 있다.
trees = [[[] for _ in range(N)] for __ in range(N)]
tree_list = []
dead_tree = []
for i in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)
    tree_list.append([x - 1, y - 1, z])
# 처음 있는 나무수는 M 그루. 번식하고 죽을 때마다 나무 수를 최신화한다.
ans = M
for i in range(K):
    spring()
    summer()
    fall()
    winter()
print(ans)
