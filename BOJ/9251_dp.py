def main():
    s1 = input()
    s2 = input()
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    board = [[0 for _ in range(l1)] for __ in range(l2)]
    for row in range(1, l2):
        for col in range(1, l1):
            if s2[row - 1] == s1[col - 1]:
                board[row][col] = board[row - 1][col - 1] + 1
            else:
                board[row][col] = max(board[row][col - 1], board[row - 1][col])
    print(board[l2 - 1][l1 - 1])


main()

