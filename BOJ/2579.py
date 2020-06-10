def main():
    N = int(input())
    numbers = [0] * (N + 1)
    for i in range(1, N + 1):
        numbers[i] = int(input())
    answer = [[0 for _ in range(N + 1)] for __ in range(2)]
    answer[0][1] = numbers[1]
    answer[1][1] = numbers[1]
    for idx in range(2, N + 1):
        answer[0][idx] = max(answer[0][idx - 2] + numbers[idx], answer[1][idx - 2] + numbers[idx])
        answer[1][idx] = answer[0][idx - 1] + numbers[idx]
    print(max(answer[0][N], answer[1][N]))


main()
