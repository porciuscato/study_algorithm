from heapq import heappop, heappush
PAPER_SIZE = 10


def is_color_paper_match(row: int, col: int, size: int, paper, covered) -> bool:
    if row + size <= PAPER_SIZE and col + size <= PAPER_SIZE:
        for r in range(row, row + size):
            for c in range(col, col + size):
                if not paper[r][c] or covered[r][c]:
                    return False
        return True
    else:
        return False


def cover_paper(row: int, col: int, size: int, covered, key=True):
    for r in range(row, row + size):
        for c in range(col, col + size):
            covered[r][c] = True if key else False


def solve(r, c, paper, covered, left_colored_paper):
    global answers
    if r == PAPER_SIZE:
        heappush(answers, 25 - sum(left_colored_paper))
    else:
        if paper[r][c] and not covered[r][c]:
            for size in range(5, 0, -1):
                if is_color_paper_match(r, c, size, paper, covered):
                    if left_colored_paper[size - 1] - 1 >= 0:
                        left_colored_paper[size - 1] -= 1
                        cover_paper(r, c, size, covered)
                        solve(r, c, paper, covered, left_colored_paper)
                        cover_paper(r, c, size, covered, False)
                        left_colored_paper[size - 1] += 1
        else:
            c += 1
            if c == PAPER_SIZE:
                r += 1
                c = 0
            solve(r, c, paper, covered, left_colored_paper)


def main():
    global answers
    paper = [list(map(int, input().split())) for _ in range(PAPER_SIZE)]
    covered = [[False for _ in range(PAPER_SIZE)] for __ in range(PAPER_SIZE)]
    left_colored_paper = [5, 5, 5, 5, 5]
    solve(0, 0, paper, covered, left_colored_paper)


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

# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0