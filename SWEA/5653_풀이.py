import sys

sys.stdin = open("5653.txt", "r")


class Cell:
    def __init__(self):
        # 0 죽음 1 활성 2 비활성
        self.status = 0
        self.life = 0
        self.time = 0


def data_init():
    global data, visited
    for n in range(half_K, half_K + N):
        temp = list(map(int, input().split()))
        idx = 0
        for m in range(half_K, half_K + M):
            if temp[idx]:
                cell = Cell()
                cell.status = 2
                cell.life = temp[idx]
                cell.time = cell.life
                data[n][m] = cell
                visited[n][m] = True
            idx += 1


def solve():
    global visited, data
    for n in range(K + N):
        for m in range(K + M):
            if visited[n][m] and data[n][m].status > 0:
                one = data[n][m]
                # 비활성
                if one.status == 2:
                    # 시간 감소
                    one.time -= 1
                    if one.time == 0:
                        one.status -= 1
                        one.time = one.life
                # 활성
                elif one.status == 1:
                    # 번식
                    n_r, n_c = n, m
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        next_r = n_r + dr
                        next_c = n_c + dc
                        if 0 <= next_r < (K + N) and 0 <= next_c < (K + M) and not visited[next_r][next_c]:
                            # 있는 경우
                            if data[next_r][next_c]:
                                # 있는 경우, 원래 있던 것과 비교해, life 가 더 크면 life로 새로 바꾸자.
                                next_one = data[next_r][next_c]
                                if next_one.life < one.life:
                                    new_one = Cell()
                                    new_one.status = 2
                                    new_one.life = one.life
                                    new_one.time = one.life
                                    data[next_r][next_c] = new_one
                            # 없는 경우
                            else:
                                # 이 곳을 cell로 만들자.
                                new_one = Cell()
                                new_one.status = 2
                                new_one.life = one.life
                                new_one.time = one.life
                                data[next_r][next_c] = new_one
                    # 시간 감소
                    one.time -= 1
                    if one.time == 0:
                        one.status -= 1
                        one.time = one.life
    # visit 처리
    for n in range(K + N):
        for m in range(K + M):
            if not visited[n][m] and data[n][m]:
                visited[n][m] = True


def live_count():
    global answer
    for r in range(K + N):
        for c in range(K + M):
            if data[r][c] and 0 < data[r][c].status:
                answer += 1


for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    half_K = K // 2
    visited = [[False for _ in range(K + M)] for __ in range(K + N)]
    data = [[None for _ in range(K + M)] for __ in range(K + N)]
    cells = [[] for _ in range(11)]
    answer = 0
    data_init()
    for k in range(K):
        solve()
    live_count()
    print("#{} {}".format(T, answer))
