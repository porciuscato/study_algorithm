# 입력 받기
# 1 위치로 최대 회전 수를 계산
# 궁수 가능한 위치의 모든 조합을 계산
# 각 위치별 타격 범위를 구한 뒤, 타격 가능한 좌표를 (칼럼 오름차순, 로우 내림차순) 으로 정렬
# 그리고 각 조합별로 타격 실시
# 타격 가능한 범위의 후보자들을 좌표에 넣어. -> 하나씩 순회하며 0으로 바꾼다. 이미 0이면 패스 -> 이때 0으로 바뀌면 하나씩 증가
# 아무 것도 없을 경우 0으로 끝남

from itertools import combinations


def find_max_rotate(area: list) -> int:
    ans = 0
    end = False
    for i in range(N):
        if not end:
            for j in range(M):
                if area[i][j]:
                    ans = N - i
                    end = True
                    break
        else:
            break
    return ans


def bfs_range_search(idx, dis) -> list:
    que = [(N - 1, idx, 1)]
    front = -1
    rear = 0
    visited = [[False for _ in range(M)] for __ in range(N)]
    visited[N - 1][idx] = True
    while front != rear:
        front += 1
        r, c, d = que[front]
        if d <= dis:
            for dr, dc in DELTA:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    que.append((nr, nc, d + 1))
                    visited[nr][nc] = True
                    rear += 1
        else:
            break
    result = que[:front]
    result.sort(key=lambda x: (x[2], x[1], -x[0]))
    return result


def rotate(area: list) -> None:
    for j in range(M):
        for i in range(N - 1, 0, -1):
            area[i][j] = area[i - 1][j]
    for j in range(M):
        area[0][j] = 0


def set_attack_range(dis: int) -> list:
    result = []
    for j in range(M):
        result.append(bfs_range_search(j, dis))
    return result


def attack(combination: tuple, area: list) -> int:
    total = 0
    attack_targets = []
    for com in combination:
        for r, c, _ in ATTACK_RANGE[com]:
            if area[r][c]:
                attack_targets.append((r, c))
                break
    for r, c in attack_targets:
        if area[r][c]:
            area[r][c] = 0
            total += 1
    return total


def is_enemy_left(area: list) -> bool:
    for i in range(N):
        for j in range(M):
            if area[i][j]:
                return True
    return False


def solve(combination: tuple) -> None:
    global answer
    total = 0
    area = []
    for i in range(N):
        t = []
        for j in range(M):
            t.append(board[i][j])
        area.append(t)

    while True:
        total += attack(combination, area)
        rotate(area)
        if not is_enemy_left(area):
            break

    answer = max(answer, total)


if __name__ == "__main__":
    N, M, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1))
    MAX_ROTATE = find_max_rotate(board)
    ATTACK_RANGE = set_attack_range(D)

    for combi in combinations([i for i in range(M)], 3):
        solve(combi)
    print(answer)
