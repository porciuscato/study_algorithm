def bfs(place, players):
    for player in players:
        pr, pc = player
        que = []
        visited = [[False for _ in range(COL)] for __ in range(ROW)]
        visited[pr][pc] = True
        que.append((pr, pc, 0))
        front = -1
        rear = 0
        while front != rear:
            front += 1
            r, c, dis = que[front]
            for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc] and place[nr][nc] != 'X':
                    if place[nr][nc] == 'P' and dis + 1 <= 2:
                        return 0
                    else:
                        que.append((nr, nc, dis + 1))
                        visited[nr][nc] = True
                        rear += 1
    return 1


def solution(places):
    global ROW, COL
    answer = []
    for place in places:
        players = []
        ROW = len(places)
        COL = len(places[0])
        for r in range(ROW):
            for c in range(COL):
                if place[r][c] == 'P':
                    players.append((r, c))
        answer.append(bfs(place, players))

    return answer


cases = [
    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
]

for case in cases:
    print(solution(case))
