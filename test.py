# 중복 순열

LIST = (1, 2, 3)


def permu(arr, depth):
    if depth == len(LIST):
        print(arr)
    else:
        for idx in range(len(LIST)):
            ar = arr[:]
            ar.append(LIST[idx])
            permu(ar, depth + 1)

permu([], 0)