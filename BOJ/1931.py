def main():
    n = int(input())
    meetings = []
    for _ in range(n):
        meetings.append(tuple(map(int, input().split())))
    meetings.sort(key=lambda x: (x[0], x[1]))
    ans = 1
    cri = meetings[n - 1][0]
    for i in range(n - 2, - 1, -1):
        if cri >= meetings[i][1]:
            ans += 1
            cri = meetings[i][0]
    print(ans)


main()
