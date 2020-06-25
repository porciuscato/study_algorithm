from collections import deque
import random


def main():
    # n = int(input())
    n = 100000
    # array = list(map(int, input().split()))
    array = [random.randint(-1000, 1000) for _ in range(n)]
    board = deque([deque([0 for _ in range(n + 1)])])
    ans = -2e12
    for row in range(1, n + 1):
        board.append(deque([0 for _ in range(n + 1)]))
        for col in range(row, n + 1):
            board[1][col] = board[0][col - 1] + array[col - 1]
            ans = max(ans, board[1][col])
        board.popleft()
    print(ans)


main()

