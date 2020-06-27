def eratos(N):
    array = [True for _ in range(N + 1)]
    for j in range(2, (N // 2) + 1):
        if array[j]:
            for jj in range(j + j, N + 1, j):
                array[jj] = False
    return [i for i in range(2, N + 1) if array[i]]


def main():
    P, K = map(int, input().split())
    for ele in eratos(10 ** 6):
        if P % ele == 0:
            v = min(ele, P // ele)
            break
    else:
        print("GOOD")
        return
    print("GOOD" if v >= K else "BAD {}".format(v))


main()
