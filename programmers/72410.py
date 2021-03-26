def solution(new_id):
    ans = ["" for _ in range(7)]
    # rule 1
    for i in range(len(new_id)):
        if new_id[i].isalpha():
            ans[0] += new_id[i].lower()
        else:
            ans[0] += new_id[i]
    # rule 2
    for i in range(len(ans[0])):
        if ans[0][i].isalpha() or ans[0][i].isdigit() or ans[0][i] in ('-', '_', '.'):
            ans[1] += ans[0][i]
    # rule 3
    for i in range(len(ans[1])):
        if ans[1][i] == '.':
            try:
                if ans[1][i + 1] != '.':
                    ans[2] += ans[1][i]
            except IndexError:
                ans[2] += ans[1][i]
        else:
            ans[2] += ans[1][i]
    # rule 4
    if ans[2][0] == '.':
        ans[3] = ans[2][1:]
    else:
        ans[3] = ans[2][:]
    try:
        if ans[3][-1] == '.':
            ans[3] = ans[3][:-1]
    except IndexError:
        pass
    # rule 5
    if not ans[3]:
        ans[4] = "a"
    else:
        ans[4] = ans[3][:]
    # rule 6
    if len(ans[4]) >= 16:
        ans[5] = ans[4][:15]
        if ans[5][-1] == '.':
            ans[5] = ans[5][:-1]
    else:
        ans[5] = ans[4][:]
    # rule 7
    if len(ans[5]) <= 2:
        alpha = ans[5][-1]
        ans[6] = ans[5][:]
        while (len(ans[6]) < 3):
            ans[6] += alpha
    else:
        ans[6] = ans[5][:]
    return ans[6]


cases = [
    	"...!@BaT#*..y.abcdefghijklm",
        "z-+.^.",
        "=.=",
        "123_.def",
        "abcdefghijklmn.p",
]

for case in cases:
    print(solution(case))

