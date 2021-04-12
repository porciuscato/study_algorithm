from heapq import heappop, heappush
PAPER_SIZE = 10


def is_color_paper_match(r: int, c: int, size: int, paper, covered) -> bool:
    if not (r + size <= PAPER_SIZE and c + size <= PAPER_SIZE):
        return False
    for row in range(r, r + size):
        for col in range(c, c + size):
            if not paper[row][col] or covered[row][col]:
                return False
    return True


def cover_paper(r, c, size, covered):
    for row in range(r, r + size):
        for col in range(c, c + size):
            covered[row][col] = True


# def search(paper, covered, left_coloredpaper, sizes) -> int:
#     answer = 0
#     for size in sizes:
#         for r in range(PAPER_SIZE - size + 1):
#             for c in range(PAPER_SIZE - size + 1):
#                 if paper[r][c] == 1 and not covered[r][c]:
#                     if is_color_paper_match(r, c, size, paper, covered):
#                         cover_paper(r, c, size, covered)
#                         answer += 1
#                         left_coloredpaper[size - 1] -= 1
#                         if left_coloredpaper[size - 1] < 0:
#                             return -1
#     return answer


def solve(r, c, paper, covered, left_coloredpaper):
    global answers
    left_coloredpaper_dup = left_coloredpaper[:]
    covered_dup = []

    for i in range(PAPER_SIZE):
        temp = []
        for j in range(PAPER_SIZE):
            temp.append(covered[i][j])
        covered_dup.append(temp)

    flag = True
    while r < PAPER_SIZE:
        for size in range(5, 0, -1):
            if is_color_paper_match(r, c, size, paper, covered_dup):
                flag = False
                if left_coloredpaper_dup[size - 1] - 1 < 0:
                    heappush(answers, -1)
                    return
                else:
                    cover_paper(r, c, size, covered_dup)
                    left_coloredpaper_dup[size - 1] -= 1
                    solve(r, c, paper, covered_dup, left_coloredpaper_dup)
        c += 1
        if c == PAPER_SIZE:
            r += 1
            c = 0
    if flag:
        heappush(answers, 25 - sum(left_coloredpaper_dup))


def main():
    global answers
    paper = [list(map(int, input().split())) for _ in range(PAPER_SIZE)]
    covered = [[False for _ in range(PAPER_SIZE)] for __ in range(PAPER_SIZE)]
    left_coloredpaper = [5, 5, 5, 5, 5]
    solve(0, 0, paper, covered, left_coloredpaper)


if __name__ == "__main__":
    answers = []
    main()
    while answers:
        answer = heappop(answers)
        if answer != -1:
            print(answer)
            break
    else:
        print(-1)


# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0


# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 0 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 0 0 0 0