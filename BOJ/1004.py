import sys

input = sys.stdin.readline


def main():
    for t in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        ans = 0
        check = [0] * n
        for i in range(n):
            cx, cy, r = map(int, input().split())
            if (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2:
                check[i] += 1
            if (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2:
                check[i] += 2
            if check[i] == 1:
                ans += 1
            elif check[i] == 2:
                ans += 1
        print(ans)


main()
