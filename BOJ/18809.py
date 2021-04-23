import sys
from itertools import combinations
from collections import deque

s_input = sys.stdin.readline
s_print = sys.stdout.write


def simulation(green_seeds, red_seeds) -> int:
    visited = [[False for _ in range(M)] for __ in range(N)]
    seed_check = [['' for _ in range(M)] for __ in range(N)]

    que = deque([])
    for row, col in green_seeds:
        visited[row][col] = True
        que.append((row, col, 'G'))
    for row, col in red_seeds:
        visited[row][col] = True
        que.append((row, col, 'R'))

    flowers = 0
    temp = deque([])
    while que:
        r, c, color = que.popleft()
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and garden[nr][nc] != 0:
                    temp.append((nr, nc, color))

        if len(que) == 0:
            for seed in temp:
                r, c, color = seed
                visited[r][c] = True
                if color == "G":
                    seed_check[r][c] += color
                else:
                    seed_check[r][c] += color

            for seed in temp:
                r, c, _ = seed
                if 'GR' in seed_check[r][c] or 'RG' in seed_check[r][c]:
                    seed_check[r][c] = 'F'
                    flowers += 1

            while temp:
                r, c, color = temp.popleft()
                if seed_check[r][c] == '':
                    continue
                if seed_check[r][c] != 'F':
                    que.append((r, c, color))
                seed_check[r][c] = ''

    return flowers


if __name__ == "__main__":
    N, M, G, R = map(int, s_input().split())
    garden = []
    seed_lands = []
    for i in range(N):
        arr = list(map(int, s_input().split()))
        garden.append(arr)
        for j in range(M):
            if arr[j] == 2:
                seed_lands.append((i, j))

    answer = 0
    for combs in combinations(seed_lands, G + R):
        for green in combinations(combs, G):
            answer = max(answer, simulation(green, (pair for pair in combs if pair not in green)))

    s_print(f'{answer}\n')
