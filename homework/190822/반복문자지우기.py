for T in range(1, int(input()) + 1):
    word = list(input())
    while 1:
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                word.pop(i)
                word.pop(i)
                break
        else:
            break

    print('#{} {}'.format(T, len(word)))
