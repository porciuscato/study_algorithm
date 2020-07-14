import sys

input = sys.stdin.readline


def main():
    word = input()
    while word != '0\n':
        lp, rp = 0, len(word) - 2
        is_pelin = True
        while lp < rp:
            if word[lp] != word[rp]:
                print("no")
                is_pelin = False
                break
            lp += 1
            rp -= 1
        if is_pelin:
            print("yes")
        word = input()


if __name__ == '__main__':
    main()
