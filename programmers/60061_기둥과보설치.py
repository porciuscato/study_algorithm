class Node:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0


def set_bridge(board, row, col):
    l_grid = board[row][col]
    r_grid = board[row][col + 1]
    if (l_grid.down or r_grid.down) or (l_grid.left and r_grid.right):
        l_grid.right = 1
        r_grid.left = 1


def del_bridge(board, row, col):
    l_grid = board[row][col]
    r_grid = board[row][col + 1]
    if l_grid.left:
        ll_grid = board[row][col - 1]
        if not (ll_grid.down or l_grid.down):
            return
    if l_grid.up:
        if not (l_grid.left or l_grid.down):
            return
    if r_grid.right:
        rr_grid = board[row][col + 2]
        if not (r_grid.down or rr_grid.down):
            return
    if r_grid.up:
        if not (r_grid.right or r_grid.down):
            return
    l_grid.right = 0
    r_grid.left = 0


def set_pillar(board, row, col):
    grid = board[row][col]
    if grid.down or grid.left or grid.right:
        board[row][col].up = 1
        board[row - 1][col].down = 1


def del_pillar(board, row, col):
    u_grid = board[row - 1][col]
    d_grid = board[row][col]

    if u_grid.left:
        ul_grid = board[row - 1][col - 1]
        if not (ul_grid.down or (ul_grid.left and u_grid.right)):
            return
    if u_grid.right:
        ur_grid = board[row - 1][col + 1]
        if not (ur_grid.down or (u_grid.left and ur_grid.right)):
            return
    if u_grid.up:
        if not (u_grid.left or u_grid.right):
            return
    u_grid.down = 0
    d_grid.up = 0


def solution(n, build_frame):
    board = [[Node() for _ in range(n + 1)] for __ in range(n + 1)]
    for i in range(n + 1):
        board[n][i].down = 1

    for x, y, a, b in build_frame:
        x, y = n - y, x
        if a:
            if b:
                set_bridge(board, x, y)
            else:
                del_bridge(board, x, y)
        else:
            if b:
                set_pillar(board, x, y)
            else:
                del_pillar(board, x, y)

    answer = []
    for c in range(n + 1):
        for r in range(n, -1, -1):
            grid = board[r][c]
            if grid.up:     # pillar
                answer.append([c, n - r, 0])
            if grid.right:  # bridge
                answer.append([c, n - r, 1])

    return answer


cases = [
    (5,
     [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]),
    (5,
     [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
      [1, 1, 1, 0], [2, 2, 0, 1]])
]

for case in cases:
    print(solution(*case))
