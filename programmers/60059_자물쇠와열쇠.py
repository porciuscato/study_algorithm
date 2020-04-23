def rotate(arr, size):
    new_arr = []
    for i in range(size):
        temp = []
        for j in range(size - 1, -1, -1):
            temp.append(arr[j][i])
        new_arr.append(temp)
    return new_arr


def check(BOARD, KEY, B_size, K_size):
    total_size = B_size + (K_size - 1) * 2
    board = []
    for i in range(BOARD):
        board += BOARD[i][:]
    for i in range(B_size - K_size - 1, B_size + K_size):
        for j in range(B_size - K_size - 1, B_size + K_size):
            pass
    return 0


def solution(key, lock):
    lock_size = len(lock)
    BOARD = [[0] * (lock_size * 3) for _ in range(lock_size * 3)]
    for i in range(lock_size, lock_size * 2):
        for j in range(lock_size, lock_size * 2):
            BOARD[i][j] = lock[i - lock_size][j - lock_size]
    key_size = len(key)
    for i in range(4):
        key = rotate(key, key_size)
        if check(BOARD, key, lock_size, key_size):
            return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
