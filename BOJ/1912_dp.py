def main():
    n = int(input())
    array = list(map(int, input().split()))
    board = [0 for _ in range(n)]
    board[0] = array[0]
    ans = array[0]
    for i in range(1, n):
        board[i] = max(board[i - 1] + array[i], array[i])
        if ans < board[i]:
            ans = board[i]
    print(ans)


main()


