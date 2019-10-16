import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def spring():
    global land, trees, ans, dead_tree, tree_list
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                trees[r][c] = sorted(trees[r][c])
                i = 0
                while i < len(trees[r][c]):
                    k = 0
                    while k < len(tree_list):
                        if tree_list[k][0] == r and tree_list[k][1] == c and tree_list[k][2] == trees[r][c][i]:
                            if land[r][c] >= trees[r][c][i]:
                                land[r][c] -= trees[r][c][i]
                                trees[r][c][i] += 1
                                tree_list[k][2] += 1
                            else:
                                trees[r][c].pop(i)
                                dead_tree.append(tree_list.pop(k))
                                ans -= 1
                            break
                        k += 1
                    i += 1


def summer():
    global dead_tree, land
    while dead_tree:
        x, y, z = dead_tree.pop(0)
        land[x][y] += z // 2


def fall():
    global trees, tree_list, ans
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


N, M, K = map(int, input().split())
land = [[5] * N for _ in range(N)]
nourish = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for __ in range(N)]
tree_list = []
dead_tree = []
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)
    tree_list.append([x - 1, y - 1, z])
ans = M
for _ in range(K):
    spring()
    summer()
    fall()
    winter()
print(ans)
