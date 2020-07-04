def condition(smaller, bigger):
    s_len = len(smaller)
    b_len = len(bigger)
    if s_len < b_len:
        return True
    elif s_len > b_len:
        return False
    else:
        s_sum = 0
        b_sum = 0
        for i in range(s_len):
            asc_s = ord(smaller[i])
            asc_b = ord(bigger[i])
            if 48 <= asc_s <= 57:
                s_sum += int(smaller[i])
            if 48 <= asc_b <= 57:
                b_sum += int(bigger[i])
        if s_sum < b_sum:
            return True
        elif s_sum > b_sum:
            return False
        else:
            for i in range(s_len):
                asc_s = ord(smaller[i])
                asc_b = ord(bigger[i])
                if asc_s < asc_b:
                    return True
                elif asc_s > asc_b:
                    return False


def q_sort(arr, left, right):
    if left < right:
        pivot, lp, rp = left, left, right
        while lp < rp:
            while lp < right and condition(arr[lp], arr[pivot]):
                lp += 1
            while rp > left and condition(arr[pivot], arr[rp]):
                rp -= 1
            if lp < rp:
                arr[lp], arr[rp] = arr[rp], arr[lp]
        if condition(arr[rp], arr[pivot]):
            arr[rp], arr[pivot] = arr[pivot], arr[rp]
        q_sort(arr, left, rp - 1)
        q_sort(arr, rp + 1, right)


def quick_sort(arr):
    q_sort(arr, 0, len(arr) - 1)


def main():
    numbers = [input() for _ in range(int(input()))]
    quick_sort(numbers)
    for number in numbers:
        print(number)


main()
