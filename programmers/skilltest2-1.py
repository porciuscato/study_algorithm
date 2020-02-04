s = 'baabaa'
# 이걸 리스트로 변환
s = list(s)

check = []

for ele in s:
    if not check:
        check.append(ele)
    else:
        last = check[-1]
        if last == ele:
            check.pop(-1)
        else:
            check.append(ele)
if check:
    return 0
else:
    return 1
        