import random
import time


def main():
    # n = int(input())
    n = 10000
    # array = list(map(int, input().split()))
    array = [random.randint(-1000, 1000) for _ in range(n)]
    board = [0 for _ in range(n)]
    ans = array[0]
    for row in range(1, n + 1):
        for col in range(row, n + 1):
            board[col] = board[col - 1] + array[col - 1]
            if ans < board[col]:
                ans = board[col]
    print(ans)


st = time.time()
main()
print(time.time() - st)


