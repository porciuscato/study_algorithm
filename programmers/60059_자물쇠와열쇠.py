def make_board(lock, k_size, l_size, B_size):
    BOARD = [[0 for _ in range(B_size)] for __ in range(B_size)]
    for i in range(k_size - 1, k_size + l_size - 1):
        for j in range(k_size - 1, k_size + l_size - 1):
            BOARD[i][j] = lock[i - k_size + 1][j - k_size + 1]
    return BOARD


def check(BOARD, k_size, l_size):
    for i in range(k_size - 1, k_size + l_size - 1):
        for j in range(k_size - 1, k_size + l_size - 1):
            if BOARD[i][j] != 1:
                return False
    return True


def insert_key(key, BOARD, i, j, k_size):
    for r in range(k_size):
        for c in range(k_size):
            BOARD[i + r][j + c] += key[r][c]


def restore_board(key, BOARD, i, j, k_size):
    for r in range(k_size):
        for c in range(k_size):
            BOARD[i + r][j + c] -= key[r][c]


def rotate_key(key, k_size):
    result1 = [[key[j][k_size - 1 - i] for j in range(k_size)] for i in range(k_size)]
    result2 = [[key[k_size - 1 - i][k_size - 1 - j] for j in range(k_size)] for i in range(k_size)]
    result3 = [[key[k_size - 1 - j][i] for j in range(k_size)] for i in range(k_size)]
    return key, result1, result2, result3


def solution(key, lock):
    k_size = len(key)
    l_size = len(lock)
    B_size = 2 * k_size + l_size - 2
    BOARD = make_board(lock, k_size, l_size, B_size)
    keys = rotate_key(key, k_size)

    for i in range(B_size - k_size + 1):
        for j in range(B_size - k_size + 1):
            for rot in range(4):
                key = keys[rot]
                insert_key(key, BOARD, i, j, k_size)
                if check(BOARD, k_size, l_size):
                    return True
                restore_board(key, BOARD, i, j, k_size)
    return False


arr = [
    ([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
]

for ar in arr:
    print(solution(*ar))
