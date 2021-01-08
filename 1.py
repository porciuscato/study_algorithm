def editDistance(source, target):
    mx_same_cnt = 0
    # mx_same_idx = -1
    mx_result = ''
    result_list = []
    for i in range(26):
        result = ''
        for word in source:
            asc = ord(word) + i
            if asc >= 123:
                asc -= 26
            result += chr(asc)
        if result == target:
            return 0
        else:
            ri = 0
            ti = 0
            same_cnt = 0
            while ri < len(result):
                if result[ri] == target[ti]:
                    ri += 1
                    ti += 1
                    same_cnt += 1
                else:
                    ri += 1
            if mx_same_cnt <= same_cnt:
                mx_same_cnt = same_cnt
                # mx_same_idx = i
                mx_result = result
                print(result)
                result_list.append(mx_result)
    ans = 1000000
    for temp in result_list:
        total = 0
        mi = 0
        ti = 0
        while ti < len(target):
            try:
                if temp[mi] == target[ti]:
                    mi += 1
                    ti += 1
                else:
                    mi += 1
                    total += 1
            except IndexError:
                total += 1
                ti += 1
        ans = min(ans, total)
    return ans


# editDistance('abc', 'gzu')
print(editDistance('abdh', 'bcif'))
