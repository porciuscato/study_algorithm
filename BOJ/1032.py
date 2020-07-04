def main():
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    length = len(words[0])
    answer = []
    for col in range(length):
        word = words[0][col]
        for row in range(1, N):
            if word != words[row][col]:
                answer.append("?")
                break
        else:
            answer.append(word)
    print("".join(answer))


main()
