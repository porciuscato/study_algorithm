import sys

input = sys.stdin.readline


def move_block_down(typ, row, col):
    if typ == 1:
        for r in range(4, 10):
            if board[r][col]:
                board[r - 1][col] = 1
                break
        else:
            board[9][col] = 1
    elif typ == 2:
        for r in range(4, 10):
            if board[r][col] or board[r][col + 1]:
                board[r - 1][col] = 2
                board[r - 1][col + 1] = 2
                break
        else:
            board[9][col] = 2
            board[9][col + 1] = 2
    elif typ == 3:
        for r in range(4, 10):
            if board[r][col]:
                board[r - 2][col] = 3
                board[r - 1][col] = 3
                break
        else:
            board[8][col] = 3
            board[9][col] = 3


def move_block_right(typ, row, col):
    if typ == 1:
        for c in range(4, 10):
            if board[row][c]:
                board[row][c - 1] = 1
                break
        else:
            board[row][9] = 1
    elif typ == 2:
        for c in range(4, 10):
            if board[row][c]:
                board[row][c - 2] = 2
                board[row][c - 1] = 2
                break
        else:
            board[row][8] = 2
            board[row][9] = 2
    elif typ == 3:
        for c in range(4, 10):
            if board[row][c] or board[row + 1][c]:
                board[row][c - 1] = 3
                board[row + 1][c - 1] = 3
                break
        else:
            board[row][9] = 3
            board[row + 1][9] = 3


def check_score_down():
    global score
    rows = []
    for i in range(4, 10):
        for j in range(4):
            if not board[i][j]:
                break
        else:
            rows.append(i)
    if rows:
        score += len(rows)
        for row in rows:
            for j in range(4):
                board[row][j] = 0
        heights = [9, 9, 9, 9]
        temp = [[0 for _ in range(4)] for __ in range(10)]
        for r in range(9, 3, -1):
            for c in range(4):
                if board[r][c] == 1 or board[r][c] == 3:
                    temp[heights[c]][c] = board[r][c]
                    heights[c] -= 1
                elif board[r][c] == 2:
                    if c <= 2 and board[r][c + 1] == 2:
                        mn = min(heights[c], heights[c + 1])
                        temp[mn][c] = 2
                        temp[mn][c + 1] = 2
                        heights[c] = mn - 1
                        heights[c + 1] = mn - 1
        for r in range(4, 10):
            for c in range(4):
                board[r][c] = temp[r][c]
        return True
    return False


def check_score_right():
    global score
    cols = []
    for j in range(4, 10):
        for i in range(4):
            if not board[i][j]:
                break
        else:
            cols.append(j)
    if cols:
        score += len(cols)
        for col in cols:
            for i in range(4):
                board[i][col] = 0
        temp = [[0 for _ in range(10)] for __ in range(4)]
        heights = [9, 9, 9, 9]
        for c in range(9, 3, -1):
            for r in range(4):
                if board[r][c] == 1 or board[r][c] == 2:
                    temp[r][heights[r]] = board[r][c]
                    heights[r] -= 1
                elif board[r][c] == 3:
                    if r <= 2 and board[r + 1][c] == 3:
                        mn = min(heights[r], heights[r + 1])
                        temp[r][mn] = 3
                        temp[r + 1][mn] = 3
                        heights[r] = mn - 1
                        heights[r + 1] = mn - 1
        for r in range(4):
            for c in range(4, 10):
                board[r][c] = temp[r][c]
        return True
    return False


def move_down_all(down):
    for j in range(4):
        temp = []
        for i in range(4, 10 - down):
            temp.append(board[i][j])
        if down == 1:
            temp = [0] + temp
        elif down == 2:
            temp = [0, 0] + temp
        for i in range(6):
            board[4 + i][j] = temp[i]


def move_right_all(right):
    for i in range(4):
        temp = []
        for j in range(4, 10 - right):
            temp.append(board[i][j])
        if right == 1:
            temp = [0] + temp
        elif right == 2:
            temp = [0, 0] + temp
        for j in range(6):
            board[i][4 + j] = temp[j]


def remove_light():
    down = 0
    right = 0
    for i in range(4, 6):
        for j in range(4):
            if board[i][j]:
                down += 1
                break
    for j in range(4, 6):
        for i in range(4):
            if board[i][j]:
                right += 1
                break
    if down:
        move_down_all(down)
    if right:
        move_right_all(right)


def solve(typ, row, col):
    move_block_down(typ, row, col)
    move_block_right(typ, row, col)
    while check_score_down():
        continue
    while check_score_right():
        continue
    remove_light()


def print_answer():
    blocks = 0
    for i in range(4):
        for j in range(4, 10):
            if board[i][j]:
                blocks += 1
    for i in range(4, 10):
        for j in range(4):
            if board[i][j]:
                blocks += 1
    print(f'{score}\n{blocks}')


if __name__ == "__main__":
    board = [[0 for _ in range(10)] for __ in range(10)]
    score = 0
    for _ in range(int(input())):
        t, x, y = map(int, input().split())
        solve(t, x, y)
    print_answer()

# 6
# 1 0 0
# 1 0 2
# 2 0 0
# 3 0 2
# 2 0 1
# 3 0 3