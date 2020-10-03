sentence = input().split()
space = int(input())
alphas = list(map(int, input().split()))
if space < len(sentence) - 1:
    print(-1)
else:
    title = ''
    flag = True
    for word in sentence:
        if flag:
            cap = word[0].upper()
            title += cap
            alphas[ord(cap) - 65] -= 1
            i = 0
            while i < len(word):
                letter = word[i]
                j = i + 1
                while j < len(word):
                    if letter == word[j]:
                        j += 1
                        i += 1
                    else:
                        break
                val = ord(letter)
                idx = val - 97 if val >= 97 else val - 65
                alphas[idx] -= 1
                if alphas[idx] < 0:
                    flag = False
                    title = -1
                    break
                i += 1
    print(title)
