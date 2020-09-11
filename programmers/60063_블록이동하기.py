from collections import deque

par_delta = (
    ((0, -1), (0, -1), "par", ((0, -1), (0, -1))),
    ((0, 1), (0, 1), "par", ((0, 1), (0, 1))),
    ((-1, 0), (-1, 0), "par", ((-1, 0), (-1, 0))),
    ((1, 0), (1, 0), "par", ((1, 0), (1, 0))),
    ((-1, 0), (0, -1), "ver", ((-1, 0), (-1, 0))),
    ((-1, 1), (0, 0), "ver", ((-1, 0), (-1, 0))),
    ((0, 0), (1, -1), "ver", ((1, 0), (1, 0))),
    ((0, 1), (1, 0), "ver", ((1, 0), (1, 0)))
)

ver_delta = (
    ((0, -1), (0, -1), "ver", ((0, -1), (0, -1))),
    ((0, 1), (0, 1), "ver", ((0, 1), (0, 1))),
    ((-1, 0), (-1, 0), "ver", ((-1, 0), (-1, 0))),
    ((1, 0), (1, 0), "ver", ((1, 0), (1, 0))),
    ((0, -1), (-1, 0), "par", ((0, -1), (0, -1))),
    ((1, -1), (0, 0), "par", ((0, -1), (0, -1))),
    ((0, 0), (-1, 1), "par", ((0, 1), (0, 1))),
    ((1, 0), (0, 1), "par", ((0, 1), (0, 1)))
)


class Robot:
    def __init__(self, cor1=(0, 0), cor2=(0, 0), pos="par"):
        self.cor1 = cor1
        self.cor2 = cor2
        self.pos = pos


def solution(board):
    n = len(board)
    visited = [[[0, 0] for _ in range(n)] for __ in range(n)]  # (par, ver)
    visited[0][0][0] = 1
    deq = deque([(Robot((0, 0), (0, 1), "par"), 0)])
    while deq:
        robot, time = deq.popleft()
        if robot.cor2 == (n - 1, n - 1):
            return time

        if robot.pos == "par":
            delta = par_delta
        else:
            delta = ver_delta

        for (d1r, d1c), (d2r, d2c), pos, ((c1r, c1c), (c2r, c2c)) in delta:
            (r1r, r1c), (r2r, r2c) = robot.cor1, robot.cor2
            if 0 <= r1r + d1r < n and 0 <= r1c + d1c < n and 0 <= r2r + d2r < n and 0 <= r2c + d2c < n:
                if not board[r1r + c1r][r1c + c1c] and not board[r2r + c2r][r2c + c2c]:
                    if pos == "par":
                        if not visited[r1r + d1r][r1c + d1c][0]:
                            deq.append((Robot((r1r + d1r, r1c + d1c), (r2r + d2r, r2c + d2c), "par"), time + 1))
                            visited[r1r + d1r][r1c + d1c][0] = 1
                    else:
                        if not visited[r1r + d1r][r1c + d1c][1]:
                            deq.append((Robot((r1r + d1r, r1c + d1c), (r2r + d2r, r2c + d2c), "ver"), time + 1))
                            visited[r1r + d1r][r1c + d1c][1] = 1


cases = [
    [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
]

for case in cases:
    print(solution(case))
