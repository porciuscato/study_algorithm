def make_set(x):
    parent[x] = x
    rank[x] = 0


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def link(x, y):
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    if rank[x] == rank[y]:
        rank[x] += 1


def union(x, y):
    link(find_set(x), find_set(y))


SIZE = 20
arr = [i for i in range(SIZE)]
parent = [0] * SIZE
rank = [0] * SIZE

for ele in arr:
    make_set(ele)

union(0, 1)
union(2, 3)
union(4, 5)
union(1, 3)

for ele in arr:
    print(find_set(ele), end=' ')
print()

for ele in arr:
    print(rank[ele], end=' ')
