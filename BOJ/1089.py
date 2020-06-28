import sys

input = sys.stdin.readline

numbers = [['###', '#.#', '#.#', '#.#', '###'],
           ['..#', '..#', '..#', '..#', '..#'],
           ['###', '..#', '###', '#..', '###'],
           ['###', '..#', '###', '..#', '###'],
           ['#.#', '#.#', '###', '..#', '..#'],
           ['###', '#..', '###', '..#', '###'],
           ['###', '#..', '###', '#.#', '###'],
           ['###', '..#', '..#', '..#', '..#'],
           ['###', '#.#', '###', '#.#', '###'],
           ['###', '#.#', '###', '..#', '###']]


def solve(arr, N, case):
    global total
    n = N - 1
    for ar in arr:
        cipher = 10 ** n
        times = case // len(ar)
        total += sum(ar) * times * cipher
        n -= 1


def main():
    N = int(input())
    data = [input() for _ in range(5)]
    hubo = []
    for n in range(N):
        hubo.append([])
    for j in range(5):
        for i in range(0, 4 * N - 1, 4):
            hubo[i // 4].append(data[j][i:i + 3])

    possibles = [[] for _ in range(N)]
    for i in range(N):
        for j in range(10):
            row, col = 0, 0
            while row < 5:
                if numbers[j][row][col] == "." and hubo[i][row][col] == "#":
                    break
                else:
                    col += 1
                    if col == 3:
                        col = 0
                        row += 1
            else:
                possibles[i].append(j)
    case = 1
    for possible in possibles:
        if not possible:
            print(-1)
            return
        else:
            case *= len(possible)
    solve(possibles, N, case)
    print(round((total / case), 5))


total = 0
main()

# 9
# ..#...#...#...#...#...#...#...#...#
# ...................................
# ..#...#...#...#...#...#...#...#...#
# ...................................
# ..#...#...#...#...#...#...#...#...#


# 8
# ..#...#...#...#...#...#...#...#
# ...............................
# ..#...#...#...#...#...#...#...#
# ...............................
# ..#...#...#...#...#...#...#...#