def solve(origin, arr, depth, length):
    global answer
    if depth == length:
        answer = max(answer, len(arr))
    else:
        solve(origin, arr, depth + 1, length)
        for ele in origin[depth]:
            try:
                if ele > arr[-1]:
                    ar = arr[:]
                    ar.append(ele)
                    solve(origin, ar, depth + 1, length)
            except:
                ar = arr[:]
                ar.append(ele)
                solve(origin, ar, depth + 1, length)


def main():
    global answer
    string1 = input()
    string2 = input()
    data = {}
    for ele in set(string2):
        if not data.get(ele):
            temp = []
            idx = 0
            for ch in string2:
                if ch == ele:
                    temp.append(idx)
                idx += 1
            data[ele] = temp

    length = len(string1)
    answer = 0
    hubo_list = [[]] * length
    for i in range(length):
        if data.get(string1[i]):
            hubo_list[i] = data[string1[i]]
    solve(hubo_list, [], 0, length)
    print(answer)


main()

# AAABBBBBBBBDEFEFDAGHDG
# CCCCCCAACCCCACCCB

# AAB
# AB

# SKDFHWEODJKSFSDFJK
# WKJSDHFOWEFKJDVKSDF

# CAPCK
# AA