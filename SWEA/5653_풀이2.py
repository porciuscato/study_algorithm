import sys

sys.stdin = open("5653.txt", "r")


class Cell:
    def __init__(self, row, col, status, life, time):
        self.row = row
        self.col = col
        self.status = status
        self.life = life
        self.time = time

    def __repr__(self):
        return "(({}, {}) => {}, {})".format(self.row, self.col, self.status, self.life)


def solve():
    global cells, visited
    # cells 거꾸로 돈다.
    for idx in range(10, 0, -1):
        if cells[idx]:
            cell_list = cells[idx]
            new_cells = []
            removed_cells = []
            for cell_obj in cell_list:
                # 번식
                if cell_obj.status == 1:
                    r, c = cell_obj.row, cell_obj.col
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        n_r = r + dr
                        n_c = c + dc
                        if 0 <= n_r < K + N and 0 <= n_c < K + M and not visited[n_r][n_c]:
                            new_one = Cell(n_r, n_c, 2, cell_obj.life, cell_obj.life)
                            visited[n_r][n_c] = True
                            new_cells.append(new_one)
                # 시간 감소
                cell_obj.time -= 1
                if cell_obj.time == 0:
                    cell_obj.status -= 1
                    cell_obj.time = cell_obj.life
                    if cell_obj.status == 0:
                        removed_cells.append(cell_obj)
            if new_cells:
                cell_list += new_cells
            if removed_cells:
                for r_cell in removed_cells:
                    cell_list.remove(r_cell)


def data_init():
    global visited, cells
    for n in range(half_K, half_K + N):
        temp = list(map(int, input().split()))
        idx = 0
        for m in range(half_K, half_K + M):
            if temp[idx]:
                cell = Cell(n, m, 2, temp[idx], temp[idx])
                cells[cell.life].append(cell)
                visited[n][m] = True
            idx += 1


def live_count():
    global answer
    for cell_list in cells:
        answer += len(cell_list)


for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    half_K = K // 2
    visited = [[False for _ in range(K + M)] for __ in range(K + N)]
    cells = [[] for _ in range(11)]
    answer = 0
    data_init()
    for k in range(K):
        solve()
    live_count()
    print("#{} {}".format(T, answer))
