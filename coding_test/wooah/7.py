delta = (
    (0, 1),   # 오른쪽, True 시작
    (1, -1),  # 왼쪽 아래
    (1, 0),   # 아래쪽, False 시작
    (-1, 1),  # 오른쪽 위
)


def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for __ in range(n)]
    pos = [0, 0]
    time = 0
    if horizontal:
        direc = 0
    else:
        direc = 2
    for i in range(1, n * n):
        if direc % 2 == 0:
            nr, nc = pos[0] + delta[direc][0], pos[1] + delta[direc][1]
            time += 1
            answer[nr][nc] = time
            direc += 1
        else:
            nr, nc = pos[0] + delta[direc][0], pos[1] + delta[direc][1]
            if 0 <= nr < n and 0 <= nc < n:
                time += 2
                answer[nr][nc] = time
            else:
                direc = (direc + 1) % 4
                nr, nc = pos[0] + delta[direc][0], pos[1] + delta[direc][1]
                if 0 <= nr < n and 0 <= nc < n:
                    time += 1
                    answer[nr][nc] = time
                    direc = (direc + 1) % 4
                else:
                    direc = (direc + 2) % 4
                    nr, nc = pos[0] + delta[direc][0], pos[1] + delta[direc][1]
                    time += 1
                    answer[nr][nc] = time
                    direc = (direc + 3) % 4
        pos = [nr, nc]
    return answer


cases = [
    (4, True),
    (5, False),
    (100, True)
]

for case in cases:
    print(solution(*case))
